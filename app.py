from flask import Flask, request, jsonify, url_for, redirect, session, render_template
import pytube, requests, secrets

from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask('ClipSaver')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']=secrets.token_hex(20)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
migrate = Migrate(app, db)
Session(app)





# ROUTES
@app.route('/')
def index():
    return render_template("main.html")

@app.route('/download_yt', methods=['POST', 'GET'])
def download_yt():
    if request.method=='POST':
        link = request.form.get('link', False)
        link = is_yt(link)
        print(link)
        if link:
            yt = pytube.YouTube(link)
            print(session.items())
            video = yt.streams.filter(progressive=True, file_extension="mp4")
            audio = yt.streams.filter(only_audio=True)
            video = {f.itag:{"title":f.title, "file_type":f.type,'file_extension':f.subtype, 'res':f.resolution, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in video}
            audio= {f.itag:{"title":f.title, "file_type":f.type,'bitrate':f.abr, 'file_extension':f.subtype, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in audio}
            session['audio'] = audio
            session['video'] =video
            session['status']=True
            print(session.items())
            return redirect(url_for('result'))
        else:
            session['status'] =  False
            return jsonify({'message':'Invalid request'})
    print(session.items())
    return render_template("home.html")
    
@app.route('/result')
def result():
    if session.get('status',None):
        audio,video = session.get('audio', None), session.get('video', None)
        session.clear()
        return render_template('result.html', data={'audio':audio, 'video':video})
    else:
        return render_template('result.html', data=None)
        
    


# UTILITY FUNCTIONS
def is_yt(link):
    thumb=f'img.youtube.com/vi/[VideoID]/maxresdefault.jpg'
    if link:
        try:
            link = requests.get(link).url
            return link if 'youtu' in link or link.lower().startswith('youtu') else False
        except:
            return False
    return False

def get_size_format(number, factor=1024, suffix="B"):
    """
    Converts arbitrary numbers to human readable size formats
    e.g:
        1234226 => '1.18MB'
        1246622552 => '1.16GB'
    """
    for unit in ["", "K", "M", "G", "T", "P", "E", "Z"]:
        if number < factor:
            return f"{number:.2f}{unit}{suffix}"
        number /= factor
    return f"{number:.2f}Y{suffix}"


if __name__ == '__main__':
    app.run(debug=True)
