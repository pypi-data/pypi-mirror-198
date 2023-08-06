import os.path

from airpage.core import *

new_main_content = f"""__author__ = {os.getlogin()}
from airpage import *
env = GetEnviron(__file__)
''' ------------------------------------- '''
# Create your script here:
from page import *

"""
new_page_content = f"""from airpage import *
Page('shut', Not(IDENTITY))  # page when program is shutdown.
page('main', IDNETITY)  # main page.

''' ------------------ Page Definition End -------------------- '''
@transfer('shut', 'main')
def bootloader() -> bool:
    '''boot your program'''
    return True

"""

def NewProject(project_path:str):
    """
    新建airpage工程。
    :param project_path: 工程路径，可以是空的，也可以是已经刚刚由airtest创建的工程
    :return: bool 成功返回True，失败返回False
    """
    if project_path[-4:].lower() != '.air':
        error("TypeError", "Project path must be endwith '.air'")

    if os.path.exists(project_path):
        warn(f"Exists {project_path}, Failed to create.")
        return False
    else:
        ''' 不存在项目，可以开始快乐创建空项目了 '''
        os.makedirs(project_path)
        assert os.path.exists(project_path), f"Failed to create directory:{project_path}"

        # 创建主脚本
        fname = os.path.basename(project_path)
        if fname[-4:].lower() == '.air':
            fname = fname[:-4]
        with open(os.path.join(project_path, fname + '.py'), 'w') as f:
            f.write(new_main_content)

        # 创建page脚本
        with open(os.path.join(project_path, 'page.py'), 'w') as f:
            f.write(new_page_content)
        return True

def CMD_NewProject(*argv):
    return NewProject(*argv)

if __name__ == '__main__':
    _ = input("请输入项目路径(包含项目名，以.air结尾): ")
    if NewProject(_):
        print("Ok.")
    else:
        print("Failed")