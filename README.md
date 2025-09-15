# 🚀 CommandHub – All in One Command & Tool Platform

A centralized platform developed in **Streamlit** to execute, manage, and monitor essential system commands and tools from a user-friendly web interface.

---

## ✅ Project Overview

**CommandHub** allows you to run system commands remotely through a web interface, log the commands, and display outputs in real-time.  
Ideal for DevOps engineers, system administrators, or automation enthusiasts.

---

## ⚡ Features

- Execute system commands securely from a web UI
- Monitor command outputs in real-time
- Log executed commands into a file
- Simple and intuitive Streamlit-based interface
- Lightweight and easy to deploy using Docker

---

## 🚧 Technologies Used

- Python 3.9+
- Streamlit
- Subprocess module
- Docker (for containerized deployment)

---

## 🚀 How to Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/bhushan-yadava/CommandHub-All-In-One-Command-Tool-Platform.git
cd CommandHub-All-In-One-Command-Tool-Platform

```
---
### 2️⃣ Set Up Virtual Environment

python -m venv env
#### Activate environment

#### Windows:

.\env\Scripts\activate

#### Linux/macOS:
source env/bin/activate

### 3️⃣ Install Dependencies
pip install -r requirements.txt


### 4️⃣ Run the Application
streamlit run app.py


👉 Open in browser:
http://localhost:8501

---

---

## 🐳 Run with Docker

#### 1️⃣ Build Docker Image
docker build -t commandhub .

#### 2️⃣ Run Docker Container
docker run -p 8501:8501 commandhub


👉 Access the app at:
http://localhost:8501

---

✅ Folder Structure
CommandHub/
│
├── app.py                  # Main Streamlit application
├── utils.py                # Helper functions
├── requirements.txt        # Python dependencies
├── Dockerfile               # Docker image definition
├── .dockerignore            # Files excluded in Docker build
├── .gitignore               # Files excluded from git
└── commands.log            # Stores command history (generated at runtime)


### ⚡ Future Improvements

Add user authentication

Command history visualization

Pre-defined command templates

Integration with databases for persistent storage

Role-based access control
