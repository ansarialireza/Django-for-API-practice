# Django for APIs — Practice Repository

This repository contains my solutions, notes, and projects from the book **"Django for APIs (4.0 Edition)"** by *William S. Vincent*.

## 📚 About the Book
The book provides a comprehensive, step-by-step guide to building web APIs using **Django** and **Django REST Framework (DRF)**.  
It covers essential topics such as authentication, permissions, serializers, viewsets, routers, and deployment.

👉 Official site: [https://www.wsvincent.com/](https://www.wsvincent.com/)

---

## 🧠 Purpose
This repo serves as my personal learning log and exercise workspace.  
Each chapter includes:
- Source code of projects and exercises  
- Notes and comments for better understanding  
- Optional improvements or experiments I try along the way  

---

## ⚙️ Setup & Usage
To run any project locally:

```bash
# clone the repo
git clone https://github.com/alireza-ansari/django-for-apis-practice.git

# navigate to a specific project
cd chapter-01-blogapi/

# create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

# run the development server
python manage.py runserver
