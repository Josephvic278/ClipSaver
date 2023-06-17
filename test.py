import requests

url = 'http://127.0.0.1:5000/'
r = requests.post(url+'download_yt', json={'link':'https://www.youtube.com/watch?v=O0HQnTJhr70'})
print(r.text)