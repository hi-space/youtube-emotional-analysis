# Youtube-Comments-Crawler

Python scripts for crawling youtube comments.

## 1. using Seleniums

After loading a youtube page, it is automatically scrolled to load comments continuously. but if there are too many comments, it may not all be loaded.

### Run

1. Download the `chromedriver.exe` and then set `CHROME_DRIVER_PATH`.
2. Set the path to save the crawled files in `STORE_FILE_PATH`

## 2. using Youtube Data API

In order to access the YouTube Data API, you need to have a project on Google Cloud Platform and get a API key of Youtube Data API.

```sh
GET https://www.googleapis.com/youtube/v3/commentThreads
```

Comments are loaded using this http request. For paging, it is necessary to continuously receive the `nextToken`.

### Run

1. Set the credentials key in `KEY` to access the API
2. Set the path to save the crawled files in `STORE_FILE_PATH`
3. `author`, `contents`, `likeCount`, `date` of comment are saved.

# Links

- [Google Cloud Console](https://console.developers.google.com/projectselector2/apis/dashboard)
- [Youtube Data API](https://developers.google.com/youtube/v3/docs/commentThreads/list)