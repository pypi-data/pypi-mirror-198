import abc
import functools
import os
from enum import Enum
from typing import List, Tuple

import pyromname.crc
import pyromname.io
import pyromname.rom_database
import pyromname.seven_zip


class FileException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(message)


class FileStatus(Enum):

    SUCCESS = (0,)
    PARTIAL_SUCCESS = (1,)
    FAILURE = 2


class File:

    rom_database: pyromname.rom_database.RomDatabase

    def __init__(self, file):
        self.file = file

    @property
    @abc.abstractmethod
    def content(self) -> Tuple[FileStatus, List[Tuple[str, str, Tuple[str, str]]]]:
        pass

    @abc.abstractmethod
    def extract(
        self, destination_dir
    ) -> Tuple[FileStatus, List[Tuple[str, str, Tuple[str, str], str]]]:
        pass

    def check(self):
        status, content = self.content
        if status == FileStatus.FAILURE:
            return False
        if len(content) != 1:
            return False
        for (filename, _, name_in_db) in content:
            if name_in_db:
                name, _ = name_in_db
                filename_only = os.path.basename(filename)
                if name != filename_only:
                    return False
            else:
                return False

        return True


class SingleFile(File):

    @functools.cached_property
    def content(self):
        try:
            crc = pyromname.crc.crc_from_file(self.file)
        except (IOError, OSError) as exception:
            raise FileException(f"Unable to read {self.file}") from exception

        name_in_db = self.rom_database.name_by_crc(crc)
        if name_in_db:
            return (FileStatus.SUCCESS, [(self.file, crc, name_in_db)])
        else:
            return (FileStatus.FAILURE, [(self.file, crc, name_in_db)])

    def extract(self, destination_dir):
        result = [] # type: List[Tuple[str, str, str, str]]
        status, content = self.content
        if status == FileStatus.FAILURE:
            return (FileStatus.FAILURE, result)
        try:
            for (filename, crc, name_in_db) in content:
                if name_in_db:
                    name, _ = name_in_db
                    pyromname.io.copy_to_dir(filename, destination_dir, name)
                    result.append((filename, crc, name_in_db, name))
        except (IOError, OSError) as exception:
            raise FileException(f"Unable to read {self.file}") from exception

        return (FileStatus.SUCCESS, result)


class ArchiveFile(File):
    def __init__(self, file: str):
        self.archive = pyromname.seven_zip.SevenZip(file)
        super().__init__(file)

    @functools.cached_property
    def content(self):
        result = [] # type: List[Tuple[str, str, str]]
        unknown_content = 0
        try:
            if not self.archive.test():
                return FileStatus.FAILURE, result

            for (filename, crc) in self.archive.content() or []:
                name_in_db = self.rom_database.name_by_crc(crc)
                result.append((filename, crc, name_in_db))
                if not name_in_db:
                    unknown_content += 1

            if len(result) == 0 or unknown_content == len(result):
                return (FileStatus.FAILURE, result)
            if unknown_content > 0:
                return (FileStatus.PARTIAL_SUCCESS, result)
            else:
                return (FileStatus.SUCCESS, result)
        except pyromname.seven_zip.SevenZipException as exception:
            raise FileException(
                f"{exception.message} ({exception.command})"
            ) from exception

    def extract(self, destination_dir):
        result = [] # type: List[Tuple[str, str, str|None, str|None]]
        unknown_content = 0
        status, content = self.content

        try:
            for (filename, crc, name_in_db) in content:
                if name_in_db:
                    name, _ = name_in_db
                    if self.archive.extract_to_specific_filename(
                        filename, destination_dir, name
                    ):
                        result.append((filename, crc, name_in_db, name))
                    else:
                        result.append((filename, crc, name_in_db, None))
                        raise FileException(
                            f"Unable to extract '{filename}' in {self.file}"            
                        )
                else:
                    result.append((filename, crc, None, None))
                    unknown_content += 1
        except pyromname.seven_zip.SevenZipException as exception:
            raise FileException(
                f"{exception.message} ({exception.command})"
            ) from exception
        except (IOError, OSError) as exception:
            raise FileException(f"Unable to read {self.file}") from exception

        if status == FileStatus.FAILURE:
            return (FileStatus.FAILURE, result)
        elif unknown_content > 0:
            return (FileStatus.PARTIAL_SUCCESS, result)
        else:
            return (FileStatus.SUCCESS, result)
