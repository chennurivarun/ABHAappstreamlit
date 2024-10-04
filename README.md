# ABHAappStreamlit

ABHAappStreamlit is a user-friendly dashboard built with Streamlit, allowing users to manage their ABHA (Ayushman Bharat Health Account) profile, view and update health records, and track important health data such as vaccinations, medication adherence, lab results, consultations, and more. This application aims to simplify health management by providing an intuitive interface for users to access and manage their health data.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Setup Instructions](#setup-instructions)
  - [Prerequisites](#prerequisites)
  - [Local Setup](#local-setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features

- **ABHA Profile Management**: Users can update their personal details such as name, gender, date of birth, and more.
- **Health Records Management**: Add, view, and delete personal health records.
- **Vaccination Tracking**: Display vaccination status with progress bars and charts.
- **Medication Adherence**: Track medication adherence with pie charts and trend lines.
- **Lab Test Results**: Show recent lab test results with trend lines and critical health indicators.
- **Consultations & Appointments**: Track past consultations and manage upcoming appointments.
- **Activity Levels & Sleep Patterns**: Visualize physical activity levels and sleep patterns.
- **BMI & Vital Stats Monitoring**: Track BMI, blood pressure, pulse rate, and other vital stats.
- **QR Code Generation**: Easily generate and share ABHA profile details using a QR code.

## Technologies

- **Streamlit**: The core technology for building the interactive web application.
- **Python**: The main programming language used in the project.
- **Pandas**: For managing health data.
- **Matplotlib & Streamlit-ECharts**: For generating visualizations such as charts and graphs.
- **qrcode**: For generating ABHA profile QR codes.

## Setup Instructions

### Prerequisites

Ensure you have the following installed on your local machine:

- **Python 3.8+**
- **Git** (to clone the repository)
- **pip** (Python package installer)

### Local Setup

1. **Clone the Repository**

   Open a terminal and run the following command to clone the repository:

   ```bash
   git clone https://github.com/chennurivarun/ABHAappstreamlit.git
2. Navigate to the Project Directory

After cloning the repository, navigate into the project directory by running:

    ```bash
    cd ABHAappstreamlit
3. Create and Activate a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

To create a virtual environment:

    ```bash
    python -m venv venv

Then activate it:

For Windows:

    ```bash
    venv\Scripts\activate
For macOS/Linux:

    ```bash
    source venv/bin/activate
Install Dependencies

Install the required Python packages from the requirements.txt file:

    ```bash
    pip install -r requirements.txt
Run the Streamlit App

Once the dependencies are installed, you can run the app using:

    ```bash
    streamlit run app.py

## Usage
Once the app is running, users can:

- **Login**: Enter the credentials to access the dashboard. (default : email: user@exampel.com, password: Password123)
- **Manage ABHA Profile**: View and update your profile information, such as name, gender, and date of birth.
- **Track Health Data**: Visualize important health information such as vaccination status, lab results, medication adherence, and more.
- **Generate QR Code**: Share your ABHA profile details through a QR code.

## Contributing

Contributions are welcome! If you want to contribute to this project, please follow these steps:

Fork the repository.
Create a new feature branch (git checkout -b feature/your-feature).
Commit your changes (git commit -m 'Add some feature').
Push to the branch (git push origin feature/your-feature).
Open a pull request.
License
This project is licensed under the MIT License. See the LICENSE file for more details.
    
