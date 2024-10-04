import streamlit as st
import qrcode
import io
from streamlit_echarts import st_echarts
import datetime

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
            st.session_state['logged_in'] = True
            st.session_state['current_user'] = email
            st.session_state['current_page'] = 'User Dashboard'
        else:
            st.error("Invalid email or password. Please check your credentials and try again.")

    st.button("Login", key="login", on_click=handle_login)

    st.markdown("<p style='text-align: center;'>Forgot your password? <a href='#'>Click here</a> to reset it.</p>", unsafe_allow_html=True)

# Function for user dashboard
def user_dashboard():
    st.markdown("<h1 style='text-align: center;'>ABHA User Dashboard</h1>", unsafe_allow_html=True)

    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        abha_number = st.session_state.get('abha_number', 'Not provided')
        abha_address = st.session_state.get('abha_address', 'Not provided')
        name = st.session_state.get('current_user', 'User')

        st.success(f"Welcome back, {name}!")

        # Profile section
        with st.expander("Your Profile Information", expanded=False):
            col1, col2 = st.columns([3, 1])
            with col1:
                st.write(f"**Name:** {name}")
                st.write(f"**ABHA Number:** {abha_number}")
                st.write(f"**ABHA Address:** {abha_address}")
                st.write(f"**Gender:** {st.session_state.get('gender', 'Not provided')}")
                st.write(f"**Date of Birth:** {st.session_state.get('dob', 'Not provided')}")

                st.subheader("Update Profile")
                new_name = st.text_input("Update Name", value=name, help="Enter your updated name.")
                new_gender = st.selectbox("Update Gender", ['Male', 'Female', 'Other'], index=['Male', 'Female', 'Other'].index(st.session_state.get('gender', 'Male')))
                new_dob = st.date_input("Update Date of Birth", value=st.session_state.get('dob', datetime.date(2000, 1, 1)))

                if st.button("Save Changes", key="save_profile"):
                    st.session_state.update({
                        'name': new_name,
                        'gender': new_gender,
                        'dob': new_dob
                    })
                    st.success("Profile updated successfully!")

        # Health Records
        with st.expander("Manage Your Health Records", expanded=False):
            records = st.session_state.get('health_records', [])
            if not records:
                st.info("No health records available. Add a new record below.")
            else:
                for idx, record in enumerate(records, 1):
                    with st.expander(f"Record {idx}", expanded=False):
                        st.write(record)
                        if st.button(f"Delete Record {idx}", key=f"delete_{idx}"):
                            records.pop(idx - 1)
                            st.session_state['health_records'] = records
                            st.success(f"Record '{record}' deleted!")

            new_record = st.text_input("Add a new health record", help="Enter the details of your health record here.")
            if st.button("Add Record", key="add_record"):
                if new_record:
                    records.append(new_record)
                    st.session_state['health_records'] = records
                    st.success(f"Record '{new_record}' added!")
                else:
                    st.error("Please enter a valid record.")

        # Health Overview Section
        with st.expander("Health Data Overview", expanded=True):
            col1, col2, col3 = st.columns(3)

            # Vaccination Status
            with col1:
                st.subheader("Vaccination Status")
                show_vaccination_status()

            # Medication Adherence
            with col2:
                st.subheader("Medication Adherence")
                show_medication_adherence()

            # Lab Test Results
            with col3:
                st.subheader("Lab Test Results")
                show_lab_tests()

        # Second row of health data overview
        col1, col2 = st.columns(2)
        with col1:
            with st.expander("Consultations & Appointments", expanded=False):
                show_consultations()

            with st.expander("Activity Levels", expanded=False):
                show_activity_levels()

        with col2:
            with st.expander("Sleep Patterns", expanded=False):
                show_sleep_patterns()

            with st.expander("BMI & Vital Stats", expanded=False):
                show_bmi_vital_stats()

        # QR Code Section
        st.markdown("<hr>", unsafe_allow_html=True)
        st.subheader("Generate QR Code")
        if st.button("Generate QR Code for Sharing", key="generate_qr_button", help="Click to generate your ABHA QR code"):
            qr_data = f"{abha_number}|{name}|{st.session_state.get('gender')}|{st.session_state.get('dob')}"
            qr_code_image = generate_qr_code(qr_data)
            st.image(qr_code_image, caption="Scan to share your ABHA profile", width=200)

    else:
        st.error("You need to log in to access the dashboard.")
        if st.button("Go to Login"):
            st.session_state['current_page'] = 'Login'

# Helper Functions for different sections

