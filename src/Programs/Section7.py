class Section:
	def __init__(self,win):
		self.window=win
	def pack():
		from PIL import ImageTk , Image
		filename = r'../Pics/7-partner.png'
		img = Image.open(filename)
		images = ImageTk.PhotoImage(img)
		label = Label(self.window,image=images)
		label.pack()
		#获取数据
		return 0
