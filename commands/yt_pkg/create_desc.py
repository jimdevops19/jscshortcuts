import commands.yt_pkg.constants as const
import os
from string import Template


class CreateDesc:
    def __init__(self,):
        '''
            Build the new description as expected

            Templated args:
                - hashtag1
                - hashtag2
                - hashtag3
                - short_description
                - desc_link_list
                - timeline_list

        :param kwargs:
        '''
        self.hashtag1 = input('hashtag1: \n')
        self.hashtag2 = input('hashtag2: \n')
        self.hashtag3 = input('hashtag3: \n')
        self.short_description = input('Short Description: \n')
        self.desc_link_list = input('Description Link List: \n')
        self.timeline_list = input('Timeline List: \n')

    def template_file(
            self,
            file_path=os.path.join(
                const.YT_TEMPLATES_DIR, const.DESCRIPTION_FILE
            )
    ):
        with open(file_path, 'r', encoding='utf-8') as f:
            src = Template(f.read())
            result = src.substitute(self.__dict__)

        # We are allowed to access here result, after context mgr
        return result


    def write_desc(self, upload_name):
        '''
            Write the templated description to the given file path
        :param dest:
        :return:
        '''
        templated_text = self.template_file()
        final_destination = os.path.join(const.YT_UPLOADS_DIR, upload_name, const.DESCRIPTION_FILE)
        with open(final_destination, 'w', encoding="utf-8") as f:
            f.write(templated_text)
            print(f'FILE CREATED AND TEXT WRITTEN ✔️ -> {final_destination}')
