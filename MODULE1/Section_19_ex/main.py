# Note: This script runs only on a local IDE with "streamlit run main.py"
import streamlit as st
from PIL import Image
 
st.subheader("Color to Grayscale Converter")
 
with st.expander("Start camera"):
    camera_image = st.camera_input("Camera")
 
if camera_image:
    img = Image.open(camera_image)
    gray_camera_img = img.convert('L')
    st.image(gray_camera_img)

with st.expander("Convert Image"):
    uploaded_image = st.file_uploader("Upload Image")

if uploaded_image:
    img = Image.open(uploaded_image)
    gray_image = img.convert("L")
    st.image(gray_image)
    
