import streamlit as st
from PIL import Image
with st.form(key="Login details"):
    username=st.text_input("Username")
    passowrd=st.text_input("Password")
    st.form_submit_button("Login")
st.checkbox("Agree")
    
img=Image.open("image.png")
st.sidebar.image(img.resize((400,400)))

st.title("My first StreamLit webapp")
st.subheader("This is Looking Good")


st.selectbox("Gender",["Male","Female","Others"])
w=st.sidebar.number_input("what's Your weight", step=1)
h=st.sidebar.number_input("How tall are you in meters")

def bmi_calc(w,h):
    bmi= round(w/(h**2),1)
    return bmi
a1,a2=st.columns(2)
with a1:
    st.checkbox("Accept")
    st.number_input("How old are you?",step=1)
    st.text_input("What is your name?")
with a2:
    st.checkbox("Reject")
    st.text_area("Address")
    st.date_input("Date of last visit?")

if st.button("Cal"):
    st.balloons()
    st.write(bmi_calc(w,h))
    
    
    
