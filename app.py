import json
from flask import Flask, request, jsonify, url_for, redirect, session, render_template
import pytube, requests, secrets

# from flask_migrate import Migrate
# from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


app = Flask('ClipSaver')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY']=secrets.token_hex(20)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SESSION_SQLALCHEMY'] = db
# migrate = Migrate(app, db)
# Session(app)




# ROUTES
@app.route('/')
def index():
    return render_template("main.html")

@app.route('/download_yt', methods=['POST', 'GET'])
def download_yt():
    if request.method=='POST':
        link = request.form.get('link', False)
        link = is_yt(link)

        if link:
            try:
                yt = pytube.YouTube(link)
                thumb = yt.thumbnail_url
                title = yt.title
                length = format_seconds(yt.length)
                
                video = yt.streams.filter(progressive=True)
                audio = yt.streams.filter(adaptive=True)
                video = {f.itag:{"title":f.title, 'id':f.itag, "file_type":f.type,'file_extension':f.subtype, 'res':f.resolution, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in video}
                audio= {a.itag:{"title":a.title,  'id':a.itag, "file_type":a.type+' (No Audio)' if not a.abr else a.type+' (No Video)','bitrate':a.abr, 'file_extension':a.subtype, "filesize":get_size_format(a.filesize), 'download_link':a.url} for a in audio}
                meta = {'thumb':thumb, 'length':length, 'title':title}
                with open('static/json/meta.json','w') as f:
                    f.write(json.dumps(meta, indent=1))
                with open('static/json/audio.json','w') as f:
                    f.write(json.dumps(audio, indent=1))
                with open('static/json/video.json','w') as f:
                    f.write(json.dumps(video,indent=1))
                session['status']='success'
    
                return redirect(url_for('result'))
            except pytube.exceptions.LiveStreamError as LSerr:
                print(LSerr)
                session['status'] = 'error'
                LSerr=" ".join(str(LSerr).split()[1:])
                LSerr = 'This '+LSerr
                session['error'] = LSerr
                return redirect(url_for('result'))
        else:
            session['status'] =  False
            return jsonify({'message':'Invalid request'})
    return render_template("home.html")


@app.route('/result')
def result():
    print(session.get('status'))
    if session.get('status',None) == 'success':
        with open('static/json/audio.json') as f:
            audio=json.loads(f.read())
        with open('static/json/video.json') as f:
            video=json.loads(f.read())
        with open('static/json/meta.json') as f:
            meta=json.loads(f.read())
        return render_template('result.html', data={'audio':audio, 'video':video, 'meta':meta})
    elif session.get('status',None) == 'error':
        LSerr=session.get('error')
        return render_template('result.html', data={'error':LSerr})
    else:
        return redirect(url_for('download_yt'))


# UTILITY FUNCTIONS
def is_yt(link):
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

def format_seconds(seconds):
    if isinstance(seconds, int) and seconds >= 0:
        # calculate the hours, minutes and seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = (seconds % 3600) % 60
        # format the output with leading zeros
        return f"{hours:02d}:{minutes:02d}:{seconds:02d}"
    else:
        # return an error message for invalid input
        return '00:00:00'



if __name__ == '__main__':
    app.run(debug=True)
