import re
import pandas as pd
from utils import log


HANGUL = re.compile('[^ ㄱ-ㅣ가-힣]+')
ENGLISH = re.compile('[^-a-zA-Z]')
LETTERS = re.compile('[^-가-힣a-zA-Z0-9/ ]')


def is_hangul(s):
    result = HANGUL.sub('', str(s)).strip()
    if len(result) == 0:
        return False
    return True

def is_english(s):
    result = ENGLISH.sub('', str(s)).strip()
    if len(result) == 0:
        return False
    return True

def refine_sentence(s):
    return LETTERS.sub('', str(s))

def refine_file(source_path, output_path, file):
    try:
        df = pd.read_csv(source_path + file)
    except Exception:
        log("Exception during reading file - " + source_path + file)

    # remove letters without hangul or english
    for idx, row in df.iterrows():
        s = refine_sentence(row.contents)

        if len(s.strip()) != 0:
            df.at[idx, 'contents'] = s
        else:
            df.drop(idx, inplace=True)
    
    # save refined file
    df.to_csv(output_path + file,
                sep=',',
                columns=['author', 'contents', 'likeCount', 'date', 'hangul'],
                encoding='utf-8-sig')

