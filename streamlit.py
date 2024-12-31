import cv2
import streamlit as st

st.set_page_config(
    page_title="Sample Page"
)

st.title("4-Video Grid")

cap = cv2.VideoCapture("/videorepo/AMD_Advancing_AI.mp4")

col1, col2 = st.columns([1, 1])

while True:
    ret, frame1 = cap.read()
    ret, frame2 = cap.read()
    if not ret:
        break
    
    col1.image(frame1, channels="BGR")
    col2.image(frame2, channels="BGR")


    key = cv2.waitKey(1)
    if key == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
