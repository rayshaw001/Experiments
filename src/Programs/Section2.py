class Section:
	def __init__(self,type,win):
		self.type=type
		self.window=win

	def pack(self):
		from PIL import ImageTk , Image
		filename = r'../Pics/2-1-info.png'
		if self.type == 2 :
			filename = r'../Pics/2-2-info.png'
		img = Image.open(filename)
		images = ImageTk.PhotoImage(img)
		label = Label(self.window,image=images)
		label.pack()