# face_video_detection
Scans a video and identify faces circunventing with a square

Implements:
- face_recognition library for detecting faces (uses deep learning techniques to achieve high accuracy in face detection)
- Streamlit in Python to user interface https://flask.palletsprojects.com/en/stable/

NOTICE:
- Due to HW requirements, start a VM with 4G and 2 CPUs

Steps:

1) run a docker image
   $ docker container run -d -p 8501:8501 -v $(pwd)/videorepo:/videorepo python:3.11-slim sleep infinity

2) apt-get update && apt install -y cmake g++

3) pip install dlib (can take ~ 7 minutes to install)

4) pip install -r requirements.txt

5) running "python main.py", the following errors will raise. 
   install the appropriate libraries as indicated. 

ImportError: libGL.so.1: cannot open shared object file: No such file or directory

- apt-get update && apt-get install libgl1


ImportError: libgthread-2.0.so.0: cannot open shared object file: No such file or directory

- apt-get install libglib2.0-0

5) streamlit run streamlit.py  (generates a lot of video frames)

6) streamlit run streamlit2.py