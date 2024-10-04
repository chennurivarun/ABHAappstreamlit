import streamlit as st
import requests
import re
from datetime import datetime
from createaccount import create_abha_account, update_abha_profile
from dashboard import user_dashboard
from login import login_screen

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state['current_page'] = 'Home'
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False  # Track user login state
if 'current_user' not in st.session_state:
    st.session_state['current_user'] = None  # Store the current user's email
if 'abha_number' not in st.session_state:
    st.session_state['abha_number'] = None  # Store the user's ABHA number
if 'abha_address' not in st.session_state:
    st.session_state['abha_address'] = None  # Store the user's ABHA address
if 'name' not in st.session_state:
    st.session_state['name'] = None  # Store the user's name

# Callback functions for navigation
def go_to_home():
    st.session_state['current_page'] = 'Home'

def go_to_create_account():
    if st.session_state['logged_in']:
        st.session_state['current_page'] = 'Create ABHA Account'
    else:
        st.error("Please login to create an ABHA account.")

def go_to_login():
    st.session_state['current_page'] = 'Login'

def go_to_update_profile():
    if st.session_state['logged_in']:
        st.session_state['current_page'] = 'Profile Update'
    else:
        st.error("Please login to update your profile.")

def go_to_scan_share():
    if st.session_state['logged_in']:
        st.session_state['current_page'] = 'Scan & Share'
    else:
        st.error("Please login to access Scan & Share.")

def go_to_dashboard():
    st.session_state['current_page'] = 'User Dashboard'  # New page for user dashboard

# Load CSS and other components...
def load_css():
    st.markdown("""
    <style>
        .stApp {
            background-color: #000000;
        }
        h1, h2 {
            text-align: center;
            font-family: 'Roboto', sans-serif;
            letter-spacing: 2px;
        }
        h1 {
            color: #FFFFFF;
            font-size: 48px;
        }
        h2 {
            color: #AAAAAA;
            font-size: 24px;
        }
        .two-column {
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 20px;
            justify-content: center;
            align-items: center;
            width: 80%;
            margin: auto;
            margin-top: 50px;
        }
        .stButton>button {
            background-color: #333333;
            color: white;
            font-size: 18px;
            padding: 18px 32px;
            border-radius: 10px;
            border: 2px solid #666666;
            width: 100%;
            transition: background-color 0.3s ease, border-color 0.3s ease, transform 0.3s ease;
            font-family: 'Roboto', sans-serif;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.4);
        }
        .stButton>button:hover {
            background-color: #555555;
            border-color: #FF0000;
            transform: scale(1.02);
        }
        .footer {
            text-align: center;
            padding-top: 30px;
            color: #AAAAAA;
        }
        .footer a {
            color: #FF0000;
            text-decoration: none;
        }
        .footer a:hover {
            text-decoration: underline;
        }
        .sidebar .stButton>button {
            background-color: #333333;
            color: white;
            border-radius: 5px;
            font-size: 16px;
        }
        .sidebar .stButton>button.active {
            background-color: #FF0000;
            color: white;
        }
    </style>
    """, unsafe_allow_html=True)

# Home screen function
def home_screen():
    st.markdown("<h1>ABHA Onboarding Prototype</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Your easy solution to manage ABHA accounts.</h2>", unsafe_allow_html=True)

    st.markdown('<div class="two-column">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.button("🆕 Create ABHA Account", key="create", on_click=go_to_create_account)
        st.button("🔑 Login to ABHA", key="login", on_click=go_to_login)
    
    with col2:
        st.button("🔄 Update Profile", key="update", on_click=go_to_update_profile)
        st.button("📤 Scan & Share QR", key="share", on_click=go_to_scan_share)
    
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="footer">
        <p>Need help? Visit our <a href="#">support page</a>.</p>
    </div>
    """, unsafe_allow_html=True)

# Main function to run the app
def main():
    load_css()

    st.sidebar.title("Navigation")
    
    st.sidebar.button("Home", on_click=go_to_home)
    st.sidebar.button("Create ABHA Account", on_click=go_to_create_account)
    st.sidebar.button("Login", on_click=go_to_login)
    st.sidebar.button("Profile Update", on_click=go_to_update_profile)
    st.sidebar.button("Scan & Share", on_click=go_to_scan_share)

    if st.session_state['current_page'] == "Home":
        home_screen()
    elif st.session_state['current_page'] == "Create ABHA Account":
        create_abha_account()  # Call the create account function
    elif st.session_state['current_page'] == "Login":
        login_screen()
        if st.session_state['logged_in']:
            go_to_dashboard()  # Redirect to dashboard on successful login
    elif st.session_state['current_page'] == "User Dashboard":
        user_dashboard()  # Call the user dashboard function
    elif st.session_state['current_page'] == "Profile Update":
        update_abha_profile()  # Call the update profile function
    elif st.session_state['current_page'] == "Scan & Share":
        st.write("Scan & Share is under construction")

# Run the main function
if __name__ == "__main__":
    main()