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

def check_or_create_upload_name(upload_name):
    final_upload_dir = os.path.join(const.YT_UPLOADS_DIR, upload_name)
    # I want to catch differently whether if the folder is created or not to log it out
    if not os.path.exists(final_upload_dir):
        os.makedirs(final_upload_dir, exist_ok=False)
        print(f'FOLDER CREATED ✔️ -> {final_upload_dir}')
    else:
        print(f'WORKING ON EXISTING FOLDER -> {final_upload_dir}')


def clean():
    os.system('cls') if os.name == 'nt' else os.system('clear')
