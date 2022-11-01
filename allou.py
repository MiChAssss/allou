# -*- coding: utf-8 -*-
"""Allou.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z83OUYswXrbiUGp8c5_QjnDu4NLxkS16
"""

import base64
import streamlit as st
st.set_page_config(page_title= "Allou Fun Park", page_icon=":tada")
""
def add_bgfrom_url():
  st.markdown(
      f"""
      <style>
      .stApp{{
        background-image:url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSKdIDwNVO4f5QGuTSN2ivKbtUi5L66dHu1HQ&usqp=CAU");
        background-attachment: fixed;
        background-size: cover
      }}
      </style>
      """,
      unsafe_allow_html=True
  )
  add_bgfrom_url()

with st.container():
  st.subheader("Panorama")
  st.write("7 Rides + XXL Pass + Mega Pass")
  st.write("Height>1m")
  st.write("5 euro")
  st.write("[Learn More >](https://www.allou.gr/gr/paihnidia/?Gameid=4) ")

