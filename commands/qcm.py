import os
import sys


def main(**kwargs):
    '''
    # Quick Commit
    Args:
        commit_msg - Use any commit message, include double quotes!

    Usage:
        qcm "My Commit Message"
    :return:
    '''
    commit_msg = kwargs.get('commit_msg')
    os.system("git add --all")
    os.system(f'git commit -m {commit_msg}')
    os.system('git push')


if __name__ == '__main__':
    # Change keys for more acceptable arguments
    keys = [
        'commit_msg'
    ]

    values = sys.argv[1:]
    kwargs = dict(zip(keys, values))
    main(**kwargs)
