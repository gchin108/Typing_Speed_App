import tkinter as tk
from tkinter import *
from words import programming_facts
from random import choice
import time

word = ['apple', 'orange', 'elephant']


class Typing:
    def __init__(self):
        self.root = Tk()
        self.root.title('Typing Speed App')
        self.root.geometry('800x600')
        self.current_sentence = ""
        self.start_time = 0
        self.total_time = 0
        self.correct_words = 0
        self.typing_started = False

        self.sentence_label = Label(self.root, text="", font=('Helvetica', 16), wraplength=600, pady=60)
        self.sentence_label.pack()
        self.text_field = Text(self.root, font=('Helvetica', 16), height=2)
        self.text_field.pack()
        self.text_field.focus_set()
        self.wpm = Label(self.root, text="Type the sentence and press enter", font=('Helvetica', 16))
        self.wpm.pack()
        self.time = Label(self.root, text="", font=('Helvetica', 16))
        self.time.pack()

        self.root.bind('<Return>', self.check_entries)
        self.root.bind('<space>', self.word_check)
        self.root.bind('<Key>', self.start_typing)

        self.new_sentence()

    def start_typing(self, event):
        if not self.typing_started:
            self.start_time = time.time()
            self.typing_started = True

    def display_sentence(self):
        self.current_sentence = choice(programming_facts)
        return self.current_sentence

    def new_sentence(self):

        if self.current_sentence != choice(programming_facts):
            self.current_sentence = choice(programming_facts)
            self.sentence_label.config(text=self.current_sentence)
            self.typing_started = False
        else:
            self.current_sentence = choice(programming_facts)
            self.sentence_label.config(text=self.current_sentence)
            self.typing_started = False

    def check_entries(self, event):
        if self.text_field.get(1.0, 'end-1c').strip() == self.current_sentence:
            self.text_field.delete(1.0, tk.END)
            self.check_time()
            self.new_sentence()
        else:
            self.wpm.config(text='Incorrect. Try again')

    def check_time(self):
        end_time = time.time()
        time_taken = round(end_time - self.start_time, 2)
        self.time.config(text=f'Took = {time_taken}s')
        self.total_time += time_taken
        self.correct_words += len(self.current_sentence.split())
        wpm = round((self.correct_words / self.total_time) * 60)
        self.wpm.config(text=f'Wpm = {wpm}')

    def word_check(self, event):
        entered_text = self.text_field.get(1.0, "end-1c")  # Get text from text widget
        entered_words = entered_text.split()
        sentence_words = self.current_sentence.split()
        if entered_words[-1] == sentence_words[len(entered_words) - 1]:  # Check last word entered
            self.text_field.tag_remove('incorrect', '1.0', 'end')
            self.text_field.tag_add('correct', '1.0', 'end')
            self.text_field.tag_config('correct', background="white", foreground="green")
        else:
            self.text_field.tag_remove('correct', '1.0', 'end')
            self.text_field.tag_add('incorrect', '1.0', 'end')
            self.text_field.tag_config('incorrect', background="white", foreground="red")


app = Typing()
app.root.mainloop()
