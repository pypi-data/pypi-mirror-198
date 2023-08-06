import subprocess
import os
import sys
import time
import oss2
import http.client
import json
import logging
import calendar
from pathlib import Path
import shutil
import zipfile
import platform
import requests

def updateBin(rootDir):
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

def ffmpegBinary():
    binDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    updateBin(binDir)
    if sys.platform == "win32":
        return os.path.join(binDir, "ffmpeg", "win", "ffmpeg.exe")
    elif sys.platform == "linux":
        machine = platform.machine().lower()
        return os.path.join(binDir, "ffmpeg", "linux", machine, "ffmpeg")
    elif sys.platform == "darwin":
        return os.path.join(binDir, "ffmpeg", "darwin", "ffmpeg")
    else:
        return ""
    
def ffmpegTest():
    binDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    testImage = os.path.join(binDir, "ffmpeg", "test.jpg")
    ffmpegProcess(f"-i {testImage}")
    
def ffmpegProcess(args):
    binary = ffmpegBinary()
    command = f'{binary} {args}'
    logging.info(f"ffmpegProcess: {command}")
    try:
        result = subprocess.run(command, stdout=subprocess.PIPE,
                                stderr=subprocess.PIPE, shell=True)
        if result.returncode == 0:
            logging.info(result.stdout.decode(encoding="utf8", errors="ignore"))
        else:
            logging.error("====================== ffmpeg error ======================")
            logging.error(result.stderr.decode(encoding="utf8", errors="ignore"))
            logging.error("======================     end      ======================")
    except subprocess.CalledProcessError as e:
        logging.error("====================== process error ======================")
        logging.error(e.output)
        logging.error("======================      end      ======================")

AccessKeyId = ""
AccessKeySecret = ""
SecurityToken = ""
BucketName = ""
Expiration = 0
Endpoint = ""
CallbackUrl = ""
cdn = ""
def upload(file):
    global AccessKeyId, AccessKeySecret, SecurityToken, BucketName, Expiration, Endpoint, CallbackUrl, cdn
    if calendar.timegm(time.gmtime()) > (Expiration + 30):
        conn = http.client.HTTPSConnection("mecord-beta.2tianxin.com")
        payload = json.dumps({
            "sign": "f033ab37c30201f73f142449d037028d"
        })
        headers = {
            'Content-Type': 'application/json'
        }
        conn.request("POST", "/proxymsg/get_oss_config", payload, headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode("utf-8"))
        if data["code"] == 0:
            AccessKeyId = data["data"]["AccessKeyId"]
            AccessKeySecret = data["data"]["AccessKeySecret"]
            SecurityToken = data["data"]["SecurityToken"]
            BucketName = data["data"]["BucketName"]
            Expiration = data["data"]["Expiration"]
            Endpoint = data["data"]["Endpoint"]
            CallbackUrl = data["data"]["CallbackUrl"]
            cdn = data["data"]["cdn"]
        else:
            logging.error(f"get_oss_config fail: response={data}")
    
    if len(AccessKeyId) <= 0:
        logging.error(f"get_oss_config error?")
        return
    
    auth = oss2.StsAuth(AccessKeyId, AccessKeySecret, SecurityToken)
    bucket = oss2.Bucket(auth, Endpoint, BucketName)
    with open(file, "rb") as f:
        byte_data = f.read()
    file_name = Path(file).name
    publish_name = f"mecord/crawler/{file_name}" 
    bucket.put_object(publish_name, byte_data)
    # domain = Endpoint.replace("http://", f"http://{BucketName}.").replace("https://", f"https://{BucketName}.")
    # return f"{domain}/{publish_name}"
    return f"{cdn}{publish_name}"