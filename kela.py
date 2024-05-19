import json
import time
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image

st.set_page_config(page_title="Kela", page_icon="🍌", layout="wide", initial_sidebar_state="expanded")

def load_lottiefile(filepath: str):
    with open(filepath, "r") as f:
        return json.load(f)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style/style.css")


# Page Title
st.title("The Golden Kela! 🍌")
st.header(
    """
    Our kela are sourced from the finest plantations and are guaranteed to be fresh and delicious.
    Perfect for snacking, baking, or smoothies. Packed with essential nutrients and vitamins.
    """
)


# Product Information
st.title("The Golden Kela Trailer 2024")

VIDEO_URL= "https://youtu.be/9xu1cd-Wkz4?si=gT9ezfvyEPx8Bgfs"
st.video(VIDEO_URL)

st.subheader("The Authentic Lore")

st.header("The Best Kela's You'll Ever Taste")

banana_image = "images/kela.png"
st.image(banana_image, caption="Fresh and delicious Kela", use_column_width=True)

# Product Metrics
st.write("---")
st.header("Product Metrics")
st.metric("Average Weight", "120g")
st.metric("Nutritional Value", "89 calories per 100g")
st.metric("Shelf Life", "7 days")

st.metric("Kela Temprature", '78°C' , '32°C')
st.metric(label="Active Kela's", value=69, delta=89, 
    delta_color="inverse")

# Sales Analytics
st.write("---")
st.header("Sales Analytics")
chart_data = pd.DataFrame(
    np.random.randn(30, 3),
    columns=["Kela's Sold", "Revenue ($)", "Customer Satisfaction"]
)
st.line_chart(chart_data)

# Contact Form
st.write("---")
st.header("Contact Us")

contact_form = """
<form action="https://formsubmit.co/ahmedzayan433@gmail.com" method="POST">
   <input type="hidden" name="_captcha" value="false">
   <input type="text" name="name" placeholder="Your name" required>
   <input type="email" name="email" placeholder="Your email" required>
   <input type="quantity" name="quantity" placeholder="Quantity?" required>
   <textarea name="message" placeholder="Your Message Here" required></textarea>
   <button type="submit">Send</button>
</form>
"""

with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Please fill the details below')

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.write("---") 
st.write("## Follow Us")
social_media_html = """
<div class="social-icons">
    <a href="https://www.facebook.com/yourprofile" target="_blank">
        <img src="images/facebook.png" alt="Facebook">
    </a>
    <a href="https://www.instagram.com/zeyox.4016/" target="_blank">
        <img src="images/insta.png" alt="Instagram">
    </a>
</div>
"""

st.markdown(social_media_html, unsafe_allow_html=True)

# Footer
st.write("---")
st.write("© 2024 Kela")
st.write("© All Rights Reserved ZeyoX™ ")