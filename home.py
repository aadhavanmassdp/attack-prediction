import streamlit as st


# Home Page
def home_page():
    st.image('bkg.png', use_container_width=True)
    st.title('Home')
    st.write('Welcome to the DDOS Attack Detection App!')
