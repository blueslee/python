from tkinter import *

class Alarm(Frame):
	def __init__(self):
		Frame.__init__(self)
		self.pack()
		stopper = Button(self, text='stop me', command = self.quit)
		stopper.pack()
		stopper.config(bg="navy", fg="white", bd=8)
		self.stopper = stopper
		self.repeater()

	def repeater(self):
		self.bell()
		self.stopper.flash()

Alarm().mainloop()
