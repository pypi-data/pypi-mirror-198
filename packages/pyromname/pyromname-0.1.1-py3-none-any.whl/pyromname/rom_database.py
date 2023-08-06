import os
from typing import Dict, Set

import defusedxml.ElementTree as ET


class RomDatabase:
    def __init__(self, dat_dir):
        self.dat_dir = dat_dir
        self._xml_files = []
        self._xml_roots = []
        self._found_crc = {} # type: Dict[str,Set[str]]
        self._crc = {} # type: Dict[str,Set[str]]
        for dat_file in [
            os.path.join(self.dat_dir, f)
            for f in os.listdir(self.dat_dir)
            if os.path.isfile(os.path.join(self.dat_dir, f))
        ]:
            self._xml_files.append(dat_file)
            self._xml_roots.append(ET.parse(dat_file).getroot())
            self._found_crc[dat_file] = set()
            self._crc[dat_file] = set()
            exts = set()
            self.names = {}
            for index, xml_root in enumerate(self._xml_roots):
                for rom in xml_root.findall(".//rom"):
                    crc = rom.get("crc")
                    name = rom.get("name")
                    ext = name.split(".")[-1].lower()
                    exts.add(ext)
                    self.names[crc] = (name, self._xml_files[index])
                    self._crc[self._xml_files[index]].add(crc)
            self.extensions = list(exts)

    def name_by_crc(self, crc):
        name_in_db = self.names.get(crc)
        if name_in_db:
            _, db = name_in_db
            self._found_crc[db].add(crc)
        return name_in_db

    def dbs(self):
        pass

    def info(self):
        dict_info = {}
        for xml in self._xml_files:
            dict_info[xml] = (len(self._crc[xml]), len(self._found_crc[xml]))
        return dict_info

    def stats(self):
        print()
        print("Rom founds:")
        for xml in self._xml_files:
            print(
                f"{xml} total {len(self._crc[xml])} found {len(self._found_crc[xml])}"
            )

    def dump_found_crc(self, file):
        with open(file, "w+", encoding="utf-8") as writer:
            for xml in self._xml_files:
                for crc in sorted(self._found_crc[xml]):
                    writer.write(f"{crc}\n")
