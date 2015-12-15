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
		# Title
		self.root.wm_title("BER Curves")
		self.root.geometry("%dx%d+0+0" % (self.w, self.h))
		# Variables required from Bit Sequence Selection
		self.bit_sequence = None # Bit Sequence Variable
		self.setup_bit_sequence()
		# Variables required from simulation control
		self.snr = None # Signal to Noise variable
		self.error_bits = None # Error bits variable
		self.setup_simulation_control()
		# Variables required from Channel Noise
		self.gaussian = None # Gaussian Noise Variable (Yes/No)
		self.burst_frequency = None # Burst Frequency Variable
		self.burst_error = None # Burst Error Variable
		self.setup_channel_noise()

	def run_program(self):
		self.graph()
		print self.error_bits.get()
		#output1 = Generate(input)
		#output2 = Modulate(input)
		#output3 = Coding(input)
		#output4 = Noise(input)
		#output5 = SNR(i.get())
			
	def graph(self):
		# simple graph for place holder
		f = Figure(figsize=(5, 4), dpi=100)
		a = f.add_subplot(111)
		t = (1, 2, 3, 4)
		s = (1, 2, 3, 4)
		canvas = FigureCanvasTkAgg(f, root)
		canvas.show()
		canvas.get_tk_widget().grid(row=5)
		a.plot(t, s)
		
	def setup_bit_sequence(self):
		# Bit Sequences		
		row = 0
		bit_sequence_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady=15, padx=10)
		bit_sequence_frame.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		bit_sequence_label = Tk.Label(bit_sequence_frame, text = "Bit Sequences", font=("Helvetica", 14)).grid(row = row, column = 0, columnspan = 2, pady = 15, padx = 50)
		row += 1
		# Sequence Selection
		self.bit_sequence = Tk.StringVar()
		self.bit_sequence.set("Default Sequence")
		bit_sequence_menu = Tk.OptionMenu(bit_sequence_frame, self.bit_sequence, "Sequence 1", "Sequence 2", "Sequence 3", "Other").grid(row = row, columnspan = 2, pady = 15)

	def setup_simulation_control(self):
		row = 3
		# Section Title
		simulate_label = Tk.Label(root, text="Simulation Control").grid(row=row, column=0)
		row += 1
		# Error bits inupt
		lb1 = Tk.Label(root, text="Error Bits").grid(row=row, sticky=W)
		row += 1
		self.error_bits = Tk.IntVar()
		self.error_bits.set(0)
		err_input = Tk.Entry(root, width=10, textvariable=self.error_bits).grid(row=row, sticky=W)
		row += 1
		# Noise Type selection box
		self.snr = Tk.StringVar()
		self.snr.set("Default SNR")
		snr_menu = Tk.OptionMenu(root, self.snr, "one", "two", "three", "etc").grid(row=row, sticky=W)
		row += 1
		# Button to run program
		run = Tk.Button(root, text="Run", command=self.run_program).grid(row=row, sticky=W)

	def	setup_channel_noise(self):
		# Channel Noise
		row = 0
		channel_noise_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady= 15, padx=10)
		channel_noise_frame.grid(row = 0, column = 2, rowspan = 5, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		channel_noise_label = Tk.Label(channel_noise_frame, text = "Channel Noise", font=("Helvetica", 14)).grid(row = row, column = 2, columnspan = 2, pady = 15, padx = 50)
		row += 1
		# Gaussian Checkbox
		self.gaussian = Tk.IntVar()
		self.gaussian.set(0)
		gaussian_checkbox = Tk.Checkbutton(channel_noise_frame, text="  Gaussian", font=("Helvetica", 12), variable = self.gaussian).grid(row = row, column = 2, columnspan = 2)
		row += 1
		# Burst Noise Input
		burst_noise_label = Tk.Label(channel_noise_frame, text = "Burst", font=("Helvetica", 12)).grid(row = row, column = 2, columnspan = 2, pady = 15)
		row += 1
		self.burst_frequency = Tk.IntVar()
		self.burst_frequency.set(0)
		self.burst_error = Tk.IntVar()
		self.burst_error.set(0)
		burst_frequency_label = Tk.Label(channel_noise_frame, text = "Frequency").grid(row = row, column = 2)
		burst_error_label = Tk.Label(channel_noise_frame, text = "Error").grid(row = row, column = 3)
		row+=1
		burst_frequency_input = Tk.Entry(channel_noise_frame, width=10, textvariable=self.burst_frequency).grid(row = row, column = 2)
		burst_error_input = Tk.Entry(channel_noise_frame, width=10, textvariable=self.burst_error).grid(row = row, column = 3)
		
root = Tk.Tk()
a = GUI(root)
root.mainloop()

