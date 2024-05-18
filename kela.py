from PIL import Image
import json
import streamlit as st
import os
import time
import requests
import streamlit as st
import pandas as pd
import numpy as np
import altair as alt
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)

st.set_page_config(page_title="Kela", page_icon=":banana:", layout="wide")

def load_lottiefile(filepath: str):
   with open(filepath, "r") as f:
      return json.load(f)
   
def local_css(file_name):
   with open(file_name) as f:
      st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
local_css("style/style.css")
   
lottie_coding = load_lottiefile("lottie/kela.json")
image_path = ("images/kela.png")

st.title("INTRODUCING")

st.header("THE GOLDEN KELA")
st.title("A Golden Marvel in fruit technology. With advanced features, it unveils the nutritional richness, from mangoes' vitamin-packed flesh to kiwis' protein-rich seeds.")
st.subheader(" Perfect for chefs and health enthusiasts, offering a fresh perspective on nutrition and flavor.")
st.header("[The Golden Kela Trailer 2024](https://www.instagram.com/p/C5igXiRNI_Z/)")
st.subheader(" ^^^^^^^^^^^^^^^^^^^^^^^^^ full lore of this kela")

with st.container():
    st.write('---')
    left_column, right_column = st.columns(2)
    with left_column:
     st.title("What we do")
     st.write("##")
     st.write("We provide the most perfect Golden Kela with the pricise machine nano technolgy")

with st.container():
   st.write("---")
   st.title("Our Kela's")
   st.write("##")
   image_column, text_column = st.columns((1, 1))
   with image_column:
      st.image(image_path)
   with text_column:
      st.header("Our best kela ever made")
      st.write("damn man just look at this thing, you want it inside you don't you")
st.subheader("gahhh dayyumm")

st.metric("Kela Temprature", '78°C' , '32°C')
st.metric(label="Active Kela's", value=69, delta=89, 
    delta_color="inverse")

st.header("Analytics of Kela")
chart_data = pd.DataFrame(np.random.randn(40, 3), columns=["Kela Bought", "Kela sold", "Kela Rotten"])

st.line_chart(chart_data)

with st.container():
    st.write("---")
    st.title("if u want to order please contact")
    st.write("##")

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
    time.sleep(10)
st.success('Please fill the details below')

left_column, right_column =st.columns(2)
with left_column:
   st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
   st.empty()



