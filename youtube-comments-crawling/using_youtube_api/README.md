# Youtube Comments Crawling

## 0. Setting

`config.py`

- `KEY`: Youtube Data API credential key
- `STORE_FILE_PATH`: Locate crawlled files to be saved 
- `PREPROCESSING_PATH`: Locate cleaned files to be saved
- `LOG_FILE`: Path to save log file
- `VIDEO_IDS`: List of youtube video id to crawl

## 1. Crawlling 

Run a `start_crawlling(d)` function in `main.py`

- `config.py` 의 `VIDEO_IDS` dictionary를 param으로 넣어주면 해당 링크의 댓글들을 최대 20100개까지 연속적으로 크롤링 한다.
- 크롤링 된 데이터는 `STORE_FILE_PATH` 에 `${singer}_${title}.csv` 로 저장된다.
- 댓글 작성자, 댓글 내용, like 수, 작성일자, 한글여부 데이터를 포함하고 있다.
    - 한글여부: 한글이 한글자라도 들어가 있으면 True, 그 외의 문자들은 False
  
## 2. Text Cleaning

`start_text_cleaning(directory_path)` function in `main.py`

- 한글과 영어를 대상으로 분석하기 때문에 그 외의 문자들을 제거해주기 위함
- 작업할 데이터가 있는 폴더의 path를 param으로 주면 해당 폴더 내의 `.csv` 파일들을 모두 읽어 처리한 후 `PREPROCESSING_PATH`에 저장
- 한글, 영어, 숫자를 제거한 모든 문자들을 제거하여 댓글 내용을 정제
- 한글, 영어, 숫자가 하나도 속해있지 않은 데이터는 삭제
- 즉, 이 작업을 마치고 나면 hangul field에 한글인 데이터는 True, 영어인 데이터는 False로 처리된다.

> [우려되는 corner case]   
> - 유튜브의 댓글들은 이모티콘으로 표현되는 경우가 많아 이런 데이터를 무의미하게 날려도 되는가?
> - 제대로 된 문법으로 작성되지 않은 댓글이 많다
> - 한 작성자가 여러번에 끊어서 댓글을 작성하는 경우도 있음. 연속적인 댓글들을 그냥 이어붙이기에는, 글자들로 모양을 만드는 경우들도 있다.

## 3. 형태소 추출 (한글/영어)

## 4. 단어 카운트