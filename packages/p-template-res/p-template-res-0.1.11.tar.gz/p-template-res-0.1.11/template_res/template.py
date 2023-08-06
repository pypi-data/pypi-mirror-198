import zipfile
import platform
import subprocess
import json
import os
from pathlib import Path
import shutil
import stat
import requests
import hashlib

def getOssResource(rootDir, url, md5, name):
    localFile = os.path.join(rootDir, name)
    localFileIsRemote = False
    if os.path.exists(localFile):
        with open(localFile, 'rb') as fp:
                file_data = fp.read()
        file_md5 = hashlib.md5(file_data).hexdigest()
        if file_md5 == md5:
            localFileIsRemote = True

    if localFileIsRemote == False: #download
        if os.path.exists(localFile):
            os.remove(localFile)
        s = requests.session()
        s.keep_alive = False
        file = s.get(url, verify=False)
        with open(localFile, "wb") as c:
            c.write(file.content)
        s.close()
        
def updateNewTempalte(rootDir):
    getOssResource(rootDir, "http://mecord-m.2tianxin.com/res/template_res_2023032218.zip", "1b19e466c685c4d21362bf266b20988d", "template_res.zip.py")
    for root,dirs,files in os.walk(rootDir):
        for dir in dirs:
            shutil.rmtree(os.path.join(root, dir))

    for root,dirs,files in os.walk(rootDir):
        for file in files:
            name = file[0:file.index(".")]
            ext = file[file.index("."):]
            if ext == ".zip.py" and os.path.exists(os.path.join(root, name)) == False:
                with zipfile.ZipFile(os.path.join(root, file), "r") as zipf:
                    zipf.extractall(os.path.join(root, name))
                return
        if root != files:
            break
        
def templateDir(rootDir):
    for root,dirs,files in os.walk(rootDir):
        for dir in dirs:
            return os.path.join(root, dir)
        if root != files:
            break
    return ""

def savePut(src, dst, name):
    if name in src:
        dst[name] = src[name]

def inputConfig(data):
    videoCount = 0
    imageCount = 0
    audioCount = 0
    textCount = 0
    list = []
    otherParam = []
    for it in data:
        if it["type"].lower() == "image":
            imageCount += 1
            list.append({
                "type": "image",
                "width": it["width"],
                "height": it["height"]
            })
        elif it["type"].lower() == "video":
            videoCount += 1
            list.append({
                "type": "video",
                "width": it["width"],
                "height": it["height"]
            })
        elif it["type"].lower() == "audio":
            audioCount += 1
            list.append({
                "type": "audio"
            })
        elif it["type"].lower() == "text":
            textCount += 1
            list.append({
                "type": "text",
                "value": it["value"]
            })
        else:
            dd = {
                "type": it["type"],
                "name": it["name"]
                }
            savePut(it, dd, "minValue")
            savePut(it, dd, "maxValue")
            if "paramSettingInfo" in it:
                filterIndex = it["paramSettingInfo"][0]["filterIndex"]
                paramName = it["paramSettingInfo"][0]["paramName"]
                objName = it["paramSettingInfo"][0]["paramName"]
                valueType = it["paramSettingInfo"][0]["valueType"]
                dd["paramKey"] = f"{filterIndex}:{paramName}"
                dd["obj"] = objName
                dd["valueType"] = valueType
            otherParam.append(dd)
    return {
        "videoCount":videoCount,
        "imageCount":imageCount,
        "audioCount":audioCount,
        "textCount":textCount,
        "list":list,
        "otherParams":list
    }

def listTemplate():
    rootDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "res")
    updateNewTempalte(rootDir)
    tpDir = templateDir(rootDir)
    if len(tpDir) <= 0:
        print("template not found")
    result = []
    for root,dirs,files in os.walk(tpDir):
        for dir in dirs:
            projFile = os.path.join(root, dir, "template.proj")
            if os.path.exists(projFile) == False:
                for root,dirs,files in os.walk(os.path.join(root, dir)):
                    for file in files:
                        name, ext = os.path.splitext(file)
                        if ext == ".proj":
                            projFile = os.path.join(root, file)
            with open(projFile, 'r', encoding='utf-8') as f:
                projConfig = json.load(f)
            inputListPath = os.path.join(root, dir, "inputList.conf")
            if "inputList" in projConfig:
                inputListPath = os.path.join(root, dir, projConfig["inputList"])
            if "type" not in projConfig:
                continue
            if os.path.exists(inputListPath) == False:
                continue
            inputList = []
            with open(inputListPath, 'r', encoding='utf-8') as f:
                inputList = json.load(f)
            data = inputConfig(inputList)
            data["name"] = dir
            data["path"] = os.path.join(root, dir)
            result.append(data)
        if root != files:
            break
    print(json.dumps(result))
    return

import random
dstLst = [
    { "width": 100, "height": 100 },
    { "width": 100, "height": 200 },
    { "width": 200, "height": 100 },
    { "width": 50, "height": 200 },
    { "width": 200, "height": 50 }
]
srcLst = [
    { "width": 100, "height": 100 },
    { "width": 100, "height": 200 },
    { "width": 200, "height": 100 },
    { "width": 50, "height": 200 },
    { "width": 200, "height": 50 }
]
for i in range(0,100):
    src = srcLst[random.randint(0, 4)]
    dst = dstLst[random.randint(0, 4)]
    resInfowidth = src["width"]
    resInfoheight = src["height"]
    dstWidth = dst["width"]
    dstHeight = dst["height"]

    # resInfowidth = 512
    # resInfoheight = 512
    # dstWidth = 576
    # dstHeight = 1024
    floats = []
    scale = float(min(dstWidth, dstHeight)) / float(max(resInfowidth, resInfoheight))
    halfScale = scale / 2.0
    if float(dstWidth) / float(dstHeight) > float(resInfowidth) / float(resInfoheight):
        wscale = float(resInfowidth) / float(dstWidth)
        hscale = float(resInfoheight) / float(dstHeight)
        w = (float(dstWidth) / float(dstHeight) - float(resInfowidth) / float(resInfoheight)) / 2.0
        if scale > 0.5:
            floats.append(0.5 - halfScale)
        else:
            floats.append(0.5 + halfScale)
        floats.append(0.0)
        floats.append(float(dstHeight) / float(dstWidth))
        floats.append(1.0)
    else:
        wscale = float(resInfowidth) / float(dstWidth)
        hscale = float(resInfoheight) / float(dstHeight)
        y = (float(resInfowidth) / float(resInfoheight) - float(dstWidth) / float(dstHeight)) / 2.0
        floats.append(0)
        if scale < 0.5:
            floats.append(0.5 - halfScale)
        else:
            floats.append(0.5 + halfScale)
        floats.append(1.0)
        floats.append(float(dstWidth) / float(dstHeight))
    print(f"==== ({resInfowidth},{resInfoheight}) to ({dstWidth},{dstHeight})   scale={scale} value is [{floats[0]},{floats[1]},{floats[2]},{floats[3]}]")