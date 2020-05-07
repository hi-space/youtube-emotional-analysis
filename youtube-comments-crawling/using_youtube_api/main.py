from crawlling import *


def start_job(d, origin_key=None):
    for k, v in d.items():
        if isinstance(v, dict):
            start_job(v, k)
        else:
            log(origin_key + " / " + k + " / " + v)
            crawlling_comments(origin_key, k, v)


if __name__ == "__main__":
    start_job(VIDEO_IDS)
