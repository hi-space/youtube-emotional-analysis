from crawlling import *
from text_cleaning import *
from utils import * 
from config import *


def start_crawlling(d, origin_key=None):
    for k, v in d.items():
        if isinstance(v, dict):
            start_crawlling(v, k)
        else:
            log(origin_key + " / " + k + " / " + v)
            crawlling_comments(origin_key, k, v)

def start_text_cleaning(directory_path=STORE_FILE_PATH):
    file_list = file_list_in_directory(directory_path)
    for file in file_list:
        log('cleaning - ' + file)
        refine_file(directory_path, PREPROCESSING_PATH, file)

if __name__ == "__main__":
    # start_crawlling(VIDEO_IDS)
    
    start_text_cleaning('D:\\02-yscec\\2020-1\\DataVisualization\\final-term\\source_data\\interview\\')
    