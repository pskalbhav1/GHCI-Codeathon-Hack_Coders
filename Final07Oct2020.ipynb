{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pyttsx3\n",
    "import PyPDF2\n",
    "import numpy as np\n",
    "import cv2\n",
    "import math\n",
    "import playsound"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "w1=5.0\n",
    "d1=18.0\n",
    "f=(200*d1)/w1\n",
    "body_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')\n",
    "ALLOWED_EXTENSIONS = {'pdf', 'txt'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "import os\n",
    "import urllib.request\n",
    "from flask import Flask, request, redirect, url_for, render_template, send_from_directory,Response\n",
    "from werkzeug.utils import secure_filename\n",
    "from PyPDF2 import PdfFileReader, PdfFileWriter\n",
    "from flask_cors import cross_origin\n",
    "\n",
    "UPLOAD_FOLDER = 'static/uploads/'\n",
    "DOWNLOAD_FOLDER = 'static/uploads/'\n",
    "\n",
    "app = Flask(__name__, static_url_path=\"/static\")\n",
    "app.secret_key = \"secret key\"\n",
    "app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER\n",
    "app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER\n",
    "app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "def speak(file):\n",
    "    book=open(file,'rb')\n",
    "    pdfReader=PyPDF2.PdfFileReader(book)\n",
    "    pdfReader.getIsEncrypted()\n",
    "    pages=pdfReader.numPages\n",
    "    speaker=pyttsx3.init()\n",
    "    for i in range(pages):\n",
    "        page=pdfReader.getPage(i)\n",
    "        text=page.extractText()\n",
    "        speaker.say(text)\n",
    "        speaker.runAndWait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "def gen_frames(): \n",
    "    camera = cv2.VideoCapture(0)# generate frame by frame from camera\n",
    "    while True:\n",
    "        # Capture frame-by-frame\n",
    "        success, frame = camera.read()  # read the camera frame\n",
    "        if not success:\n",
    "            break\n",
    "        else:\n",
    "            frame=cv2.flip(frame,1)\n",
    "            gray= cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)\n",
    "            bodies = body_cascade.detectMultiScale(gray,1.3,5)\n",
    "            for(x,y,w,h) in bodies:\n",
    "                cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)\n",
    "                p=math.sqrt(w**2+h**2)\n",
    "                x=str(int((w1*f)/p))\n",
    "                speakerx=pyttsx3.init()\n",
    "                if int(x)<15:\n",
    "                    cv2.putText(frame,\"Warning\",(0,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)\n",
    "                    speakerx.say(\"Warning\")\n",
    "                    speakerx.runAndWait()\n",
    "                cv2.putText(frame,x,(0,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3,cv2.LINE_AA)\n",
    "            ret, buffer = cv2.imencode('.jpg', frame)\n",
    "            frame = buffer.tobytes()\n",
    "            yield (b'--frame\\r\\n'\n",
    "                   b'Content-Type: image/jpeg\\r\\n\\r\\n' + frame + b'\\r\\n')  # concat frame one by one and show result"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [],
   "source": [
    "def text_to_speech(text, gender):\n",
    "    voice_dict = {'Male': 0, 'Female': 1}\n",
    "    code = voice_dict[gender]\n",
    "\n",
    "    engine = pyttsx3.init()\n",
    "\n",
    "    # Setting up voice rate\n",
    "    engine.setProperty('rate', 125)\n",
    "\n",
    "    # Setting up volume level  between 0 and 1\n",
    "    engine.setProperty('volume', 0.8)\n",
    "\n",
    "    # Change voices: 0 for male and 1 for female\n",
    "    voices = engine.getProperty('voices')\n",
    "    engine.setProperty('voice', voices[code].id)\n",
    "\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      " * Serving Flask app \"__main__\" (lazy loading)\n",
      " * Environment: production\n",
      "   WARNING: This is a development server. Do not use it in a production deployment.\n",
      "   Use a production WSGI server instead.\n",
      " * Debug mode: off\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      " * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)\n"
     ]
    }
   ],
   "source": [
    "def allowed_file(filename):\n",
    "    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS\n",
    "\n",
    "\n",
    "@app.route('/')\n",
    "def index():\n",
    "    return render_template('index.html')\n",
    "\n",
    "@app.route('/static/audioLectures.html',methods=['GET', 'POST'])\n",
    "def index_audio():\n",
    "    if request.method == 'POST':\n",
    "        if 'file' not in request.files:\n",
    "            print('No file attached in request')\n",
    "            return redirect(request.url)\n",
    "        file = request.files['file']\n",
    "        if file.filename == '':\n",
    "            print('No file selected')\n",
    "            return redirect(request.url)\n",
    "        if file and allowed_file(file.filename):\n",
    "            filename = secure_filename(file.filename)\n",
    "            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))\n",
    "            process_file(os.path.join(app.config['UPLOAD_FOLDER'], filename), filename)\n",
    "            return redirect(url_for('uploaded_file', filename=filename))\n",
    "    return render_template('audioLectures.html')\n",
    "\n",
    "\n",
    "def process_file(path, filename):\n",
    "    speak(path)\n",
    "    # with open(path, 'a') as f:\n",
    "    #    f.write(\"\\nAdded processed content\")\n",
    "\n",
    "\n",
    "@app.route('/uploads/<filename>')\n",
    "def uploaded_file(filename):\n",
    "    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True) \n",
    "    \n",
    "\n",
    "@app.route('/static/video_feed')\n",
    "def video_feed():\n",
    "    \"\"\"Video streaming route. Put this in the src attribute of an img tag.\"\"\"\n",
    "    return Response(gen_frames(),\n",
    "                    mimetype='multipart/x-mixed-replace; boundary=frame')\n",
    "\n",
    "@app.route('/static/socialDistancing.html',methods=['GET', 'POST'])\n",
    "def index_social():\n",
    "    if request.method == 'GET':\n",
    "        return redirect(url_for('video_feed'))\n",
    "    \"\"\"Video streaming home page.\"\"\"\n",
    "    return render_template('socialDistancing.html')\n",
    "\n",
    "@app.route('/static/liveLectures.html',methods=['GET', 'POST'])\n",
    "def index_live():\n",
    "       return render_template('liveLectures.html')\n",
    "\n",
    "    \n",
    "@app.route('/static/summary.html',methods=['GET', 'POST'])\n",
    "def index_summary():\n",
    "    return render_template('summary.html')\n",
    "    \n",
    "@app.route('/static/text2speech.html',methods=['GET', 'POST'])\n",
    "@cross_origin()\n",
    "def index_text2speech():\n",
    "    if request.method == 'POST':\n",
    "        text = request.form['speech']\n",
    "        gender = request.form['voices']\n",
    "        text_to_speech(text, gender)\n",
    "        return render_template('text2speech.html')\n",
    "    else:\n",
    "        return render_template('text2speech.html')\n",
    "    \n",
    "@app.route('/static/index1.html',methods=['GET', 'POST'])\n",
    "def index_home():\n",
    "       return render_template('index1.html')\n",
    "\n",
    "if __name__ == '__main__':\n",
    "    app.run()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
