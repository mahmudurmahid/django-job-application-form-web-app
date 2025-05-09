# 📝 Django Job Application Form Web App

A comprehensive web application built with Django, designed to help organizations collect and manage job applications effectively.

---

## 📖 Table of Contents

- [📝 Django Job Application Form Web App](#-django-job-application-form-web-app)
- [📖 Table of Contents](#-table-of-contents)
- [🧑‍💼 User Experience (UX)](#-user-experience-ux)
  - [🧾 User Stories](#-user-stories)
- [🎨 Design](#-design)
  - [🗂 Interface Structure](#-interface-structure)
  - [🌈 Color Scheme & Typography](#-color-scheme--typography)
- [🚀 Features](#-features)
  - [✅ Implemented Features](#-implemented-features)
  - [🛠️ Planned Improvements](#-planned-improvements)
- [💻 Technologies Used](#-technologies-used)
  - [🧑‍💻 Languages Used](#-languages-used)
  - [📚 Libraries Used](#-libraries-used)
- [📁 Project Files](#-project-files)
- [🛠 Installation & Usage](#-installation--usage)
  - [⚙️ How to Run](#-how-to-run)
  - [🧾 Configuration](#-configuration)
- [🔒 Security & Environment Configuration](#-security-&environment-configuration)
  - [🧑‍💻 Use of `python-dotenv`](#-use-of-python-dotenv)
  - [🔧 Setting Up a Forked Repository](#-setting-up-a-forked-repository)
- [✅ Testing](#-testing)
  - [🧪 Test Scenarios Checklist](#-test-scenarios-checklist)
  - [🧪 Running Tests](#-running-tests)
- [🙌 Credits](#-credits)
  - [👨‍💻 Author](#-author)
  - [🧰 Tools & Technologies](#-tools--technologies)
  - [📚 Learning Resources & Documentation](#-learning-resources--documentation)

---

## 🧑‍💼 User Experience (UX)

This application is created to simplify the job application process. Applicants can fill out forms and upload resumes, while recruiters can easily manage and review applications.

### 🧾 User Stories

- **As an applicant**, I want to fill out and submit a job application form online, so that I can apply for a job easily.
- **As a recruiter**, I want to store and manage the received job applications, so that I can review candidates efficiently.
- **As a system administrator**, I want to configure and deploy the application without hassle, so that it can be used in production environments.

---

## 🎨 Design

### 🗂 Interface Structure

- **Home Page**: Brief introduction and link to the application form.
- **Job Application Form**: Fields for personal details, contact information, resume upload, and additional questions.
- **Submission Confirmation**: A message confirming that the form was successfully submitted.

### 🌈 Color Scheme & Typography

- **Color Scheme**: A professional blue and white palette to maintain a corporate appearance.
- **Typography**: Simple, readable fonts like Arial or Helvetica to ensure accessibility and clarity.

---

## 🚀 Features

### ✅ Implemented Features

- **Responsive Design**: The application adjusts seamlessly for mobile and desktop devices.
- **Form Validation**: Validates inputs to ensure required fields are completed and data is correctly formatted.
- **Data Storage**: Stores applicant details securely in the database.
- **Email Notifications**: Sends confirmation emails to applicants and notification emails to recruiters.

### 🛠️ Planned Improvements

- **Admin Dashboard**: A view for recruiters to filter and manage submitted applications.
- **Search & Filter**: Tools to search and filter applications based on specific criteria.
- **Export Functionality**: Ability to export applicant data into CSV or PDF formats.
- **Authentication**: Secure login for recruiters to access the admin panel.

---

## 💻 Technologies Used

### 🧑‍💻 Languages Used

- **Python**: Server-side logic and backend functionality.
- **HTML/CSS**: Page structure and styling.
- **JavaScript**: Enhancements for form interactivity and validation.

### 📚 Libraries Used

- **Django**: Web framework for handling backend logic and routing.
- **Django Forms**: Simplifies form creation and validation.
- **Django Email**: Sends emails for application confirmations and recruiter notifications.
- **SQLite**: Lightweight database used to store job application data (configurable for other databases like PostgreSQL or MySQL).

---

## 📁 Project Files

- `manage.py`: Main file to interact with the Django project.
- `app/`: The main Django application containing models, views, and templates.
- `templates/`: HTML templates used for rendering web pages.
- `static/`: Static files like CSS, JavaScript, and images.
- `requirements.txt`: List of Python dependencies for the project.
- `README.md`: Documentation and setup instructions for the project.

---

## 🛠 Installation & Usage

### ⚙️ How to Run

1. **Clone the repository**:

```bash
git clone https://github.com/mahmudurmahid/django-job-application-form-web-app.git
cd django-job-application-form-web-app
```

2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Set up environment variables:

```bash
export DJANGO_SETTINGS_MODULE=app.settings
```

5. Apply migrations to set up the database:

```bash
python manage.py migrate
```

6. Run the server:

```bash
python manage.py runserver
```

7. Access the app at http://localhost:8000.

### 🧾 Configuration

Email Settings: You will need to configure your SMTP settings in the settings.py file for email functionality (e.g., for sending application confirmations).

Database Configuration: The app uses SQLite by default, but you can change this to any other database like PostgreSQL by modifying DATABASES in settings.py.

---

## 🔒 Security & Environment Configuration

### 🧑‍💻 Use of python-dotenv

To maintain security and best practices, sensitive configurations (like database credentials, email settings, and other environment variables) are stored in .env files, rather than being hardcoded into the codebase. The python-dotenv package is used to manage these environment variables.

Why python-dotenv?
It keeps sensitive data (like database passwords and API keys) secure and out of version control (e.g., GitHub), helping maintain privacy.

Security Benefits:
This method ensures that sensitive information is not accidentally exposed, especially in production or testing environments.

How It Works:
The .env file is loaded when the app starts up, and environment variables are injected into the settings, where they are used for configuration (e.g., email, database settings).

### 🔧 Setting Up a Forked Repository

1. Install python-dotenv:

```bash
pip install python-dotenv
```

2. Create a .env file in the root directory of your project (same level as manage.py) and add the necessary configurations.

Example .env file:

```bash
DJANGO_SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///db.sqlite3
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-email-password
```

3. Update your settings:

In settings.py, use python-dotenv to load environment variables:

```bash
from dotenv import load_dotenv
load_dotenv()
```

4. Run the application:

```bash
python manage.py runserver
```

---

## ✅ Testing

### 🧪 Test Scenarios Checklist

This project includes several test cases to ensure that the application is working as expected:

| **Feature**                | **Test Type** | **Status** |
| -------------------------- | ------------- | ---------- |
| **Form Field Validation**  | Unit          | ✅ Passed  |
| **Email Notifications**    | Integration   | ✅ Passed  |
| **Database Functionality** | Integration   | ✅ Passed  |
| **Responsive Design**      | Manual        | ✅ Passed  |
| **Error Handling**         | Unit / Manual | ✅ Passed  |

### 🧪 Running Tests

To run tests on your local environment:

1. **Install testing dependencies**:

```bash
pip install pytest
```

Run tests:

```bash
pytest
```

This will run all the tests and output a summary of the results.

---

## 🙌 Credits

### 👨‍💻 Author

This project is developed and maintained by Mahmudur Mahid.

GitHub: [@mahmudurmahid](https://github.com/mahmudurmahid)

### 🧰 Tools & Technologies

The web app utilizes the following tools and technologies:

```plaintext
Tool/Library     Purpose
---------------  --------------------------------------
Python           Core programming language
Django           Web framework for building the app
Django Forms     Form handling and validation
Django Email     Email functionality for notifications
SQLite           Database for storing applications
```

### 📚 Learning Resources & Documentation

The following resources were helpful during the development:

```plaintext
- Django Documentation: https://docs.djangoproject.com/en/stable/
- python-dotenv Documentation: https://pypi.org/project/python-dotenv/
```
