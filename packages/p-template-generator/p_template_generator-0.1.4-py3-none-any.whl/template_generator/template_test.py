import sys
import os
import subprocess
import json
import shutil
import zipfile
from template_generator import template

def updateRes(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for file in files:
            if file.find(".") <= 0:
                continue
            name = file[0:file.index(".")]
            ext = file[file.index("."):]
            if ext == ".zip.py" and os.path.exists(os.path.join(root, name)) == False:
                for dir in dirs:
                    shutil.rmtree(os.path.join(root, dir))
                with zipfile.ZipFile(os.path.join(root, file), "r") as zipf:
                    zipf.extractall(os.path.join(root, name))
                return
        if root != files:
            break

def test():
    rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "test")
    updateRes(rootDir)
    config = {
        "input":[
            f"{rootDir}/res/1.png",
            f"{rootDir}/res/2.png",
            f"{rootDir}/res/3.png",
            f"{rootDir}/res/4.png"
            ],
        "template":f"{rootDir}/res/GreenAlbum_9-16",
        "params":{},
        "output":f"{rootDir}/res/out.mp4"
        }
    with open(os.path.join(rootDir, "res", "param.config"), 'w') as f:
        json.dump(config, f)

    binary = ""
    if sys.platform == "win32":
        binary = template.winBinary(rootDir)
    elif sys.platform == "linux":
        binary = template.linuxBinary(rootDir)
        if linuxEnvCheck(rootDir) == False:
            print("linux environment error")
    if len(binary) <= 0:
        print("binary not found")
        return
        
    command = f'{binary} {os.path.join(rootDir, "res", "param.config")}'
    cmd = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while cmd.poll() is None:
        print(cmd.stdout.readline().rstrip())

