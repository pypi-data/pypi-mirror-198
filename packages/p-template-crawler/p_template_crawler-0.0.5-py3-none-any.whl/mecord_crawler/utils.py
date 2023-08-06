import uuid
import platform
import subprocess
import os
import sys
from io import BytesIO
import psutil
import pynvml
import time
import oss2
import http.client
import json
import logging
import calendar
from pathlib import Path
from PIL import Image
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer, SquareModuleDrawer, CircleModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask, SquareGradiantColorMask, SolidFillColorMask

def ffmpegBinary():
    binDir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "bin")
    if sys.platform == "win32":
        return os.path.join(binDir, "win", "ffmpeg.exe")
    elif sys.platform == "linux":
        return os.path.join(binDir, "linux", "ffmpeg")
    else:
        return ""
    
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