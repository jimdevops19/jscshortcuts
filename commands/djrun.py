import os
import sys


def main(**kwargs):
    '''
    A command to execute python manage.py runserver,
    Args:
        port - specify the port to execute the django server on,
            if not specified, 8000 will be used

    Usage:
        djrun 8000
    :return:
    '''

    port = kwargs.get('port') or 8000
    os.system(f'python manage.py runserver 127.0.0.1:{port}')


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        'port',

    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)
