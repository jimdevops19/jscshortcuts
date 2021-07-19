# General functions file
import os
import commands.yt_pkg.constants as const





def validate(expression):
    if expression:
        pass
    else:
        raise ValueError(
            f'Given expression could not be validated! \n'
            f'Please use a proper value'
        )

def check_or_create(folder_dir):
    '''
        A generic method to create directories,
        It also logs out if the folder was already created
    :param folder_dir:
    :return:
    '''

    # I want to catch differently whether if the folder is created or not to log it out
    if not os.path.exists(folder_dir):
        os.makedirs(folder_dir, exist_ok=False)
        print(f'FOLDER CREATED ✔️ -> {folder_dir}')
    else:
        print(f'WORKING ON EXISTING FOLDER -> {folder_dir}')


def clean():
    os.system('cls') if os.name == 'nt' else os.system('clear')