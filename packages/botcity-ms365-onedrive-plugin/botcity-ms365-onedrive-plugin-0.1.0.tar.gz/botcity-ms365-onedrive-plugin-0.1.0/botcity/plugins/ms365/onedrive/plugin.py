from O365.drive import Drive, Storage

from botcity.plugins.ms365.credentials import MS365CredentialsPlugin


class MS365OneDrivePlugin:
    def __init__(self, service_account: MS365CredentialsPlugin) -> None:
        """
        MS365OneDrivePlugin.

        Args:
            service_account (MS365CredentialsPlugin): The authenticated Microsoft365 account.
                The authentication process must be done through the credentials plugin.
        """
        self._onedrive = service_account.ms365_account.storage()
        self._default_drive = self._onedrive.get_default_drive()

    @property
    def onedrive_service(self) -> Storage:
        """
        The Office365/Microsoft365 account service.

        You can use this property to access OneDrive functionality.
        """
        return self._onedrive

    @property
    def default_drive(self) -> Drive:
        """
        The default drive reference.

        You can use this property to access OneDrive functionality.
        """
        return self._default_drive

    def get_files(self):
        """
        Get a list of all files and folders in the OneDrive root folder.

        Returns:
            List[DriveItem]: The list containing the found files.
        """
        files = self.default_drive.get_root_folder()
        return files.get_items()

    def get_file_by_name(self, file_name: str):
        """
        Search for a OneDrive item using its name.

        Args:
            file_name (str): The name of the file to be fetched.

        Returns:
            DriveItem: The found item.
        """
        file = None
        for item in self.default_drive.search(file_name):
            if item.name == file_name:
                file = item
                break
        return file

    def get_files_from_parent_folder(self, folder_path: str):
        """
        Get a list of all files and folders from a specific parent folder.

        Args:
            folder_path (str): The parent folder path in OneDrive.
                The path must be used in the pattern: /path/to/parent/folder.

        Returns:
            List[DriveItem]: The list containing the found files.
        """
        parent_folder = self.get_file_by_path(folder_path)
        if not parent_folder or not parent_folder.is_folder:
            raise ValueError("No folder found using this folder_name.")

        return parent_folder.get_items()

    def get_file_by_path(self, file_path: str):
        """
        Search for a item using its path on OneDrive.

        The file path must be used in the pattern: /path/to/file

        Args:
            file_path (str): The path of the file to be fetched.

        Returns:
            DriveItem: The found item.
        """
        file = self.default_drive.get_item_by_path(file_path)
        return file

    def upload_file(self, local_file_path: str, destination_folder_path: str = ''):
        """
        Upload a file on OneDrive.

        Args:
            local_file_path (str): The path of the file to be uploaded.
            destination_folder_path (str, optional): The destination folder path in OneDrive.
                The path must be used in the pattern: /path/to/parent/folder. Defaults to root folder.

        Returns:
            DriveItem: The reference for the uploaded file.
        """
        folder = self.default_drive.get_root_folder()
        if destination_folder_path:
            item = self.get_file_by_path(destination_folder_path)
            if item and item.is_folder:
                folder = item

        return folder.upload_file(local_file_path)

    def download_file(self, file_path: str, to_path: str = ''):
        """
        Download a file stored on OneDrive.

        Args:
            file_path (str): The file path in OneDrive.
                The path must be used in the pattern: /path/to/file.
            to_path (str, optional): The path where the file will be saved.
                Defaults to the current working dir.
        """
        file = self.get_file_by_path(file_path)
        if not file or not file.is_file:
            raise ValueError("No file found using this file_name.")

        file.download(to_path=to_path)

    def delete_file(self, file_path: str):
        """
        Delete a file stored on OneDrive.

        Args:
            file_path (str): The path of the file in OneDrive.
                The file path must be used in the pattern: /path/to/file
        """
        file = self.get_file_by_path(file_path)
        if file:
            file.delete()

    def create_folder(self, folder_name: str, create_on_path: str = ''):
        """
        Create a folder on OneDrive.

        Args:
            folder_name (str): The name of the folder to be created.
            create_on_path (str): The path in OneDrive where the folder will be created.
                The path must be used in the pattern: /path/to/parent/folder. Defaults to root folder.

        Returns:
            DriveItem: The reference for the created folder.
        """
        parent_folder = self.default_drive.get_root_folder()
        if create_on_path:
            item = self.get_file_by_path(create_on_path)
            if item and item.is_folder:
                parent_folder = item

        return parent_folder.create_child_folder(folder_name)
