import sys
import os
import codecs
import shutil
import typer
import glob


def remove(src: str):
    src = os.path.abspath(os.path.realpath(src))
    if os.path.isfile(src):
        os.remove(src)
    elif os.path.isdir(src):
        shutil.rmtree(src)


def copy(src: str, dst: str):
    src = os.path.abspath(os.path.realpath(src))
    dst = os.path.abspath(os.path.realpath(dst))

    if not os.path.exists(dst):
        os.makedirs(dst)

    if os.path.isfile(src):
        shutil.copy(src, dst)
    elif os.path.isdir(src):
        for file in os.listdir(src):
            filepath = os.path.join(src, file)
            if os.path.isfile(filepath):
                shutil.copy(filepath, dst)
            else:
                copy(filepath, os.path.join(dst, file))


def move(src: str, dst: str):
    copy(src, dst)
    remove(src)
