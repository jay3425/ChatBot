
# 🤖 Jarvis - AI ChatBot with Python & Tkinter

**Jarvis** is an AI-powered chatbot built using Python, integrating a graphical user interface (GUI) via Tkinter and powered by the Groq LLM API. Designed as part of a college project, this application provides a clean, interactive experience for users to engage in real-time conversations with a smart assistant.

---

## 🚀 Features

- 🌐 Real-time conversational AI using Groq’s LLaMA-3 model
- 💬 Persistent chat history stored in JSON
- 🕒 Dynamic integration of real-time system date and time
- 🎨 GUI designed with Tkinter for user-friendly interaction
- 🔐 Environment variables managed with `.env` for secure config

---

## 🧱 Project Structure

```

├── Chatbot.py         # Main application logic and GUI
├── ChatLog.json       # Stores conversation history
├── .env               # Environment configuration (API keys and settings)

````

---

## 🛠️ Technologies Used

- **Python 3.x**
- **Groq API** (LLaMA3 model)
- **Tkinter** (GUI Framework)
- **python-dotenv** (Environment Variable Management)
- **JSON** (Data persistence)

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
````

### 2. Install Required Packages

```bash
pip install python-dotenv groq
```

### 3. Configure the Environment

Create a `.env` file in the root directory and add:

```
Username=Jay
Assistantname=Jarvis
GroqAPIKey=your_groq_api_key
InputLanguage=en
```

> ⚠️ **Never share your `.env` file publicly.**

### 4. Run the Application

```bash
python Chatbot.py
```

---

## 📸 UI Preview

> ![]()

---

## 📌 Notes

* The chatbot is configured to **respond only in English**, regardless of input language.
* Includes logic to avoid unnecessary chatter or time display unless explicitly asked.
* Suitable as a foundational AI project for students and enthusiasts.

---

## Author - Jay dengle

This project is part of my portfolio, showcasing my Python development and chatbot integration skills using APIs and UI frameworks. It's designed to simulate real-world AI interaction, highlighting my abilities in GUI design, API usage, and conversational logic—skills essential for software development and AI-focused roles.  
If you have any questions, feedback, or would like to collaborate, feel free to get in touch!


### Stay Updated and Join me

- **GMail**: [jaydengle2005@gmail.com](mailto:jaydengle2005@gmail.com)
- **Instagram**: [Follow me]()
- **LinkedIn**: [Connect with me professionally](https://www.linkedin.com/in/jay-anil-dengle-049952337/)

Thank you, and I look forward to connecting with you!
