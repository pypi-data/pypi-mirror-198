import argparse
import os
import pathlib
import shutil
import zipfile

from colorama import Fore, Style

import pyromname.crc
import pyromname.file
import pyromname.io
import pyromname.rom_database
import pyromname.seven_zip


def print_failure(text):
    """ Print a failure message. """

    print(Fore.RED, text, Style.RESET_ALL, sep="")


def print_partialsuccess(text):
    """ Print a partial sucess message. """

    print(Fore.MAGENTA, text, Style.RESET_ALL, sep="")


def print_success(text):
    """ Print a success message. """

    print(Fore.GREEN, text, Style.RESET_ALL, sep="")

# pyromname.file.FileStatus.PARTIAL_SUCCESS
# => Le traitement de l'archive est un succès partiel. L'archive contient au moins une ROM reconnue.
# pyromname.file.FileStatus.SUCCESS
# => le traitement de l'archive est un succès: on peut supprimer. L'archive ne contient que des ROM reconnues.
# pyromname.file.FileStatus.FAILURE
# => l'archive ne contient aucune ROM reconnue.

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("dat_dir", help="DAT directory")
    parser.add_argument("rom_dir", help="Rom directory")
    parser.add_argument("-l", "--limit", type=int, help="Limit")
    parser.add_argument("-e", "--extract", help="Extract valid rom")
    parser.add_argument("-c", "--compress", help="Zip extracted rom", action="store_true")
    parser.add_argument(
        "-m", "--move", help="Move rom to ok/ko sub folder", action="store_true"
    )
    parser.add_argument("-d", "--dry-run", help="Read only mode", action="store_true")
    parser.add_argument("-u", "--dump", help="Dump the list of CRC", action="store_true")
    parser.add_argument("-k", "--check", help="Check rom_dir", action="store_true")
    args = parser.parse_args()

    dat_dir = args.dat_dir
    rom_dir = args.rom_dir
    destination_dir = args.extract
    limit = args.limit
    move = args.move
    dry_run = args.dry_run
    compress = args.compress
    dump = args.dump
    check = args.check
    # rom_dir = destination_dir

    pyromname.file.File.rom_database = pyromname.rom_database.RomDatabase(dat_dir)

    ok_dir = os.path.join(rom_dir, "ok")
    ko_dir = os.path.join(rom_dir, "ko")
    err_dir = os.path.join(rom_dir, "err")
    ok_file = os.path.join(rom_dir, "crc.txt")

    if move:
        pathlib.Path(ok_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(ko_dir).mkdir(parents=True, exist_ok=True)
        pathlib.Path(err_dir).mkdir(parents=True, exist_ok=True)

    for path, _, files in os.walk(rom_dir):
        if path in [ok_dir, ko_dir, err_dir]:
            print(f"Skipping {path}")
            continue

        for filename in files:
            filepath = os.path.join(path, filename)

            # if not "0822" in file:
            #    continue

            if limit is not None:
                if limit == 0:
                    break
                limit = limit - 1

            if filepath.split(".")[-1] in pyromname.file.File.rom_database.extensions:
                archive_file = pyromname.file.SingleFile(filepath)  # type: pyromname.file.File
            else:
                archive_file = pyromname.file.ArchiveFile(filepath)

            if not destination_dir:
                if check:
                    msg = f"Check {filepath}"
                    try:
                        status = archive_file.check()
                        if status:
                            print_success(msg)
                        else:
                            print_partialsuccess(msg)
                    except pyromname.file.FileException as exception:
                        print_failure(msg)
                        print_failure(f"  KO '{filepath}' {exception.message}.")
                else:
                    msg = f"Listing {filepath}"
                    try:
                        (status, results) = archive_file.content
                        if status == pyromname.file.FileStatus.SUCCESS:
                            print_success(msg)
                        elif status == pyromname.file.FileStatus.PARTIAL_SUCCESS:
                            print_partialsuccess(msg)
                        else:
                            print_failure(msg)
                        for (filename_in_archive, crc, name_in_db) in results:
                            if name_in_db:
                                name, database = name_in_db
                                print_success(
                                    f"  OK '{filename_in_archive}' with CRC '{crc}' match '{name}' found in '{database}'."
                                )
                            else:
                                print_failure(
                                    f"  KO '{filename_in_archive}' with CRC '{crc}' not found."
                                )
                    except pyromname.file.FileException as exception:
                        print_failure(msg)
                        print_failure(f"  KO '{filepath}' {exception.message}.")
            else:
                msg = f"Extraction {filepath}"
                status = None
                try:
                    status, extract_results = archive_file.extract(destination_dir)
                    if status == pyromname.file.FileStatus.SUCCESS:
                        print_success(msg)
                    elif status == pyromname.file.FileStatus.PARTIAL_SUCCESS:
                        print_partialsuccess(f"{msg}")
                    else:
                        print_failure(msg)
                    for (filename_in_archive, crc, name_in_db, extracted_content) in extract_results:
                        if name_in_db is None:
                            print_failure(f"  KO '{filename_in_archive}' with CRC '{crc}' not found.")
                        elif extracted_content is None:
                            print_failure(
                                f"  KO '{filename_in_archive}' with CRC '{crc}' failed to extract."
                            )
                        else:
                            name, database = name_in_db
                            print_success(
                                f"  OK '{filename_in_archive}' with CRC '{crc}' match '{name}' found in '{database}' extracted to '{extracted_content}'."
                            )
                except pyromname.file.FileException as exception:
                    print(type(exception))
                    print_failure(msg)
                    print_failure(f"  KO '{filepath}' {exception.message}.")

                if move:
                    if status is None:
                        if not dry_run:
                            shutil.move(filepath, err_dir)
                        else:
                            print(f"DRY-RUN Move file {filepath} to {err_dir}")
                    elif status == pyromname.file.FileStatus.SUCCESS:
                        if not dry_run:
                            shutil.move(filepath, ok_dir)
                        else:
                            print(f"DRY-RUN Move file {filepath} to {ok_dir}")
                    elif status == pyromname.file.FileStatus.FAILURE:
                        if not dry_run:
                            shutil.move(filepath, ko_dir)
                        else:
                            print(f"DRY-RUN Move file {filepath} to {ko_dir}")

    if compress:
        print(f"compress {rom_dir}")
        for path, _, files in os.walk(rom_dir):
            for filename in files:
                file = os.path.join(path, filename)
                if file.split(".")[-1] in pyromname.file.File.rom_database.extensions:
                    print(f"Zip file {file}")
                    original_filename = pyromname.io.get_original_filename(filename)
                    (name, _) = os.path.splitext(filename)
                    zipfilename = pyromname.io.get_destination_filename(path, f"{name}.zip")

                    with zipfile.ZipFile(
                        zipfilename, "w", zipfile.ZIP_DEFLATED, compresslevel=9
                    ) as myzip:
                        myzip.write(file, original_filename)

                    zip_is_good = False
                    with zipfile.ZipFile(zipfilename, "r") as myzip:
                        if myzip.testzip() is None:
                            zip_is_good = True
                    if zip_is_good:
                        if not dry_run:
                            os.remove(file)
                        else:
                            print(f"DRY-RUN Remove file {file}")

    pyromname.file.File.rom_database.stats()
    if dump:
        pyromname.file.File.rom_database.dump_found_crc(ok_file)