def show_vaccination_status():
    vaccinations = ["COVID-19", "Flu", "Hepatitis B", "Tetanus"]
    completed = [1, 1, 0, 1]  # 1: completed, 0: pending
    bar_option = {
        "xAxis": {"type": "category", "data": vaccinations},
        "yAxis": {"type": "value"},
        "series": [{"data": [100, 100, 0, 100], "type": "bar", "itemStyle": {"color": "#4caf50"}}],
    }
    st_echarts(options=bar_option, height="300px")
    
    progress = sum(completed) / len(completed)
    st.progress(progress)

def show_medication_adherence():
    pie_option = {
        "series": [
            {
                "name": "Medication Adherence",
                "type": "pie",
                "radius": ["40%", "70%"],
                "data": [
                    {"value": 80, "name": "Taken on Time"},
                    {"value": 20, "name": "Missed"},
                ],
                "itemStyle": {"borderRadius": 10, "borderColor": "#fff", "borderWidth": 2},
            }
        ],
    }
    st_echarts(options=pie_option, height="300px")

    line_option = {
        "xAxis": {"type": "category", "data": ["Week 1", "Week 2", "Week 3", "Week 4"]},
        "yAxis": {"type": "value"},
        "series": [{"data": [90, 80, 85, 92], "type": "line", "itemStyle": {"color": "#f97316"}}],
    }
    st_echarts(options=line_option, height="300px")

def show_lab_tests():
    line_option = {
        "xAxis": {"type": "category", "data": ["Jan", "Feb", "Mar", "Apr"]},
        "yAxis": {"type": "value", "min": 50, "max": 150, "name": "Test Result"},
        "series": [
            {"data": [120, 110, 130, 125], "type": "line", "itemStyle": {"color": "#3b82f6"}},
        ],
    }
    st_echarts(options=line_option, height="300px")
    
    st.info("Recent test results are within the normal range.")

def show_consultations():
    bar_option = {
        "xAxis": {"type": "category", "data": ["GP", "Specialist", "Dentist", "Therapist"]},
        "yAxis": {"type": "value"},
        "series": [{"data": [4, 2, 1, 3], "type": "bar", "itemStyle": {"color": "#3b82f6"}}],
    }
    st_echarts(options=bar_option, height="300px")

    st.subheader("Upcoming Appointments")
    appointments = [
        {"date": "2024-10-10", "type": "GP Consultation", "time": "10:00 AM"},
        {"date": "2024-10-15", "type": "Dentist", "time": "2:00 PM"},
    ]
    for appt in appointments:
        st.write(f"**{appt['type']}**: {appt['date']} at {appt['time']}")

def show_activity_levels():
    activity_data = {"Mon": 3000, "Tue": 5000, "Wed": 6000, "Thu": 7000, "Fri": 2000, "Sat": 4500, "Sun": 3000}
    bar_option = {
        "xAxis": {"type": "category", "data": list(activity_data.keys())},
        "yAxis": {"type": "value"},
        "series": [{"data": list(activity_data.values()), "type": "bar", "itemStyle": {"color": "#3b82f6"}}],
    }
    st_echarts(options=bar_option, height="300px")

def show_sleep_patterns():
    line_option = {
        "xAxis": {"type": "category", "data": ["Week 1", "Week 2", "Week 3", "Week 4"]},
        "yAxis": {"type": "value"},
        "series": [{"data": [7, 6.5, 7.5, 8], "type": "line", "itemStyle": {"color": "#f97316"}}],
    }
    st_echarts(options=line_option, height="300px")

    pie_option = {
        "series": [
            {
                "name": "Sleep Quality",
                "type": "pie",
                "radius": ["40%", "70%"],
                "data": [
                    {"value": 65, "name": "Deep Sleep"},
                    {"value": 35, "name": "Light Sleep"},
                ],
                "itemStyle": {"borderRadius": 10, "borderColor": "#fff", "borderWidth": 2},
            }
        ],
    }
    st_echarts(options=pie_option, height="300px")

def show_bmi_vital_stats():
    st.write("BMI: 22.5 (Normal)")
    st.write("Blood Pressure: 120/80 mmHg (Normal)")
    st.write("Pulse Rate: 72 bpm (Normal)")

    # Placeholder for gauge chart
    st.info("Vital Stats are within normal ranges.")

# Function to generate QR Code
def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)
    return img_byte_arr

if __name__ == "__main__":
    if 'current_page' not in st.session_state:
        st.session_state['current_page'] = 'Login'

    if st.session_state['current_page'] == 'Login':
        login_screen()
    elif st.session_state['current_page'] == 'User Dashboard':
        user_dashboard()
