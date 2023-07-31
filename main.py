import tkinter as tk
import random
import time
from words import programming_facts


# List of sample sentences for the speed typing test

class SpeedTypingTest:
    def __init__(self, root):
        self.root = root
        self.root.geometry('800x600')
    
        self.root.title('Speed Typing Test')
        self.root.configure(bg='black')
        self.current_sentence = ""
        self.start_time = 0
        self.total_time = 0
        self.correct_words = 0
        self.typing_started = False

        self.sentence_label = tk.Label(self.root, text="", font=('Helvetica', 16), wraplength=600, bg='black', fg='green')
        self.sentence_label.pack(pady=60)

        self.text_widget = tk.Text(self.root, font=('Helvetica', 16), height=2, bg='black', fg='green', insertbackground='white', borderwidth=0, highlightthickness=0)
        self.text_widget.pack(pady=60)
        self.text_widget.focus_set()

        self.result_label = tk.Label(self.root, text="Type the sentence and press enter", font=('Helvetica', 16), bg='black', fg='green')
        self.result_label.pack()

        self.wpm_label = tk.Label(self.root, text="Your Words Per Minute will be shown here", font=('Helvetica', 16), bg='black', fg='green')
        self.wpm_label.pack()

        self.root.bind('<space>', self.word_check)
        self.root.bind('<Return>', self.check_entry)
        self.root.bind('<Key>', self.start_typing)

        self.new_sentence()

    def new_sentence(self):
        new_sentence = random.choice(programming_facts)
        while new_sentence == self.current_sentence:
            new_sentence = random.choice(programming_facts)
        self.current_sentence = new_sentence
        self.sentence_label.config(text=self.current_sentence)
        self.typing_started = False

    def start_typing(self, event):
        if not self.typing_started:
            self.start_time = time.time()
            self.typing_started = True

    def check_entry(self, event):
        entered_text = self.text_widget.get(1.0, "end-1c")  # Get text from text widget
        if entered_text.strip() == self.current_sentence:
            end_time = time.time()
            time_taken = round(end_time - self.start_time, 2)  # Time in seconds
            self.total_time += time_taken
            self.correct_words += len(self.current_sentence.split())
            wpm = round((self.correct_words / self.total_time) * 60)  # Formula for WPM
            self.result_label.config(text=f'Correct! Time taken: {time_taken} seconds')
            self.wpm_label.config(text=f'Your WPM: {wpm}')
            self.text_widget.delete(1.0, tk.END)  # Clear text widget
            self.new_sentence()
        else:
            self.result_label.config(text='Incorrect! Try again.')
            self.text_widget.delete(1.0, tk.END)

    def word_check(self, event):
        entered_text = self.text_widget.get(1.0, "end-1c")  # Get text from text widget
        entered_words = entered_text.split()
        sentence_words = self.current_sentence.split()
        if entered_words[-1] == sentence_words[len(entered_words) - 1]:  # Check last word entered
            self.text_widget.tag_remove('incorrect', '1.0', 'end')
            self.text_widget.tag_add('correct', '1.0', 'end')
            self.text_widget.tag_config('correct', background="black", foreground="green")
        else:
            self.text_widget.tag_remove('correct', '1.0', 'end')
            self.text_widget.tag_add('incorrect', '1.0', 'end')
            self.text_widget.tag_config('incorrect', background="black", foreground="red")


root = tk.Tk()
SpeedTypingTest(root)
root.mainloop()
