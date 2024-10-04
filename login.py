import streamlit as st

# Simulated database of users
USER_DATABASE = {
    "user@example.com": "password123",  # Sample user for login
}

# Function for user login
def login_screen():
    st.markdown("<h2>Login to ABHA</h2>", unsafe_allow_html=True)
    email = st.text_input("Email", help="Enter your registered email address.")
    password = st.text_input("Password", type="password", help="Enter your password.")
    
    def handle_login():
        if email in USER_DATABASE and USER_DATABASE[email] == password:
            st.success(f"Logged in as {email}")
            st.session_state['logged_in'] = True  # Set logged-in state
            st.session_state['current_user'] = email  # Store current user's email
            st.session_state['current_page'] = 'User Dashboard'  # Redirect to user dashboard
        else:
            st.error("Invalid email or password. Please check your credentials and try again.")

    st.button("Login", key="login", on_click=handle_login)

    st.markdown("<p style='text-align: center;'>Forgot your password? <a href='#'>Click here</a> to reset it.</p>", unsafe_allow_html=True)

if __name__ == "__main__":
    login_screen()