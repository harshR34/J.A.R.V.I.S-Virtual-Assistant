import tkinter as tk
from tkinter import scrolledtext
import pyttsx3
import speech_recognition as sr


class VoiceAssistantGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Voice Assistant")
        self.engine = pyttsx3.init()

        # Create a text area for displaying conversations
        self.text_area = scrolledtext.ScrolledText(self.root, width=40, height=10, wrap=tk.WORD)
        self.text_area.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        # Create buttons
        self.btn_listen = tk.Button(self.root, text="Listen", command=self.listen)
        self.btn_listen.grid(row=1, column=0, padx=10, pady=5)

        self.btn_stop = tk.Button(self.root, text="Stop", command=self.stop_listening)
        self.btn_stop.grid(row=1, column=1, padx=10, pady=5)

        # Initialize recognizer
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def speak(self, text):
        self.text_area.insert(tk.END, f"Assistant: {text}\n")
        self.engine.say(text)
        self.engine.runAndWait()

    def listen(self):
        with self.microphone as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.text_area.insert(tk.END, "Listening...\n")
            audio = self.recognizer.listen(source)

        try:
            query = self.recognizer.recognize_google(audio)
            self.text_area.insert(tk.END, f"You: {query}\n")
            # Here you can add your logic to process the query
            self.speak("You said: " + query)
        except sr.UnknownValueError:
            self.text_area.insert(tk.END, "Assistant: Sorry, I could not understand that.\n")
        except sr.RequestError:
            self.text_area.insert(tk.END, "Assistant: There was an error processing your request.\n")

    def stop_listening(self):
        self.recognizer.stop_listening()


# Create the main window
root = tk.Tk()
app = VoiceAssistantGUI(root)
root.mainloop()
