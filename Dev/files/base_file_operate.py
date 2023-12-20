#!python3
# -*- coding: utf-8 -*-

"""
base_file_operate.py

文件的基础操作。

该模块包含以下功能：
1. 取得路径filepath下的所有文件名(不包括子目录下的文件)
2. 取得路径filepath下的所有文件名(包括子目录下的文件)

Author: niu0217
Date: 2023-12-20
"""

import os


def get_filename(folder):
    """
    取得路径filepath下的所有文件名(不包括子目录下的文件)

    Args:
        folder (str): 想要查找的文件路径

    Returns:
        list: 保存了当前路径下的所有文件名字
    """

    filenames_list = []
    for filename in os.listdir(folder):
        filenames_list.append(filename)

    return filenames_list


def get_filename_recursion(filepath):
    """
    取得路径filepath下的所有文件名(包括子目录下的文件)

    Args:
        filepath (str): 想要查找的文件路径

    Returns:
        list: 保存了当前路径下的所有文件名字
    """

    filenames_list = []
    for foldername, subdfolders, filenames in os.walk(filepath):
        for filename in filenames:
            filenames_list.append(filename)

    return filenames_list


if __name__ == '__main__':
    result_list = get_filename_recursion('/Users/niu0217/niuGithub/Documents')
    print(result_list)
