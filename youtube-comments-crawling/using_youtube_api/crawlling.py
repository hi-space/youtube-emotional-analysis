import requests
import csv
import time

from config import *
from text_cleaning import is_hangul
from utils import *


MAX_RETRY = 3


def get_comment_description(item):
    i = item['snippet']['topLevelComment']['snippet']
    return i['authorDisplayName'], i['textOriginal'], i['likeCount'], i['publishedAt']

def get_comments(params):
    time.sleep(2)
    res = requests.get('https://www.googleapis.com/youtube/v3/commentThreads', params=params, timeout=100)

    if res.status_code == 200:
        json_data = res.json()
        items = json_data.get("items")
        nextPageToken = json_data.get("nextPageToken")

        return items, nextPageToken
    else:
        log(res.text)
        return None, None

def crawlling_comments(singer, title, video_id):
    file = open(STORE_FILE_PATH + singer + '-' + title + '.csv', mode='w', encoding='utf-8-sig', newline='')
    csv_writer = csv.writer(file)
    csv_writer.writerow(['author', 'contents', 'likeCount', 'date', 'hangul'])
    
    params = {
        'part' : 'snippet',
        'maxResults' : '100',
        'videoId' : video_id,
        'key' : KEY
    }

    cnt = retry = 0
    while True:
        if cnt > 20000:
            break

        items, token = get_comments(params)

        while items == None and retry < MAX_RETRY:
            retry += 1
            items, token = get_comments(params)
        retry = 0

        if items == None:
            break
        
        cnt += len(items)

        for item in items:
            author, content, likeCount, date = get_comment_description(item)
            csv_writer.writerow([author, content, likeCount, date, is_hangul(content)])
    
        if token != None:
            params["pageToken"] = token
        else:
            break
    
    log("all comments: " + str(cnt) + "\n")
    file.close()
