import os

def rename():
        """ Renaming files. """
        dir = os.listdir('/Users/Aniket/PycharmProjects/Udacity/prank')
        print(dir)
        current_dir = os.getcwd()
        os.chdir('/Users/Aniket/PycharmProjects/Udacity/prank')

        for file_name in dir:
            try:
                os.rename(file_name, file_name.translate('None', '0123456789'))
            except:
                print('file is having some problems')

