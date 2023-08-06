# -*- coding: utf-8 -*-
import sys
import os
import codecs
import typer
import paramiko
import json

from rich import print
from pathlib import Path
from typing import List
from eboot.gtest2html import gtest2html
from . import Configuration
from . import RootCMakelist
from . import utils


sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

app = typer.Typer()


@app.callback()
def callback():
    """
    TX1:        1     PX2:        2\n
    WINDOWS:    3     J6:         4\n
    LINUX_X86:  5     QNX:        6\n
    TDA4:       7     J3:         8\n
    J5:         10
    """


@app.command()
def config():
    hosts = {
        "j3": {
            "ip": "10.10.60.151",
            "port": 22,
            "username": "root",
            "password": "",
            "workspace": "/userdata/zlw/"
        },
        "mbk": {
            "ip": "10.211.55.3",
            "port": 22,
            "username": "ejian",
            "password": "9821",
            "workspace": "/home/ejian/Desktop/"
        }
    }
    config_path = os.path.join(os.path.dirname(sys.argv[0]), "eboot.config.json")
    if not os.path.isfile(config_path):
        open(config_path, "w", encoding='utf-8').write(json.dumps(hosts, indent=4))


@app.command()
def clear(all: bool = typer.Option(False, "--all", "-a")):
    file_list = [os.path.join(os.getcwd(), "build_out"), os.path.join(os.getcwd(), "CMakeLists.txt"), os.path.join(
        os.getcwd(), "script/config/env_config.ini")]

    if not all:
        utils.move("build_out/neo/system.xml", "./")
        utils.move("build_out/neo/globals.xml", "./")
        utils.move("build_out/neo/config.cfg", "./")

    for file in file_list:
        if os.path.exists(file):
            print("clear: " + file)
            utils.remove(file)

    if not all:
        utils.move("system.xml", "build_out/neo/")
        utils.move("globals.xml", "build_out/neo/")
        utils.move("config.cfg", "build_out/neo/")


@app.command()
def build(platform: str, option: str):
    Configuration.init(platform)
    RootCMakelist.Build(option)


@app.command()
def g2h(files: List[Path], output: Path):
    gtest2html.gtest2html(files, output)


@app.command()
def x2s(files: List[Path]):
    for file in files:
        if file.is_file():
            filedata = "\""
            output = os.path.join(os.path.dirname(
                os.path.abspath(file)), os.path.basename(file).split('.')[0] + ".inc")
            with open(file, "r", encoding="utf-8") as f:
                lines = f.readlines()
                for line in lines:
                    line = line.replace("\"", "\\\"")
                    filedata += (line[:-1] + "\\" + "\n")
            filedata += "\";"
            f.close()

            os.chdir(os.path.dirname(os.path.abspath(file)))
            if os.path.isfile(output):
                os.remove(output)
            with open(output, "w", encoding="utf-8") as f:
                f.write(filedata)
                f.close()


def push_files(self, src: str, dst: str):
    self.exec_command(f"rm -rf {dst}")
    self.exec_command(f"mkdir -p {dst}")
    sftp = self.open_sftp()
    if dst[:-1] != '/':
        dst += '/'

    if os.path.isfile(src):
        sftp.put(src, dst + os.path.basename(src))
        self.exec_command(f"chmod 777 {dst + os.path.basename(src)}")
    elif os.path.isdir(src):
        for file in os.listdir(src):
            filepath = os.path.join(src, file)
            if os.path.isfile(filepath):
                sftp.put(filepath, dst + file)
                self.exec_command(f"chmod 777 {dst + file}")
            else:
                push_files(self, filepath, dst + file)
    sftp.close()


@app.command()
def push(src: str, platform: str, dst=typer.Argument("")):
    src = os.path.abspath(os.path.realpath(src))

    data = json.loads(open(os.path.join(os.path.dirname(sys.argv[0]), "eboot.config.json"), "r").read())
    print(data[platform])

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(data[platform]['ip'], data[platform]['port'], data[platform]['username'], data[platform]['password'])

    push_files(ssh, src, os.path.join(data[platform]['workspace'], dst))
    ssh.close()


if __name__ == "__main__":
    app()
    # print(os.getcwd())
    # print(os.path.join(os.getcwd(), "eboot"))
