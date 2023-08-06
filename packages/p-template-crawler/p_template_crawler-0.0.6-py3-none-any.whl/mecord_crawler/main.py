import sys
import os
import time
import requests
import json
from mecord_crawler import utils
import logging
import urllib3
import datetime

rootDir = ""
curGroupId = 0

def publish(media_type, post_text, ossurl):
    type = 0
    if media_type == "video":
        type = 2
    elif media_type == "image":
        type = 1
    elif media_type == "audio":
        type = 3
    param = {
        "task_id": curGroupId,
        "content": ossurl,
        "content_type": type,
        "info": post_text
    }
    s = requests.session()
    s.keep_alive = False
    res = s.post("https://beta.2tianxin.com/common/admin/mecord/add_crawler_post", json.dumps(param), verify=False)
    resContext = res.content.decode(encoding="utf8", errors="ignore")
    logging.info(f"publish res:{resContext}")
    s.close()

def download(name, media_type, post_text, media_resource_url, audio_resource_url):
    ext = ".mp4"
    if media_type == "image":
        ext = ".jpg"
    elif media_type == "audio":
        ext = ".mp3"
    savePath = os.path.join(rootDir, f"{name}{ext}")
    if os.path.exists(savePath):
        os.remove(savePath)

    logging.info(f"download: {media_resource_url}, {audio_resource_url}")
    s = requests.session()
    s.keep_alive = False
    file = s.get(media_resource_url, verify=False)
    with open(savePath, "wb") as c:
        c.write(file.content)
    
    if len(audio_resource_url) > 0:
        audioPath = os.path.join(rootDir, f"{name}.mp3")
        file1 = s.get(audio_resource_url)
        with open(audioPath, "wb") as c:
            c.write(file1.content)
        tmpPath = os.path.join(rootDir, f"{name}.mp4.mp4")
        utils.ffmpegProcess(f"-i {savePath} -i {audioPath} -vcodec copy -acodec copy -y {tmpPath}")
        if os.path.exists(tmpPath):
            os.remove(savePath)
            os.rename(tmpPath, savePath)
            os.remove(audioPath)
        logging.info(f"merge => {file}, {file1}")
    ossurl = utils.upload(savePath)
    logging.info(f"upload success, url = {ossurl}")
    s.close()
    os.remove(savePath)
    publish(media_type, post_text, ossurl)
    
def processPosts(uuid, data):
    post_text = data["text"]
    medias = data["medias"]
    idx = 0
    for it in medias:
        media_type = it["media_type"]
        media_resource_url = it["resource_url"]
        audio_resource_url = ""
        if "formats" in it:
            formats = it["formats"]
            quelity = 0
            for format in formats:
                if format["quality"] > quelity and format["quality"] <= 1080:
                    quelity = format["quality"]
                    media_resource_url = format["video_url"]
                    audio_resource_url = format["audio_url"]
        download(f"{uuid}_{idx}", media_type, post_text, media_resource_url, audio_resource_url)
        idx += 1

def aaaapp(groupId, url, cursor, page):
    param = {
        "userId": "D042DA67F104FCB9D61B23DD14B27410",
        "secretKey": "b6c8524557c67f47b5982304d4e0bb85",
        "url": url,
        "cursor": cursor,
    }
    isSingle = False
    requestUrl = "https://h.aaaapp.cn/posts"
    if "youtube.com/watch" in url or "youtube.com/shorts" in url or "instagram.com/p/" in url or "tiktok.com/t/" in url or "douyin.com/video" in url or "/video/" in url:
        isSingle = True
    if isSingle:
        requestUrl = "https://h.aaaapp.cn/single_post"
    logging.info(f"=== request: {requestUrl} cursor={cursor}")
    s = requests.session()
    s.keep_alive = False
    res = s.post(requestUrl, params=param, verify=False)
    logging.info(f"=== res: {res.content}")
    if len(res.content) > 0:
        data = json.loads(res.content)
        if data["code"] == 200:
            idx = 0
            if isSingle:
                processPosts(f"{curGroupId}_{page}_{idx}", data["data"])
            else:
                posts = data["data"]["posts"]
                for it in posts:
                    processPosts(f"{curGroupId}_{page}_{idx}", it)
                    idx+=1
            if "next_cursor" in data and len(data["next_cursor"]) > 0:
                aaaapp(groupId, url, data["next_cursor"])
    s.close()

def main():
    global rootDir
    global curGroupId

    if len(sys.argv) < 2:
        return
    rootDir = sys.argv[1]
    if os.path.exists(rootDir) == False:
        print(f"path {rootDir} is not exist")
        return

    urllib3.disable_warnings()
    d = datetime.datetime.now().strftime('%Y_%m_%d_%H_%M_%S')
    thisFileDir = os.path.dirname(os.path.abspath(__file__))
    logging.basicConfig(filename=f"{thisFileDir}/mecord_crawler_{d}.log", 
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        encoding="utf-8",
                        level=logging.DEBUG)
    while(1):
        try:
            s = requests.session()
            s.keep_alive = False
            res = s.get("https://beta.2tianxin.com/common/admin/mecord/get_task", verify=False)
            s.close()
            if len(res.content) > 0:
                data = json.loads(res.content)
                curGroupId = data["id"]
                logging.info(f"================ begin {curGroupId} ===================")
                logging.info(f"========== GetTask: {res.content}")
                link_url_list = data["link_url_list"]
                for s in link_url_list:
                    aaaapp(id, s, "", 0)
                print(f"complate => {curGroupId}")
                logging.info(f"================ end {curGroupId} ===================")
        except Exception as e:
            logging.error("====================== uncatch Exception ======================")
            logging.error(e)
            logging.error("======================      end      ======================")
        time.sleep(10)
        
if __name__ == '__main__':
        main()
