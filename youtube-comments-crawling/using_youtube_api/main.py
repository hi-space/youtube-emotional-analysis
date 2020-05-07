from crawlling import *
from utils import * 

def start_crawlling(d, origin_key=None):
    for k, v in d.items():
        if isinstance(v, dict):
            start_crawlling(v, k)
        else:
            log(origin_key + " / " + k + " / " + v)
            crawlling_comments(origin_key, k, v)

def start_text_cleaning(directory_path):
    file_list = file_list_in_directory(directory_path)


if __name__ == "__main__":
    # start_crawlling(VIDEO_IDS)
    l = file_list_in_directory('''D:\\02-yscec\\2020-1\\DataVisualization\\final-term\\source_data\\show''')
    print(l)