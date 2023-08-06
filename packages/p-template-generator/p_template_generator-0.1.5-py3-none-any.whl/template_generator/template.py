import sys
import os
import subprocess
import json
import random
from pathlib import Path
import shutil
import zipfile
import stat
from template_generator import binary

def linuxBinary(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for dir in dirs:
            if "linux" in dir:
                binaryFile = os.path.join(root, dir, "TemplateProcess.out")
                print("=================== chmod 755 TemplateProcess.out ==================")
                cmd = subprocess.Popen(f"chmod 755 {binaryFile}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                while cmd.poll() is None:
                    print(cmd.stdout.readline().rstrip())
                print("===================             end              ==================")
                return binaryFile
        if root != files:
            break
    return ""

def linuxEnvCheck(rootDir):
    if os.path.exists("/usr/lib/libskycore.so") == False:
        for root,dirs,files in os.walk(rootDir):
            for dir in dirs:
                if "linux" in dir:
                    shCommand = os.path.join(root, dir, "setup.sh")
                    print("=================== begin Initialize environment ==================")
                    cmd = subprocess.Popen(f"sh {shCommand}", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
                    while cmd.poll() is None:
                        print(cmd.stdout.readline().rstrip())
                    print("===================             end              ==================")
            if root != files:
                break
    return os.path.exists("/usr/lib/libskycore.so")

def getBinary(rootDir):
    binary = ""
    if sys.platform == "win32":
        binary = winBinary(rootDir)
    elif sys.platform == "linux":
        binary = linuxBinary(rootDir)
        if linuxEnvCheck(rootDir) == False:
            print("linux environment error")
    return binary

def winBinary(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for dir in dirs:
            if "win" in dir:
                return os.path.join(root, dir, "TemplateProcess.exe")
        if root != files:
            break
    return ""

def executeTemplate(inputFiles, template_path, params, output_path):
    rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    binary.updateBin(rootDir)
    binaryPath = getBinary(rootDir)
    if len(binaryPath) <= 0:
        print("binary not found")
        return

    inputArgs = os.path.join(os.path.dirname(os.path.abspath(__file__)), f"{random.randint(100,99999999)}.in")
    if os.path.exists(inputArgs):
        os.remove(inputArgs)
    with open(inputArgs, 'w') as f:
        json.dump({
            "input": inputFiles,
            "template": template_path,
            "params": params,
            "output": output_path
        }, f)
        
    command = f'{binaryPath} --config {inputArgs}'
    print(f"=== executeTemplate => {command}")
    cmd = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    while cmd.poll() is None:
        print(cmd.stdout.readline().rstrip())

def runCommand(args):
    rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    binary = getBinary(rootDir)
    if len(binary) <= 0:
        print("binary not found")
        return
    
    command = f'{binary} --exec {args}'
    print(f"=== runCommand => {command}")
    try:
        cmd = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        while cmd.poll() is None:
            print(cmd.stdout.decode(encoding="utf8", errors="ignore"))
    except subprocess.CalledProcessError as e:
        print("====================== process error ======================")
        print(e)
        print("======================      end      ======================")
