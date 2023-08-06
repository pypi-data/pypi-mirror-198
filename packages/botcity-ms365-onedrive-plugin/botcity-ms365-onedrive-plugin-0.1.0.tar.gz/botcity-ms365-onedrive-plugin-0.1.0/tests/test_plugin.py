import os
from uuid import uuid4

import conftest
from botcity.plugins.ms365.onedrive import MS365OneDrivePlugin


def test_return_existing_folder(bot: MS365OneDrivePlugin):
    folder = bot.get_file_by_path(f"/{conftest.DRIVE_FOLDER_NAME}")
    assert folder.name == conftest.DRIVE_FOLDER_NAME


def test_return_none_for_non_existent_file(bot: MS365OneDrivePlugin):
    file = bot.get_file_by_name("file.txt")
    assert file is None


def test_create_folder(bot: MS365OneDrivePlugin):
    folder_name = f"subfolder-{str(uuid4())}"
    created_folder = bot.create_folder(folder_name=folder_name, 
                                       create_on_path=f"/{conftest.DRIVE_FOLDER_NAME}")
    assert created_folder.is_folder


def test_upload_file(bot: MS365OneDrivePlugin, tmp_folder: str):
    file_path = f"{tmp_folder}/Test_Upload.txt"
    conftest.create_file(path=file_path, content="test")
    file = bot.upload_file(local_file_path=file_path, 
                           destination_folder_path=f"/{conftest.DRIVE_FOLDER_NAME}")
    os.remove(file_path)
    assert file.is_file


def test_download_file(bot: MS365OneDrivePlugin, tmp_folder: str):
    file_path = f"{tmp_folder}/Test_Upload.txt"
    bot.download_file(file_path=f"/{conftest.DRIVE_FOLDER_NAME}/Test_Upload.txt",
                      to_path=tmp_folder)
    assert os.path.isfile(file_path)


def test_return_all_files_from_root_folder(bot: MS365OneDrivePlugin):
    files = list(bot.get_files())
    assert len(files) >= 1


def test_do_not_return_any_files_for_empty_folders(bot: MS365OneDrivePlugin):
    bot.create_folder(folder_name="Empty Folder", create_on_path=f"/{conftest.DRIVE_FOLDER_NAME}")
    subfiles = list(bot.get_files_from_parent_folder(f"/{conftest.DRIVE_FOLDER_NAME}/Empty Folder"))
    assert len(subfiles) == 0


def test_return_all_files_from_parent_folder(bot: MS365OneDrivePlugin):
    subfiles = list(bot.get_files_from_parent_folder(f"/{conftest.DRIVE_FOLDER_NAME}"))
    assert len(subfiles) == 3
