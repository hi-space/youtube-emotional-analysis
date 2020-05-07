import re


HANGUL = re.compile('[^ ㄱ-ㅣ가-힣]+')
ENGLISH = re.compile('[^-a-zA-Z]')
LETTERS = re.compile('[^-가-힣a-zA-Z0-9/ ]')


def is_hangul(s):
    result = HANGUL.sub('', s).strip()
    if len(result) == 0:
        return False
    return True

def refine_sentence(s):
    return LETTERS.sub('', s)
