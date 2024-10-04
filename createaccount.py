import streamlit as st
import requests
import re
from datetime import datetime

def create_abha_account():
    st.markdown("<h2>Create a New ABHA Account</h2>", unsafe_allow_html=True)

    # Step 1: Collect Aadhaar Number
    aadhaar_number = st.text_input("Enter your AADHAAR Number", max_chars=12)

    if st.button("Generate OTP"):
        if validate_aadhaar(aadhaar_number):
            txn_id = generate_aadhaar_otp(aadhaar_number)
            if txn_id:
                st.session_state['txn_id'] = txn_id
                st.success("OTP sent to your registered mobile number.")
        else:
            st.error("Invalid AADHAAR number. Please enter a valid 12-digit number.")

    # Step 2: Enter OTP (if txn_id is set, proceed with OTP input)
    if 'txn_id' in st.session_state:
        otp = st.text_input("Enter the OTP sent to your Aadhaar-linked mobile", type="password")
        if st.button("Verify OTP"):
            if validate_otp(otp):
                result = verify_otp(st.session_state['txn_id'], otp)
                if result:
                    st.session_state['auth_token'] = result['authToken']
                    st.success("OTP Verified! Proceed with ABHA creation.")
                    del st.session_state['txn_id']  # Remove txn_id after successful verification

                    # Step 3: Create ABHA Address (if OTP is verified)
                    first_name = st.text_input("First Name")
                    last_name = st.text_input("Last Name")
                    abha_address = st.text_input("Preferred ABHA Address")

                    # Collect additional user information
                    first_name = st.text_input("First Name")
                    last_name = st.text_input("Last Name")
                    abha_address = st.text_input("Preferred ABHA Address")                    

                    if st.button("Create ABHA Account"):
                        if validate_user_info(first_name, last_name, abha_address):
                            create_account(first_name, last_name, abha_address, st.session_state['auth_token'])
                        else:
                            st.error("Please ensure all user information is valid.")
            else:
                st.error("Invalid OTP. Please check and try again.")

# Validation functions
def validate_aadhaar(aadhaar_number):
    if len(aadhaar_number) != 12 or not aadhaar_number.isdigit() or aadhaar_number.startswith('0'):
        return False
    return True

def validate_otp(otp):
    if len(otp) != 6 or not otp.isdigit():
        return False
    return True

def validate_user_info(first_name, last_name, abha_address):
    # Check first name and last name
    name_pattern = r"^[A-Za-z\s]+$"  # Allow alphabets and spaces
    if not (re.match(name_pattern, first_name) and 2 <= len(first_name) <= 50):
        st.error("First name must be alphabetic and 2-50 characters long.")
        return False
    
    if not (re.match(name_pattern, last_name) and 2 <= len(last_name) <= 50):
        st.error("Last name must be alphabetic and 2-50 characters long.")
        return False

    # Ensure ABHA address is not empty
    if not abha_address:
        st.error("ABHA Address cannot be empty.")
        return False

    return True

def generate_aadhaar_otp(aadhaar_number):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/aadhaar/generateOtp"
    headers = {"Content-Type": "application/json"}
    data = {"aadhaar": aadhaar_number}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['txnId']
    else:
        st.error(f"Error generating OTP: {response.text}")
        return None

def verify_otp(txn_id, otp):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/aadhaar/verifyOtp"
    headers = {"Content-Type": "application/json"}
    data = {"otp": otp, "txnId": txn_id}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()
    else:
        st.error(f"Error verifying OTP: {response.text}")
        return None


def create_account(first_name, last_name, abha_address, auth_token):
    # Call the API to create the ABHA account
    # (Handle success and error responses)
    st.success(f"ABHA Account created successfully! ABHA Address: {abha_address}")

# Feature 2: Update ABHA Profile
def update_abha_profile():
    st.markdown("<h2>Update ABHA Profile</h2>", unsafe_allow_html=True)

    # Step 1: Collect ABHA Number
    abha_number = st.text_input("Enter your ABHA Number")

    if st.button("Generate OTP for Profile Update"):
        if abha_number:
            txn_id = generate_abha_otp(abha_number)
            if txn_id:
                st.session_state['txn_id'] = txn_id
                st.success("OTP sent to your registered mobile number.")
        else:
            st.error("Please enter a valid ABHA number.")

    # Step 2: Enter OTP (if txn_id is set, proceed with OTP input)
    if 'txn_id' in st.session_state:
        otp = st.text_input("Enter the OTP sent to your registered mobile", type="password")
        if st.button("Verify OTP for Profile Update"):
            if validate_otp(otp):
                result = verify_otp(st.session_state['txn_id'], otp)
                if result:
                    st.session_state['auth_token'] = result['authToken']
                    st.success("OTP Verified! Proceed with updating your profile.")
                    del st.session_state['txn_id']  # Remove txn_id after successful verification

                    # Step 3: Update ABHA Profile (if OTP is verified)
                    new_first_name = st.text_input("New First Name")
                    new_last_name = st.text_input("New Last Name")

                    if st.button("Update ABHA Profile"):
                        if validate_user_info(new_first_name, new_last_name, abha_number):
                            update_profile(new_first_name, new_last_name, abha_number, st.session_state['auth_token'])
                        else:
                            st.error("Please ensure all user information is valid.")
            else:
                st.error("Invalid OTP. Please check and try again.")

def generate_abha_otp(abha_number):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/generateOtp"
    headers = {"Content-Type": "application/json"}
    data = {"healthId": abha_number}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        result = response.json()
        return result['txnId']
    else:
        st.error(f"Error generating OTP: {response.text}")
        return None

def update_profile(first_name, last_name, abha_number, auth_token):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/updateProfile"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    data = {
        "healthId": abha_number,
        "firstName": first_name,
        "lastName": last_name
    }

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        st.success("ABHA Profile updated successfully!")
    else:
        st.error(f"Error updating profile: {response.text}")
