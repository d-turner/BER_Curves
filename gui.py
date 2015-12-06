import matplotlib
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import sys
if sys.version_info[0] < 3:
    import Tkinter as Tk
else:
    import tkinter as Tk
#import Generate
#import Modulation
#import Coding
#import Noise
#import SNR
matplotlib.use('TkAgg')
W = Tk.W
class GUI:
	def __init__(self, master):
		self.root = master
		self.w, self.h = self.root.winfo_screenwidth(), self.root.winfo_screenheight()
		row = 0
		# Title
		self.root.wm_title("BER Curves")
		self.root.geometry("%dx%d+0+0" % (self.w, self.h))
		# Setion Title
		simulate_label = Tk.Label(root, text="Simulation Control").grid(row=row, column=0)
		row += 1
		# Error bits inupt
		self.lb1 = Tk.Label(root, text="Error Bits").grid(row=row, sticky=W)
		row += 1
		self.error_bits = Tk.IntVar()
		self.error_bits.set(0)
		self.err_input = Tk.Entry(root, width=10, textvariable=self.error_bits).grid(row=row, sticky=W)
		row += 1
		# Noise Type selection box
		snr = Tk.StringVar()
		snr.set("Default SNR")
		snr_step = Tk.OptionMenu(root, snr, "one", "two", "three", "etc")
		snr_step.grid(row=row, sticky=W)
		row += 1
		# Button to run program
		run = Tk.Button(root, text="Run", command=self.run_program).grid(row=row, sticky=W)

	def run_program(self):
		self.graph()
		print self.error_bits.get()
		#output1 = Generate(input)
		#output2 = Modulate(input)
		#output3 = Coding(input)
		#output4 = Noise(input)
		#output5 = SNR(i.get())
			
	def graph(self):
		f = Figure(figsize=(5, 4), dpi=100)
		a = f.add_subplot(111)
		t = (1, 2, 3, 4)
		s = (1, 2, 3, 4)
		canvas = FigureCanvasTkAgg(f, root)
		canvas.show()
		canvas.get_tk_widget().grid(row=5)
		a.plot(t, s)
		
root = Tk.Tk()
a = GUI(root)
root.mainloop()

