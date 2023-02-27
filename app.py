import streamlit as st
from PIL import Image


st.set_page_config(page_title="Sherlock Holmes")


st.title(":red[Sherlock Holmes]")


image = Image.open(r"C:\Users\admin\Desktop\innomatics internship\Project_2\sher.jpg")
st.image(image, use_column_width=True)


st.write("Sherlock Holmes is a fictional detective created by Sir Arthur Conan Doyle. Holmes is known for his exceptional analytical skills and his use of logic and observation to solve difficult cases. He has been featured in numerous books, films, and television shows.")


book = st.selectbox("Select a book:", ["A Study in Scarlet", "The Sign of the Four", "The Adventures of Sherlock Holmes"])

st.write(f"You selected: {book}")


if book == "A Study in Scarlet":
    chapter = st.slider("Select a chapter:", 1, 7, 1)
elif book == "The Sign of the Four":
    chapter = st.slider("Select a chapter:", 1, 12, 1)
else:
    chapter = st.slider("Select a chapter:", 1, 24, 1)


st.write(f"You selected Chapter {chapter}.")


st.write("Created by Varun Patil")
