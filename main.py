import streamlit as st
from streamlit_option_menu import option_menu

import home , doc ,bot , predict_disease , login , logout , signup , findambulance
st.set_page_config(
        page_title="diagnosis system",
                )

if "login" not in st.session_state:
    st.session_state.login = False

class MultiApp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, func):

        self.apps.append({
            "title": title,
            "function": func
        })

    def run():
        def is_user_logged_in():
            return st.session_state.login
        #app = st.sidebar(
        with st.sidebar:        
            app = option_menu(
                menu_title='Welcome ',
                options=['Home','Predict Disease','Precautionary Bot','Find Doc','Find an Ambulance','Sign Up','Login','Logout'],
                icons=['house-fill','clipboard-pulse','chat','file-earmark-plus','bus-front','person-circle','arrow-right-circle-fill','arrow-left-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0
            )
               

        if app == "Home":
            home.app()

        if app =="Predict Disease":
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                predict_disease.app()
            else:
                st.warning("You need to login first")

        if app == "Find Doc":
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                doc.FindDoctorApp()
            else:
                st.warning("You need to login first")

        if app == 'Find an Ambulance':
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                findambulance.FindAmbulanceApp()
            else:
                st.warning("You need to login first")

        if app == 'Precautionary Bot':
            if is_user_logged_in():
                #st.title(f"Welcome to the {app} section")
                bot.app()
            else:
                st.warning("You need to login first")

        if app == 'Login':
            login.app()

        if app == 'Logout':
            logout.app()

        if app =='Sign Up':
            signup.app()

    
    run()   