import os
from dataclasses import dataclass
from config_for_7z import *


@dataclass
class zip_file:
    file_name: str
    cmd: str = None


def _get_media_list(path: str, suffix: tuple):
    # return [i for i in os.listdir(path) if os.path.splitext(i)[-1]==f'.{suffix}']  # 获得包含suffix后缀的文件列表
    return [zip_file(os.path.join(path, i)) for i in os.listdir(path) if
            os.path.splitext(i)[-1].endswith(suffix)]  # 获得包含suffix后缀的文件列表
    
def _get_media_list_plus(path: str, suffix: tuple):
    a = os.walk(path)
    file_list = []
    for item in a:
        for i in item[-1]:
            if os.path.splitext(i)[-1].endswith(suffix):
                file_list.append(zip_file(os.path.join(item[0], i)))
    return file_list
    


def make_command(file, zipfile, pw):
    """

    :param file: 要打包的文件
    :param zipfile: zip结尾
    :return: 单个command
    """
    loc_7z = 路径7z  # 7zip开源压缩工具的可执行文件路径
    archive_command_str = f'{loc_7z} a "{zipfile}" -p{pw} "{file}"' if pw else f'{loc_7z} a "{zipfile}" "{file}"' # 编辑命令行
    return (archive_command_str)


def renaming(path):
    '''修改后缀'''
    name = os.path.splitext(path)
    newname = name[0] + ".7z"
    return newname


def command_complement(zip_file_list: list):
    for zip_file in zip_file_list:
        zip_file.cmd = make_command(zip_file.file_name, renaming(zip_file.file_name), 密码)


if __name__ == '__main__':
    # 配置文件已经移动到 config for 7z.py
    # 执行cmd
    if 子目录:
        media_list = _get_media_list_plus(path, 后缀)
    else:
        media_list = _get_media_list(path, 后缀)
    assert media_list, 'No Operation'
    command_complement(media_list)
    import subprocess

    for i in media_list:
        subprocess.call(i.cmd)
        if 删除文件:
            os.remove(i.file_name)
            print(f'已删除{i.file_name}')
