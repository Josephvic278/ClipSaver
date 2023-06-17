from flask import Flask, request, jsonify, url_for, redirect, session
import pytube, requests, secrets

from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('ClipSaver')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config['SECRET_KEY']=secrets.token_hex(20)

db = SQLAlchemy(app)
migrate = Migrate(app, db)



# ROUTES
@app.route('/')
def index():
    return "<h1> Hello </h1>"

@app.route('/download_yt', methods=['POST', 'GET'])
def download_yt():
    if request.method=='POST':
        data=request.get_json()
        link = data.get('link',False)
        link = is_yt(link)
        if link:
            yt = pytube.YouTube(link)
            
            mp4files = yt.streams.filter(progressive=True, file_extension="mp4")
            mp4files = {f.itag:{"title":f.title, "file_type":f.type,'file_extension':f.subtype, 'res':f.resolution, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in mp4files}
            audio = yt.streams.filter(only_audio=True)
            audio= {f.itag:{"title":f.title, "file_type":f.type,'bitrate':f.abr, 'file_extension':f.subtype, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in audio}
            return jsonify({'audio':audio, 'video':mp4files})
        else:
            return jsonify({'message':'Invalid request'})
    return "<h1>Download</h1> <a href=' download' target='_blank'>Download</a>"
    



# UTILITY FUNCTIONS
def is_yt(link):
    thumb=f'img.youtube.com/vi/[VideoID]/maxresdefault.jpg'
    link = requests.get(link).url
    if 'youtu' in link or link.lower().startswith('youtu'):
        return link
    return False

def get_size_format(b, factor=1024, suffix="B"):
    """
    Scale bytes to its proper byte format
    e.g:
        1253656 => '1.20MB'
        1253656678 => '1.17GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if b < factor:
            return f"{b:.2f}{unit}{suffix}"
        b /= factor
    return f"{b:.2f}Y{suffix}"

if __name__ == '__main__':
    app.run(debug=True)
