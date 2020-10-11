# UP TO THE MINUTE?

LINK TO THE WEBSITE: https://ghci.azurewebsites.net/

GHCI : Innovative Solutions for the Specially-Abled people post COVID-19 life.

## 1] OBJECT DETECTION
         Yolo v3 is an algorithm that uses deep convolutional neural networks to detect objects.

  ###  Prerequisites:
         This project is written in Python 3.8.3 using Tensorflow (deep learning), NumPy (numerical computing), 
         OpenCV (computer vision) and seaborn (visualization) packages.

               pip install -r requirements.txt

  ###  Downloading official pretrained weights:
         Let's download official weights pretrained on COCO dataset.
   
               wget -P weights https://pjreddie.com/media/files/yolov3.weights
 
  ###  Running the model:

         Now you can run the model using app.py script.

## 2] SOCIAL DISTANCING TRACKER

  ### Tools and Dependencies
    
          • Python
          •	OpenCV
          •	NumPy
          •	Math

   ### Procedure
    
          Step 1: Detect people in the frame using YOLOv3 and depict it with bounding boxes.
          Step 2:The pixel distance is calculated from the user’s device to the centre of the bounding box. 
          Arbitrary values have been considere for the project. Distance is recorded simultaneously 
          depending on the movement of the person.

## 3] SUMMARY

  ### Prerequisites
    
          As we know, Python has various applications and there are different libraries for different purposes. In our 
          further demonstration, we will be using the following libraries:
      
              * Selenium:  Selenium is a web testing library. It is used to automate browser activities.
              * BeautifulSoup: Beautiful Soup is a Python package for parsing HTML and XML documents. It creates parse trees 
                that is helpful to extract the data easily.

   ### Procedure
   
          Step 1: Find the URL that you want to scrape
          Step 2: Inspecting the Page
          Step 3: Find the data you want to extract
          Step 4: Write the code
          Step 5: Run the code and extract the data
          Step 6: Store the data in a required format
     
## 4] LIVE TEXT TRANSLATION OF SPEECH

          The model uses the Web Speech API
      
 ### Procedure

          Step 1:Select the “Start Recognition” button to start recording.
          Step 2: The API then detects voice and converts into speech. If nothing is heard it gives out a message 
          for the user to start speaking again.
          Step 3: The text is displayed on screen and can be saved as html or text files.
          Step 4: Stop recording...

## 5] AUDIO BOOKS

  ### Prerequisites

          This project is written in Python 3.8.3 using Pyttsx3 (text-to-speech conversion library in Python. 
          Unlike alternative libraries,  it works offline, and is compatible with both Python 2 and 3)
          and PyPDF2 (Pure-Python library built as a PDF toolkit) libraries.

             pip install pyttsx3 
             pip install PyPDF2

  ### Procedure:
     
          Step 1: Input a .pdf file from the user using html, css and js frontend. 
          Step 2: Store the uploaded pdf in the uploads folder using Flask.
          Step 3: Open the file and read it using PyPDF2.PdfFileReader().
          Step 4: Obtain the number of pages in the uploaded file.
          Step 5: Initialize the speaker using pyttsx3.init().
          Step 6: Extract text from each page using .extractText() and tell it out loud using speaker.say(text) and
          speaker.runAndWait() commands.

## 6] TEXT2SPEECH

  ### Prerequisites:

          This project is written in Python 3.8.3 using Pyttsx3 (text-to-speech conversion library in Python. 
          Unlike alternative libraries, it works offline, and is compatible with both Python 2 and 3) library.

              pip install pyttsx3 
    
 ### Procedure:
 
          Step 1: Input the text and male/female version choice from the user using html, css and js frontend. 
          Step 2: Store text and chosen option using flask.
          Step 3: Initialize the speaker using pyttsx3.init().
          Step 4: Set the voice rate and volume level using speaker.setProperty().
          Step 5: Obtain the text and given choice using speaker.getProperty().
          Step 6: Convert it to speech using speaker.say(text) and speaker.runAndWait() commands.

