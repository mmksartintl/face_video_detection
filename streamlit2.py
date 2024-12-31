import streamlit as st
import cv2
import face_recognition

st.set_page_config(
    page_title="Workout file"
)

st.title("Multiple Cameras")

cam1, cam2 = st.columns((1, 1))
video_1 = cam1.empty()
video_2 = cam2.empty()

cap1 = cv2.VideoCapture("/videorepo/AMD_Advancing_AI.mp4")
cap2 = cv2.VideoCapture("/videorepo/AMD_Advancing_AI.mp4")

count = 0

while cap1.isOpened() or cap2.isOpened():
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2RGB)
    frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2RGB)

    if (count % 10 == 0):
       # Find all the faces in the current frame of video
       face_locations = face_recognition.face_locations(frame2)
       for top, right, bottom, left in face_locations:
          # Draw a box around the face
          cv2.rectangle(frame2, (left, top), (right, bottom), (255, 0, 0), 2)

       video_1.image(frame1, channels="RGB")
       video_2.image(frame2, channels="RGB")

    count = count + 1

cap1.release()
cap2.release()
cv2.destroyAllWindows()
