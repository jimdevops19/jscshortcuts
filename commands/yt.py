import os
import commands.yt_pkg.constants as const
import sys
from commands.utils import utils
from commands.yt_pkg.create_desc import CreateDesc
from commands.yt_pkg.create_workspace import CreateWorkspace


def main(**kwargs):
    '''
    Describe what this command does
    Args:
        action - The action that you want to complete
            Options:
                'open', 'create_desc',

    Usage:
        yt create_desc
    :return:
    '''
    options = ['open', 'create_desc']
    action = kwargs.get('action')
    utils.validate(action in options)

    if action == 'create_desc':
        utils.clean()
        print("""
                              _           _                 _                         _         _    _               
         _   _   ___   _   _ | |_  _   _ | |__    ___    __| |  ___  ___   ___  _ __ (_) _ __  | |_ (_)  ___   _ __  
        | | | | / _ \ | | | || __|| | | || '_ \  / _ \  / _` | / _ \/ __| / __|| '__|| || '_ \ | __|| | / _ \ | '_ \ 
        | |_| || (_) || |_| || |_ | |_| || |_) ||  __/ | (_| ||  __/\__ \| (__ | |   | || |_) || |_ | || (_) || | | |
         \__, | \___/  \__,_| \__| \__,_||_.__/  \___|  \__,_| \___||___/ \___||_|   |_|| .__/  \__||_| \___/ |_| |_|
         |___/                                                                          |_|                          


        """)
        upload_name = input('Upload folder: \n')
        utils.check_or_create(os.path.join(const.YT_UPLOADS_DIR, upload_name))
        CreateDesc().write_desc(upload_name)

    if action == 'open':
        utils.clean()
        print("""
                                              _           _                                       
             _   _   ___   _   _ | |_  _   _ | |__    ___    ___   _ __    ___  _ __  
            | | | | / _ \ | | | || __|| | | || '_ \  / _ \  / _ \ | '_ \  / _ \| '_ \ 
            | |_| || (_) || |_| || |_ | |_| || |_) ||  __/ | (_) || |_) ||  __/| | | |
             \__, | \___/  \__,_| \__| \__,_||_.__/  \___|  \___/ | .__/  \___||_| |_|
             |___/                                                |_|                 
        
                    
        """)
        upload_name = input('Upload folder: \n')
        CreateWorkspace(upload_name).create_all()


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        'action'
    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)