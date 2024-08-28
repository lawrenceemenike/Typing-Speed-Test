import tkinter as tk
from tkinter import messagebox
import random
import time

class TypingSpeedTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Speed Test")
        self.master.geometry("600x400")

        self.sample_texts = [
            "The quick brown fox jumps over the lazy dog.",
            "Python is a versatile programming language.",
            "Practice makes perfect when it comes to typing.",
            "Coding is both an art and a science.",
            "The Internet has revolutionized communication."
        ]

        self.current_text = ""
        self.start_time = 0
        self.is_test_running = False

        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Type the text below:", font=("Arial", 12))
        self.instruction_label.pack(pady=10)

        self.text_display = tk.Label(self.master, text="", font=("Arial", 14), wraplength=500)
        self.text_display.pack(pady=20)

        self.entry = tk.Entry(self.master, font=("Arial", 14), width=50, state="disabled")
        self.entry.pack(pady=10)
        self.entry.bind("<KeyPress>", self.start_test)

        self.result_label = tk.Label(self.master, text="", font=("Arial", 12))
        self.result_label.pack(pady=20)

        self.button_frame = tk.Frame(self.master)
        self.button_frame.pack(pady=10)

        self.start_button = tk.Button(self.button_frame, text="Start New Test", command=self.new_test)
        self.start_button.pack(side=tk.LEFT, padx=10)

        self.complete_button = tk.Button(self.button_frame, text="Complete Test", command=self.end_test, state="disabled")
        self.complete_button.pack(side=tk.LEFT, padx=10)

    def new_test(self):
        self.current_text = random.choice(self.sample_texts)
        self.text_display.config(text=self.current_text)
        self.entry.config(state="normal")
        self.entry.delete(0, tk.END)
        self.result_label.config(text="")
        self.is_test_running = False
        self.start_time = 0
        self.complete_button.config(state="disabled")

    def start_test(self, event):
        if not self.is_test_running:
            self.start_time = time.time()
            self.is_test_running = True
            self.complete_button.config(state="normal")

    def end_test(self):
        if not self.is_test_running:
            messagebox.showinfo("Error", "Please start a new test first.")
            return

        end_time = time.time()
        elapsed_time = end_time - self.start_time
        user_text = self.entry.get()
        
        words = self.current_text.split()
        user_words = user_text.split()
        correct_words = sum(1 for user_word, correct_word in zip(user_words, words) if user_word == correct_word)
        
        wpm = (correct_words / elapsed_time) * 60

        result = f"Your typing speed: {wpm:.2f} WPM\n"
        result += f"Accuracy: {(correct_words / len(words)) * 100:.2f}%"
        
        self.result_label.config(text=result)
        self.entry.config(state="disabled")
        self.is_test_running = False
        self.complete_button.config(state="disabled")

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTest(root)
    root.mainloop()