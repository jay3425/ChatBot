import tkinter as tk
from tkinter import scrolledtext
from groq import Groq
from json import load, dump
import datetime
from dotenv import dotenv_values

# Load environment variables from the .env file.
env_vars = dotenv_values(".env")

Username = env_vars.get("Username")
Assistantname = env_vars.get("Assistantname")
GroqAPIKey = env_vars.get("GroqAPIKey")

client = Groq(api_key=GroqAPIKey)

messages = []

System = f"""Hello, I am {Username}, You are a very accurate and advanced AI ChatBot named {Assistantname} which also has real-time up-to-date information from the internet.
*** Do not tell time until I ask, do not talk too much, just answer the question.***
*** Reply in only English, even if the question is in Hindi, reply in English.***
*** Do not provide notes in the output, just answer the question and never mention your training data. ***
"""

SystemChatBot = [
    {"role": "system", "content": System}
]

def RealtimeInformation():
    current_date_time = datetime.datetime.now()
    day = current_date_time.strftime("%A")
    date = current_date_time.strftime("%d")
    month = current_date_time.strftime("%B")
    year = current_date_time.strftime("%Y")
    hour = current_date_time.strftime("%H")
    minute = current_date_time.strftime("%M")
    second = current_date_time.strftime("%S")

    data = f"Please use this real-time information if needed,\n"
    data += f"Day: {day}\nDate: {date}\nMonth: {month}\nYear: {year}\n"
    data += f"Time: {hour} hours :{minute} minutes: {second} second.\n"
    return data

def AnswerModifier(Answer):
    lines = Answer.split('\n')
    non_empty_lines = [line for line in lines if line.strip()]
    modified_answer = '\n'.join(non_empty_lines)
    return modified_answer

def ChatBot(Query):
    try:
        with open(r"ChatLog.json", "r") as f:
            messages = load(f)

        messages.append({"role": "user", "content": f"{Query}"})

        completion = client.chat.completions.create(
            model="llama3-70b-8192",
            messages=SystemChatBot + [{"role": "system", "content": RealtimeInformation()}] + messages,
            max_tokens=1024,
            temperature=0.7,
            top_p=1,
            stream=True,
            stop=None
        )

        Answer = ""

        for chunk in completion:
            if chunk.choices[0].delta.content:
                Answer += chunk.choices[0].delta.content

        Answer = Answer.replace("</s>", "")

        messages.append({"role": "assistant", "content": Answer})

        with open(r"ChatLog.json", "w") as f:
            dump(messages, f, indent=4)

        return AnswerModifier(Answer=Answer)
    
    except Exception as e:
        print(f"Error: {e}")
        with open(r"ChatLog.json", "w") as f:
            dump([], f, indent=4)
        return ChatBot(Query)

def send_message():
    message = entry.get()
    if message.strip():
        chat_box.config(state=tk.NORMAL)
        chat_box.insert(tk.END, "You: " + message + "\n", "user")
        entry.delete(0, tk.END)
        response = ChatBot(message)
        chat_box.insert(tk.END, "Bot: " + response + "\n", "bot")
        chat_box.config(state=tk.DISABLED)
        chat_box.yview(tk.END)

def clear_chat():
    chat_box.config(state=tk.NORMAL)
    chat_box.delete('1.0', tk.END)
    chat_box.config(state=tk.DISABLED)

# Create the main window
root = tk.Tk()
root.title("ChatBot")
root.state("zoomed")
root.configure(bg="#222831")

# Top label
label = tk.Label(root, text="Welcome to ChatBot", font=("Arial", 14, "bold"), bg="#00ADB5", fg="white")
label.pack(pady=5)

# Chat display
chat_box = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=90, height=30, bg="#EEEEEE", fg="#393E46", font=("Arial", 12))
chat_box.pack(pady=10, padx=10)
chat_box.tag_config("user", foreground="blue")
chat_box.tag_config("bot", foreground="green")
chat_box.config(state=tk.DISABLED)

# Input field
entry_frame = tk.Frame(root, bg="#222831")
entry_frame.pack(pady=5)
entry = tk.Entry(entry_frame, width=86, font=("Arial", 12), bg="#EEEEEE", fg="#393E46")
entry.pack(side=tk.LEFT, padx=5)

# Send button
send_button = tk.Button(entry_frame, text="Send", command=send_message, bg="#00ADB5", fg="white", font=("Arial", 12, "bold"))
send_button.pack(side=tk.RIGHT)

# Clear button
clear_button = tk.Button(root, text="Clear Chat", command=clear_chat, bg="#FF5722", fg="white", font=("Arial", 12, "bold"))
clear_button.pack(pady=5)

# Run the application
root.mainloop()
