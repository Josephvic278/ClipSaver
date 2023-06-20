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
                
                video = yt.streams.filter(progressive=True)
                audio = yt.streams.filter(adaptive=True)
                video = {f.itag:{"title":f.title, "file_type":f.type,'file_extension':f.subtype, 'res':f.resolution, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in video}
                audio= {f.itag:{"title":f.title, "file_type":f.type+' (No Audio)' if not f.abr else f.type+' (No Video)','bitrate':f.abr, 'file_extension':f.subtype, "filesize":get_size_format(f.filesize), 'download_link':f.url} for f in audio}
                session['audio'] = audio
                session['video'] =video
                session['status']='success'
                print(session['status'])
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

@app.route('/download_yt_list')

@app.route('/result')
def result():
    if session.get('status',None) == 'success':
        audio,video = session.get('audio', None), session.get('video', None)
        return render_template('result.html', data={'audio':audio, 'video':video})
    elif session.get('status',None) == 'error':
        LSerr=session.get('error')
        return render_template('result.html', data={'error':LSerr})
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
