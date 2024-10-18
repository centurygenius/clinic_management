# **Clinic Management Application**

## **Introduction**

The Clinic Management Application manages the core procedures in a clinic. It replaces the traditional approach of carrying files from one station to the other. These procedures are automated.

A new staff of the clinic is registered by the IT Department and the credentials are eventually given to the staff to reset the password when the staff logs into the platform. 

The application recognizes two categories of staff - Nurse and Doctor. A nurse log in to work using the Nursing Staion in the platform where a form is available to manage a patient by recording a saving health information of a patient vital signs. The nurse submits the form and appends signation by writing full names. Then the patient proceeds to see a doctor.

A doctor logs in to manage a patient by viewing the patient health record from the Nursing Station and manages the patient by providing necessary prescription and or comment in a form using the Doctor Station provided in the application.

The application is extremely relevant in this dispensation as it improves timely delivery of health care services.

## **Author**

Abiona Samuel Olawuyi(samuelo.abiona@gmail.com)

## **Usage**

### **Installation**

To run the application locally on your computer, install Python globally by visiting Python website and check to be sure that the installation was properly done by checking the Python version stalled. Then, follow these steps:

1. Clone the repository using

    ```https://github.com/centurygenius/clinic_management.git```

2. Navigate to the directory 

    ```cd clinic_management```

3. Create a virtual environment on Windows

    ```python -m venv <your-virtual-environment-name>```

4. Create a virtual environment on Linux

    ```python3 -m venv <your-virtual-environment-name>```

5. Activate your virtual environment on Windows

    ```source <your-virtual-environment-name>/scripts/activate```

6. Activate your virtual environment on Linux

    ```source <your-virtual-environment-name>/bin/activate```

7. Install Django assuming you are using Windows

    ```pip install django```

8. Navigate to the project root directory

    ```cd hospital```

9. Run the development server

    ```python manage.py runserver```

10. Navigate to the IP to view the application on your browser

    ```http://127.0.0.1:8000/```



