#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pyttsx3
import PyPDF2
import numpy as np
import cv2
import math
import playsound


# In[2]:


w1=5.0
d1=18.0
f=(200*d1)/w1
body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
ALLOWED_EXTENSIONS = {'pdf', 'txt'}


# In[3]:


import os
import urllib.request
from flask import Flask, request, redirect, url_for, render_template, send_from_directory,Response
from werkzeug.utils import secure_filename
from PyPDF2 import PdfFileReader, PdfFileWriter
from flask_cors import cross_origin

UPLOAD_FOLDER = 'static/uploads/'
DOWNLOAD_FOLDER = 'static/uploads/'

app = Flask(__name__, static_url_path="/static")
app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


# In[4]:


def speak(file):
    book=open(file,'rb')
    pdfReader=PyPDF2.PdfFileReader(book)
    pdfReader.getIsEncrypted()
    pages=pdfReader.numPages
    speaker=pyttsx3.init()
    for i in range(pages):
        page=pdfReader.getPage(i)
        text=page.extractText()
        speaker.say(text)
        speaker.runAndWait()


# In[5]:


def gen_frames(): 
    camera = cv2.VideoCapture(0)# generate frame by frame from camera
    while True:
        # Capture frame-by-frame
        success, frame = camera.read()  # read the camera frame
        if not success:
            break
        else:
            frame=cv2.flip(frame,1)
            gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            bodies = body_cascade.detectMultiScale(gray,1.3,5)
            for(x,y,w,h) in bodies:
                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
                p=math.sqrt(w**2+h**2)
                x=str(int((w1*f)/p))
                speakerx=pyttsx3.init()
                if int(x)<15:
                    cv2.putText(frame,"Warning",(0,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
                    speakerx.say("Warning")
                    speakerx.runAndWait()
                cv2.putText(frame,x,(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')  # concat frame one by one and show result


# In[6]:


def text_to_speech(text, gender):
    voice_dict = {'Male': 0, 'Female': 1}
    code = voice_dict[gender]

    engine = pyttsx3.init()

    # Setting up voice rate
    engine.setProperty('rate', 125)

    # Setting up volume level  between 0 and 1
    engine.setProperty('volume', 0.8)

    # Change voices: 0 for male and 1 for female
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[code].id)

    engine.say(text)
    engine.runAndWait()


# In[ ]:


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/static/audioLectures.html',methods=['GET', 'POST'])
def index_audio():
    if request.method == 'POST':
        if 'file' not in request.files:
            print('No file attached in request')
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            print('No file selected')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)
            return redirect(url_for('uploaded_file', filename=filename))
    return render_template('audioLectures.html')


def process_file(path, filename):
    speak(path)
    # with open(path, 'a') as f:
    #    f.write("\nAdded processed content")


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True) 
    

@app.route('/static/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen_frames(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/static/socialDistancing.html',methods=['GET', 'POST'])
def index_social():
    if request.method == 'GET':
        return redirect(url_for('video_feed'))
    """Video streaming home page."""
    return render_template('socialDistancing.html')

@app.route('/static/liveLectures.html',methods=['GET', 'POST'])
def index_live():
       return render_template('liveLectures.html')

    
@app.route('/static/summary.html',methods=['GET', 'POST'])
def index_summary():
    return render_template('summary.html')
    
@app.route('/static/text2speech.html',methods=['GET', 'POST'])
@cross_origin()
def index_text2speech():
    if request.method == 'POST':
        text = request.form['speech']
        gender = request.form['voices']
        text_to_speech(text, gender)
        return render_template('text2speech.html')
    else:
        return render_template('text2speech.html')
    
@app.route('/static/index1.html',methods=['GET', 'POST'])
def index_home():
       return render_template('index1.html')

if __name__ == '__main__':
    app.run()


# In[ ]:





# In[ ]:


