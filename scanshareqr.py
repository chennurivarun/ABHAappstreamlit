import streamlit as st
import qrcode
import io
import cv2
import numpy as np
from PIL import Image
from pyzbar.pyzbar import decode
from datetime import datetime

# Set page config
st.set_page_config(page_title="Scan & Share QR", layout="wide")

def scan_share_qr():
    st.markdown("<h2>Scan & Share QR Code</h2>", unsafe_allow_html=True)

    if 'logged_in' in st.session_state and st.session_state['logged_in']:
        abha_number = st.session_state.get('abha_number', 'Not provided')
        abha_address = st.session_state.get('abha_address', 'Not provided')
        name = st.session_state.get('name', 'User')

        col1, col2 = st.columns([2, 1])

        with col1:
            st.subheader("Generate QR Code to Share ABHA Profile")
            qr_data = f"Name: {name}\nABHA Number: {abha_number}\nABHA Address: {abha_address}\nGenerated On: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"

            if st.button("Generate QR Code"):
                qr_code_image = generate_qr_code(qr_data)
                st.image(qr_code_image, caption="Scan to view ABHA profile", width=250)

            st.subheader("Scan QR Code to View Information")
            uploaded_file = st.file_uploader("Upload an image of a QR Code", type=["png", "jpg", "jpeg"])

            if uploaded_file is not None:
                image = Image.open(uploaded_file)
                qr_code_data = scan_qr_code(image)
                if qr_code_data:
                    st.success(f"QR Code Data: {qr_code_data}")
                else:
                    st.error("No valid QR code found. Please try again with a different image.")

            st.subheader("Scan QR Code Using Camera")
            if st.button("Open Camera to Scan QR Code"):
                cap = cv2.VideoCapture(0)
                st_frame = st.empty()

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        st.error("Failed to access the camera. Please check your device settings.")
                        break

                    # Display the frame in Streamlit
                    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                    st_frame.image(frame, channels="RGB")

                    # Try to decode the QR code from the frame
                    decoded_objects = decode(frame)
                    if decoded_objects:
                        qr_code_data = decoded_objects[0].data.decode('utf-8')
                        st.success(f"QR Code Data: {qr_code_data}")
                        break

                    # Close camera on pressing 'q'
                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()
                cv2.destroyAllWindows()

        with col2:
            st.subheader("How to Use")
            st.markdown(
                """
                - Click the 'Generate QR Code' button to create a QR code containing your ABHA profile information.
                - Share this QR code with healthcare providers to allow them quick access to your profile.
                - You can also upload a QR code image or use your camera to scan and view the information it contains.
                """
            )

        st.subheader("Security Notice")
        st.info("Please ensure that you only share your ABHA QR code with trusted healthcare providers.")

        if st.button("Logout"):
            st.session_state['logged_in'] = False
            st.session_state['current_page'] = 'Login'
            st.success("Logged out successfully.")
            st.experimental_rerun()
    else:
        st.error("You need to log in to access this functionality.")
        if st.button("Go to Login"):
            st.session_state['current_page'] = 'Login'
            st.experimental_rerun()

def generate_qr_code(data):
    qr = qrcode.QRCode(version=1, error_correction=qrcode.constants.ERROR_CORRECT_L, box_size=10, border=4)
    qr.add_data(data)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')
    img_byte_arr = io.BytesIO()
    img.save(img_byte_arr)
    img_byte_arr.seek(0)
    return img_byte_arr

def scan_qr_code(image):
    img_array = np.array(image)
    decoded_objects = decode(img_array)
    if decoded_objects:
        for obj in decoded_objects:
            return obj.data.decode('utf-8')
    return None

if __name__ == "__main__":
    scan_share_qr()