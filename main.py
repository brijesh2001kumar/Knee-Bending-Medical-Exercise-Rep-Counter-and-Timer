# Deep learning libraries (Tensorflow Framework)
import numpy as np

# Libraries required for deployment (Done using Streamlit)
import streamlit as st

#settimng up background image for app
st.markdown(
   f'''
   <style>
   .stApp {{
             background: url("https://img.freepik.com/premium-photo/abstract-communication-technology-network-concept_34629-641.jpg?w=1380");
             background-size: cover
         }}
   </style>
   ''',
   unsafe_allow_html=True)

#creating containers for different sections of app
header = st.container()
video = st.container()
input=st.form(key='form')
output=st.container()
model_intro = st.container()
model_details = st.container()
references = st.container()


with header:
    st.title('Knee Bend Medical Exercise REP Counter and Timer using Mediapipe library')
    st.markdown("""---""")
    st.write('In this project, I developed a knee bend exercise rep counter and timer using the Mediapipe library. The system monitors knee angles and initiates a timer when the angle is below 135 degrees, requiring a minimum of 8 seconds to complete one repetition. It tracks and displays total reps, time elapsed, and provides interactive feedback messages.')
    st.image('image.png')
    st.markdown("""---""")
    
with video:

    st.subheader('Sample Implementation of project')
    video = open('trial_run_edited.mp4','rb')
    st.video(video)
    st.markdown("""---""")

with model_details:
    st.subheader('Project Methodology')
    st.subheader('')
    st.write('**1. Data Acquisition and Preprocessing:**\n\n For data acquisition, video input was captured from a webcam. The Mediapipe library was employed to detect and track key body landmarks, with a focus on knee positions. Calibration was performed to ensure precise landmark detection.')
    st.markdown("<h6 style='text-align: center; color: white;'>MediaPipe Pose Estimation</h6>", unsafe_allow_html=True)
    st.image('image2.png')    
    st.write('**2. Angle Calculation:**\n\n The system calculated knee angles by analyzing the positions of key knee landmarks. These knee angles were continuously monitored as users performed knee bend exercises.')
    st.write('**3. Repetition Detection:**\n\n Valid knee bends were identified by setting a threshold angle (e.g., 135 degrees). The system implemented logic to detect the start and end of each knee bend repetition by tracking changes in knee angles. The start time of each repetition was recorded.')
    st.write('**4. Timer Implementation:**\n\n Timers were initiated when valid knee bends began. The system measured elapsed time during each repetition and stopped timers when knee angles returned above the threshold, indicating the completion of a repetition. This ensured a minimum 8-second duration for each repetition.')
    st.write('**5. Rep Counting:**\n\n A rep counter was implemented to track the number of valid repetitions. The rep count was updated upon detecting valid repetitions.')
    st.write('**6. Interactive Feedback:**\n\n Users received real-time feedback, including the current rep count, elapsed time, and interactive messages. Alerts were issued if users did not maintain the minimum 8-second hold time or if knee angles did not meet the desired threshold.')
    st.markdown("""---""")

