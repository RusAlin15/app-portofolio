import streamlit as st
import pandas

st.set_page_config(layout="wide")

column1, column2  = st.columns(2)

with column1:
    st.image("images/photo.png")

with column2:
    st.title("Alin Rus El-Hassaina")
    content = """
    I had improved a lot of skills and competences through my involvement in different extracurricular activities and from work experience:
- Had the opportunity to interact with many people with different passions, thoughts and different cultural backgrounds
- Gained a lot of experience in team working
    """
    st.write(content)

content2 = """
"Below you cand find some of the apps I have built in Python. Feel free to contact me!"
"""
st.write(content2)

column3, column4  = st.columns(2)

df = pandas.read_csv("data.csv", sep = ';')
with column3:
    for index, row in df[:int((len(df)/2))].iterrows():
        st.header(row['title'])

with column4:
    for index, row in df[int((len(df)/2)):].iterrows():
        st.header(row['title'])

