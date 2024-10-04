import requests
import streamlit as st

def generate_aadhaar_otp(aadhaar_number):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/aadhaar/generateOtp"
    headers = {"Content-Type": "application/json"}
    data = {"aadhaar": aadhaar_number}
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        result = response.json()
        return result['txnId']  # Extract the transaction ID
    else:
        st.error(f"Error generating OTP: {response.text}")
        return None

def verify_otp(txn_id, otp):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/aadhaar/verifyOtp"
    headers = {"Content-Type": "application/json"}
    data = {"otp": otp, "txnId": txn_id}

    response = requests.post(url, json=data, headers=headers)

    if response.status_code == 200:
        return response.json()  # Return the result (authentication token)
    else:
        st.error(f"Error verifying OTP: {response.text}")
        return None

def create_abha_account(first_name, last_name, abha_address, auth_token):
    url = "https://sandbox.abdm.gov.in/sandbox/v3/healthid/aadhaar/create"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {auth_token}"
    }
    data = {
        "firstName": first_name,
        "lastName": last_name,
        "abhaAddress": abha_address
    }
    
    response = requests.post(url, json=data, headers=headers)
    
    if response.status_code == 200:
        st.success("ABHA Account created successfully!")
        return response.json()  # Return the success message
    else:
        st.error(f"Error creating account: {response.text}")
        return None
