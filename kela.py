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
    Our Kela Are Sourced From The Finest Plantations And Are Guaranteed To Be Fresh and Delicious. 
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

st.metric("Kela's Temprature", '50°C' , '30°C')
st.metric(label="Current Slaves Working To Make Golden Kela", value=69, delta="89 Executed", 
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
st.header("Order Now!")
contact_form = """
<form action="https://formsubmit.co/ahmedzayan433@gmail.com" method="POST">
   <input type="hidden" name="_captcha" value="false">
   <input type="text" name="name" placeholder="Your name" required>
   <input type="email" name="email" placeholder="Your email" required>
   <input type="quantity" name="quantity" placeholder="Your Quantity" required>
   <textarea name="message" placeholder="Your Address" required></textarea>
   <button type="submit">Order</button>
</form>
"""

with st.spinner('Wait for it...'):
    time.sleep(1)
st.success('Please fill the details below')

left_column, right_column = st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
     st.empty()

# Footer
st.write("---")
st.write("© 2024 Kela")
st.write("© All Rights Reserved ZeyoX™ ")