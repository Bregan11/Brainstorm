# 1. Скачивание папки с помощью gdown
import gdown

url = 'https://drive.google.com/drive/folders/1kUYiSAafghhYR0ARyXwPW1HZPpHcFIag'
output = '/workspaces/Brainstorm/Загрузки'
gdown.download_folder(url, output=output, quiet=True)
