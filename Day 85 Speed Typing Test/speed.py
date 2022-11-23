import tkinter
from tkinter.messagebox import showinfo
import time
from settings import GUISettings
import requests
import secrets

# We create the main window #

class UI(tkinter.Tk):
	def __init__(self, ):
		super(UI, self).__init__()
		self.count=0
		self.request = requests.get('https://random-word-api.herokuapp.com/word?number=100')
		self.dictionairy= self.request.json()
		self.random_word= secrets.choice(self.dictionairy).strip('"[]')
		self.title(GUISettings.MAIN_WINDOW_TITLE)
		self.config(
			padx=GUISettings.BUTTON_PADDING_X,
			pady=GUISettings.BUTTON_PADDING_Y
		)
		self.resizable(False, False)
		self.create_buttons()
		self.bind("<Up>", lambda e: self.check_word())
		self.bind("<Down>", lambda e: self.calculate_wpm())

	def malakas(self):
		print('malakasssss')

	def create_buttons(self) -> None:
		""" Creates the three buttons 1. Start 2. Stop 3.Submit """
		self.entry_one = tkinter.Entry(bg=GUISettings.WHITE, width=30, justify='center')
		self.entry_one.grid(row=4, column=1)
		self.button_start = tkinter.Button(
			text=GUISettings.BUTTON_START_TEXT,
			padx=GUISettings.BUTTON_PADDING_X,
			pady=GUISettings.BUTTON_PADDING_Y,
			command= lambda:[self.create_labels(), self.set_first_timer()]
		)
		self.button_start.grid(
			row=2,
			column=1,
		)
		self.button_stop = tkinter.Button(
			text=GUISettings.BUTTON_STOP_TEXT,
			padx=GUISettings.BUTTON_PADDING_X,
			pady=GUISettings.BUTTON_PADDING_Y,
			command=lambda:self.calculate_wpm(),
			state='disabled'
		)
		self.button_stop.grid(
			row=2,
			column=3,
		)
		self.button_submit = tkinter.Button(
			text=GUISettings.BUTTON_SUBMIT_TEXT,
			padx=GUISettings.BUTTON_PADDING_X,
			pady=GUISettings.BUTTON_PADDING_Y,
			command=lambda: self.check_word()
		)
		self.button_submit.grid(
			row=4,
			column=3,
		)


	def create_labels(self) -> None:
		self.random_word = secrets.choice(self.dictionairy).strip('"[]')
		self.word_label = tkinter.Label(text=self.random_word, padx=10)
		self.word_label.grid(row=3, column=1)
		self.enable_stop_button()
		self.disable_start_button()


	def set_first_timer(self):
		self.timer1 = time.time()


	def check_word(self) -> None:
		self.user_input = self.entry_one.get()
		if self.user_input == self.random_word:
			self.count = self.count + 1
			self.create_labels()
			self.clear_text()

	def calculate_wpm(self):
		self.timer2 = time.time()
		self.time = (self.timer2-self.timer1)/float(60)
		self.total_wpm = float(self.count)/self.time
		self.popup_showinfo(round(self.total_wpm))
		print(self.total_wpm)

	def popup_showinfo(self, wpm):
		showinfo("Window", f"Your WPM is : \n {wpm}")


	def clear_text(self):
		self.entry_one.delete(0, tkinter.END)

	def enable_stop_button(self) -> None:
		self.button_stop.config(state='active')

	def disable_start_button(self) -> None:
		self.button_start.config(state='disabled')