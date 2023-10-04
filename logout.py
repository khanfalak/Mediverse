# logout.py

import streamlit as st

def app():
    st.title("Logout")
    st.write("You have been successfully logged out.")
    # Optionally, clear any user-related session state variables
    if hasattr(st.session_state, 'username'):
        
        st.session_state.login = False
        
