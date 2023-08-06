import sys
import os
import subprocess
import json
import random
from pathlib import Path
import shutil
import zipfile
import stat
import requests

def getOssResource(rootDir, url, name):
    ffmpeg_url = "https://m-beta-yesdesktop.2tianxin.com/mecord/crawler/ffmpeg.zip"
    fileName = "ffmpeg.zip.py"
    if os.path.exists(os.path.join(rootDir, fileName)) == False:
        savePath = os.path.join(rootDir, fileName)
        s = requests.session()
        s.keep_alive = False
        file = s.get(ffmpeg_url, verify=False)
        with open(savePath, "wb") as c:
            c.write(file.content)
        s.close()

def updateBin(rootDir):
    getOssResource(rootDir, "https://m-beta-yesdesktop.2tianxin.com/mecord/crawler/ffmpeg.zip", "ffmpeg.zip.py")
    getOssResource(rootDir, "https://m-beta-yesdesktop.2tianxin.com/res/skymedia.zip", "skymedia.zip.py")
    for root,dirs,files in os.walk(rootDir):
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))
        for file in files:
            if file.find(".") <= 0:
                continue
            name = file[0:file.index(".")]
            ext = file[file.index("."):]
            if ext == ".zip.py" and os.path.exists(os.path.join(root, name)) == False:
                with zipfile.ZipFile(os.path.join(root, file), "r") as zipf:
                    zipf.extractall(os.path.join(root, name))
                return
        if root != files:
            break