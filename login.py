import streamlit as st

#mysql
import mysql.connector
import hashlib
import re

# Initialize session state
def app():
    if "login" not in st.session_state:
        st.session_state.login = False


    # Database connection
    db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="mysql"
    )
    cursor = db.cursor()

    # Hashing Function
    def make_hashes(password):
        return hashlib.sha256(str.encode(password)).hexdigest()


    def login_user(username, password):
        cursor.execute('SELECT * FROM usertable WHERE username = BINARY %s', (username,))
        user = cursor.fetchone()
        if user and check_hashes(password, user[1]):
            return True
        return False

    def check_hashes(password, hashed_text):
        return make_hashes(password) == hashed_text

    # Define the is_user_logged_in function
    def is_user_logged_in():
        return st.session_state.login

    if is_user_logged_in():

        st.write("You are already logged in.")
    else:
        st.subheader("Login")
        username = st.text_input("User Name")
        password = st.text_input("Password", type='password')
        if st.checkbox("Login"):
            #create_usertable()

            if login_user(username, password):
                st.success("Logged In as {}".format(username))
                st.session_state.login = True
                st.session_state.username = username
                
            else:
                st.warning("Incorrect Username/Password")
