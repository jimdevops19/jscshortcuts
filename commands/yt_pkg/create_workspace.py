from commands.utils.utils import check_or_create
import commands.yt_pkg.constants as const
import shutil
import os


class CreateWorkspace:

    DIRS = [
        'powerpnts',
        'takes',
        'tut',
        'code',
        'icons',
        ''
        ''
    ]

    def __init__(self, upload_name):
        self.upload_name = upload_name
        self.__upload_path = self.__create_folder()
        self.actions = {}

    def __get_upload_path(self):
        return self.__upload_path

    def __create_folder(self):
        full_path = os.path.join(const.YT_UPLOADS_DIR, self.upload_name)
        check_or_create(full_path)
        return full_path

    def create_all(self):
        '''
        A method that will call everything that needs to be created,
            We don't want to hard coding the create_ prefixed methods
        :return:
        '''
        methods_str = [method_str for method_str in dir(self) if method_str.startswith('create_') and method_str != self.create_all.__name__]
        get_obj_reference = lambda method_str: getattr(self, method_str)
        methods_objects = list(map(get_obj_reference, methods_str))
        for method in methods_objects:
            method()

    def create_dirs(self):
        for folder_name in self.DIRS: # Maybe someone would like to customize dirs in instance level?
            final_path = os.path.join(self.__get_upload_path(), folder_name)
            check_or_create(final_path)

    def create_powerpnts(self):
        '''
        Copy the templated power point files
        :return:
        '''
        extension = 'pptx'
        # Create powerpnt directory in destination
        destination_powerpnts_path = os.path.join(self.__get_upload_path(), const.POWERPNTS)
        check_or_create(destination_powerpnts_path)

        # Get the powerpnt files from templates
        powerpnt_files_paths = [
            os.path.join(const.YT_POWERPNT_DIR, file)
            for file in os.listdir(const.YT_POWERPNT_DIR)
            if file.endswith(extension)
        ]

        # Copy source to destination
        for file_path in powerpnt_files_paths:
            base_path, file_name = os.path.split(file_path) # Splits to a tuple with base path and file name split
            if not os.path.exists(os.path.join(destination_powerpnts_path, file_name)):
                shutil.copy(src=file_path, dst=destination_powerpnts_path)
                print(f'📁 {file_name} COPIED  ✔️ -> {destination_powerpnts_path}')
            else:
                print(f'📁 ALREADY EXISTS   -> {os.path.join(destination_powerpnts_path, file_name)} ')