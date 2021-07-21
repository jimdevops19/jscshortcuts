import os
import sys


def main(**kwargs):
    '''
    Opens grammarly.com in browser
    Args:
        None

    Usage:
        grm
    :return:
    '''
    os.system('start https://app.grammarly.com/')


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        ''
    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)