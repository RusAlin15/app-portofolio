import streamlit as st
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
- Developed a
    """
    st.text(content)