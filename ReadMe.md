# EduBot

## Overview

This project is a simple web application built with Flask that allows users to interact with the OpenAI API through a web interface. Users can send messages and receive responses from the OpenAI model.

## Features

- Simple web interface for chat interactions.
- Uses the OpenAI GPT-4 model to generate responses.
- Flask backend to handle API requests and responses.
- HTML, CSS, and JavaScript for the frontend.

## Prerequisites

- Python 3.x
- Flask
- OpenAI Python client

## Installation

### Step 1: Clone the Repository

```bash
git clone https://github.com/PrinceAsiedu/flask-openai.git
cd flask-openai
```

### Step 2: Set Up a Virtual Environment 

- Create a virtual environment to manage dependencies:

```bash
python -m venv myenv
```

- Activate the virtual environment:

Windows

```bash
myenv\Scripts\activate
```

macOS/Linux:

```bash
source myenv/bin/activate
```

### Step 3: Install the Project Dependencies.

```bash  
pip install -r requirements.txt
```

### Step 4: Set Up OpenAI API Key

1. Create an account on OpenAI.
2. Generate an API key from the OpenAI dashboard.
3. Store your 'OPENAI_API_KEY' as an enviromental variable. There are different ways for doing this on linux, windows and macOS.

### Step 5: Start the Flask Application

Ensure your virtual environment is activated, then run the Flask app:

```bash
python3 app.py
```

### Step 6: Access the Web Interface

Open your web browser and go to `http://127.0.0.1:5000/`. You should see the chat interface where you can enter a message and get a response from the OpenAI model.
