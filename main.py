import streamlit as st
from createaccount import create_abha_account
from login import login_to_abha
from updateprofile import update_profile
from scanshareqr import scan_and_share_qr

# Main function to run the app
def main():
    # Sidebar for navigation
    st.sidebar.title("Navigation")
    menu = ["Home", "Create ABHA Account", "Login", "Profile Update", "Scan & Share"]
    choice = st.sidebar.selectbox("Menu", menu)

    # Route the user to the correct screen based on their choice
    if choice == "Home":
        home_screen()

    elif choice == "Create ABHA Account":
        create_abha_account()

    elif choice == "Login":
        login_to_abha()

    elif choice == "Profile Update":
        update_profile()

    elif choice == "Scan & Share":
        scan_and_share_qr()

# Modular function for Home Screen
def home_screen():
    st.markdown("<h1>ABHA Onboarding Prototype</h1>", unsafe_allow_html=True)
    st.markdown("<h2>Your easy solution to manage ABHA accounts.</h2>", unsafe_allow_html=True)
    
    # Two-column layout for buttons
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🆕 Create ABHA Account"):
            create_abha_account()
        if st.button("🔑 Login to ABHA"):
            login_to_abha()
    
    with col2:
        if st.button("🔄 Update Profile"):
            update_profile()
        if st.button("📤 Scan & Share QR"):
            scan_and_share_qr()
    
    footer()

# Footer function for reuse
def footer():
    st.markdown("""
    <div class="footer">
        <p>Need help? Visit our <a href="#">support page</a>.</p>
    </div>
    """, unsafe_allow_html=True)

# Run the app
if __name__ == "__main__":
    main()
