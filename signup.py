import streamlit as st
#mysql
import mysql.connector
import hashlib
import re
def app():
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

    # Password validation function
    def is_valid_password(password):
        # Check if password is at least 8 characters long
        if len(password) < 8:
            return False

        # Check for at least one uppercase letter
        if not any(char.isupper() for char in password):
            return False

        # Check for at least one lowercase letter
        if not any(char.islower() for char in password):
            return False

        # Check for at least one special character (e.g., !, @, #, $, %)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
            return False

        return True

    # DB Functions
    def create_usertable():
        cursor.execute('CREATE TABLE IF NOT EXISTS usertable(username VARCHAR(255), password VARCHAR(255))')

    def add_userdata(username, password):
        cursor.execute('INSERT INTO usertable(username, password) VALUES (%s, %s)', (username, password))
        db.commit()

    st.subheader("Create New Account")
    new_user = st.text_input("Username")
    new_password = st.text_input("Password", type='password')

    if st.button("Signup"):
        # Call your functions here, assuming they are defined elsewhere
        if is_valid_password(new_password):
            hashed_password = make_hashes(new_password)
            add_userdata(new_user, hashed_password)
            st.success("You have successfully created a valid Account")
            st.info("Go to Login Menu to login")
        else:
            st.warning("Password must be at least 8 characters long, contain at least one uppercase letter, one lowercase letter, and one special character.")
