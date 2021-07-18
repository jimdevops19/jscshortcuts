import dist
import os

commands_dir = os.path.join(os.curdir, 'commands')
for file in os.listdir(commands_dir):
    is_python_file = file.endswith('.py')
    if is_python_file:
        file_path = os.path.join(commands_dir, file)
        os.system(
            f'pyinstaller --onefile {file_path}'
        )

