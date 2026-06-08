# AI Email Deadline Alert System

## Project Overview

AI Email Deadline Alert System automatically detects deadline-related emails and reminds users before the due time.

The project combines Machine Learning and traditional programming to reduce the risk of missing assignments, meetings, submissions, and office tasks.

---

## Purpose

To automatically notify users about deadlines mentioned in emails a few hours or even a day before the due time, ensuring they are reminded even if the email was never opened or checked.

---

## Problem Statement

Students and office workers receive many emails daily.

Important deadline emails can easily be missed because:

* Inboxes become crowded
* Users forget to check emails
* Deadlines are noticed too late

As a result, assignments, meetings, and important tasks may be missed.

---

## Solution

The system automatically:

1. Reads incoming emails
2. Uses Machine Learning to detect deadline-related emails
3. Extracts date and time information
4. Stores tasks in SQLite database
5. Schedules reminders
6. Displays popup deadline alerts

---

## Key Idea

### Traditional Programming (70–80%)

Used for:

* Gmail connection
* Email reading
* Date extraction
* Reminder scheduling
* Database management
* Popup notifications

### Machine Learning (20–30%)

Used for:

* Email classification
* Detecting deadline-related emails
* Ignoring irrelevant emails

Classification:

* Deadline Related
* Non-Deadline Related

This makes the system faster and more efficient.

---

## Technologies Used

* Python
* Pandas
* Scikit-Learn
* Logistic Regression
* TF-IDF Vectorization
* SQLite
* Tkinter
* Gmail IMAP

---

## Project Workflow

Email Received

↓

Machine Learning Classification

↓

Deadline Detection

↓

Task Storage (SQLite)

↓

Reminder Scheduling

↓

Popup Alert

---

## Files

### main.ipynb

Contains complete source code.

### email_dataset_1000.csv

Training dataset used by the machine learning model.

### requirements.txt

Python package dependencies.

---

## Gmail Setup

To connect your Gmail account:

### Step 1

Enable Two-Factor Authentication on your Google account.

### Step 2

Open:

Google Account

↓

Security

↓

App Passwords

### Step 3

Create a new App Password.

Copy the generated password.

### Step 4

Replace:

GMAIL_EMAIL = "[your_email@gmail.com](mailto:your_email@gmail.com)"

GMAIL_APP_PASSWORD = "your_app_password"

inside the source code.

### Step 5

Enable IMAP

Open Gmail

↓

Settings

↓

See all settings

↓

Forwarding and POP/IMAP

↓

Enable IMAP

↓

Save Changes

---

## Features

* Automatic email monitoring
* Machine Learning filtering
* Deadline extraction
* SQLite storage
* Smart reminder scheduling
* Popup alerts
* Duplicate task prevention

---

## Future Improvements

* Deep Learning email classification
* Calendar integration
* SMS notifications
* Mobile application
* Cloud deployment

---

## Author

Naveed Raza

BS Artificial Intelligence Student

Pakistan > Sindh > Sukkur > Pano Akil
