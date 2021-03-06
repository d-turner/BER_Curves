import matplotlib
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2TkAgg
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
		self.burst = None
		self.burst_frequency = None # Burst Frequency Variable
		self.burst_duration = None # Burst Error Variable
		self.setup_channel_noise()
		# Variable required from Modulation
		self.modtype = None # Modulation type variable
		self.modlevel = None
		self.codetype = None # Line Coding variable
		self.fec = None
		self.interleave = None
		self.setup_modulation_control()
		self.calculate = None
		self.hold = None 
		self.options = { 
					'FrameSize': 1024,
					'Polynomial Number': 5, 		# Options: 0 - 17
					'Burst Frequency': 5,			# Value : 1 - 10
					'Duration': 2,					# In milleseconds 
					'Modulation Code': 0,			# GRAY = 0 | LINEAR = 1
					'Modulation Levels': 64,		# 0 <= value <=  1025
					'Gaussian': True,
					'Modulation Type': 1,			# PSK = 2 | QAM = 3
					'FEC Enabled': True			# true | false
					}

	def run_program(self):
		self.plotConstellationCurve()
		self.plotBERcurve()
		self.options['Polynomial Number'] = self.bit_sequence.get()
		self.options['Burst Frequency'] = self.burst_frequency.get()
		self.options['Duration'] = self.burst_duration.get()
		self.options['Modulation Code'] = self.codetype.get()
		self.options['Modulation Levels'] = self.modlevel.get()
		self.options['Gaussian'] = self.gaussian.get()
		self.options['Modulation Type'] = self.modtype.get()
		self.options['FEC Enabled'] = self.fec.get()
		
	def setup_bit_sequence(self):
		# Bit Sequences		
		row = 0
		bit_sequence_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady=10, padx=10)
		bit_sequence_frame.grid(row = 0, column = 0, rowspan = 2, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		bit_sequence_label = Tk.Label(bit_sequence_frame, text = "Bit Sequences", font=("Helvetica", 14)).grid(row = row, column = 0, columnspan = 2, pady = 10, padx = 60)
		row += 1
		# Sequence Selection
		self.bit_sequence = Tk.StringVar()
		self.bit_sequence.set("Default Sequence")
		bit_sequence_menu = Tk.OptionMenu(bit_sequence_frame, self.bit_sequence, "x^2 + x + 1",
		    "x^3 + x^2 + 1",
		    "x^4 + x^3 + 1",
		    "x^5 + x^3 + 1",
		    "x^6 + x^5 + 1",
		    "x^7 + x^6 + 1",
		    "x^8 + x^6 + x^5 + x^4 + 1",
		    "x^9 + x^5 + 1",
		    "x^10 + x^7 + 1",
		    "x^11 + x^9 + 1",
		    "x^12 + x^11 + x^10 + x^4 + 1",
		    "x^13 + x^12 + x^11 + x^8 + 1",
		    "x^14 + x^13 + x^12 + x^2 + 1",
		    "x^15 + x^14 + 1",
		    "x^16 + x^14 + x^13 + x^11 + 1",
		    "x^17 + x^14 + 1",
		    "x^18 + x^11 + 1",
		    "x^19 + x^18 + x^17 + x^14 + 1").grid(row = row, columnspan = 2, pady = 10, padx = 10)

	def setup_simulation_control(self):
		row = 12
		sim_control_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady=10, padx=10)
		sim_control_frame.grid(row = row, column = 0, rowspan = 4, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		simulate_label = Tk.Label(sim_control_frame, text="Simulation Control", font=("Helvetica", 14)).grid(row = row, column = 0, columnspan = 2, pady = 10, padx = 50)
		row += 1
		# Error bits inupt
		lb1 = Tk.Label(sim_control_frame, text="Error Bits").grid(row=row, column = 0)
		self.error_bits = Tk.IntVar()
		self.error_bits.set(0)
		err_input = Tk.Entry(sim_control_frame, width=10, textvariable=self.error_bits).grid(row=row, column = 1)
		row += 1
		# Noise Type selection box
		self.snr = Tk.StringVar()
		self.snr.set("Default SNR")
		snr_menu = Tk.OptionMenu(sim_control_frame, self.snr, "one", "two", "three", "etc").grid(row=row, column = 0, pady= 10)
		# Button to run program
		run = Tk.Button(sim_control_frame, text="Run", command=self.run_program, bg = "cyan").grid(row=row, column = 1, pady= 10)

	def	setup_channel_noise(self):
		# Channel Noise
		row = 2
		channel_noise_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady= 10, padx=10)
		channel_noise_frame.grid(row = row, column = 0, rowspan = 5, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		channel_noise_label = Tk.Label(channel_noise_frame, text = "Channel Noise", font=("Helvetica", 14)).grid(row = row, column = 2, columnspan = 2, pady = 10, padx = 50)
		row += 1
		# Gaussian Checkbox
		self.gaussian = Tk.IntVar()
		self.gaussian.set(0)
		gaussian_checkbox = Tk.Checkbutton(channel_noise_frame, text="  Gaussian", font=("Helvetica", 12), variable = self.gaussian).grid(row = row, column = 2, columnspan = 2)
		row += 1

		# Burst Noise Input
		burst_noise_label = Tk.Label(channel_noise_frame, text = "Burst", font=("Helvetica", 12)).grid(row = row, column = 2, columnspan = 2, pady = 10)
		row += 1
		self.burst_frequency = Tk.IntVar()
		self.burst_frequency.set(0)
		self.burst_duration = Tk.IntVar()
		self.burst_duration.set(0)
		burst_frequency_label = Tk.Label(channel_noise_frame, text = "Frequency").grid(row = row, column = 2)
		burst_duration_label = Tk.Label(channel_noise_frame, text = "Duration").grid(row = row, column = 3)
		row+=1
		burst_frequency_input = Tk.Entry(channel_noise_frame, width=10, textvariable=self.burst_frequency).grid(row = row, column = 2)
		burst_duration_input = Tk.Entry(channel_noise_frame, width=10, textvariable=self.burst_duration).grid(row = row, column = 3)


	def setup_modulation_control(self):
		row = 7
		# Section Title
		modulation_frame = Tk.Frame(root, borderwidth=2, relief="raised", pady= 10, padx=10)
		modulation_frame.grid(row = row, column = 0, rowspan = 2, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		modulation_label = Tk.Label(modulation_frame, text="Modulation", font=("Helvetica", 14)).grid(row = row, column = 0, columnspan = 2, pady = 10, padx = 70)
		row += 1

		# Modulation Type Dropdown
		self.modtype = Tk.StringVar()
		self.modtype.set ("Type")
		modtype_menu = Tk.OptionMenu(modulation_frame, self.modtype, "PSK", "QAM").grid(row=row, columnspan = 2, pady = 10, padx = 10)
		row +=1

		self.modlevel = Tk.StringVar()
		self.modlevel.set ("Level")
		modlevel_menu = Tk.OptionMenu(modulation_frame, self.modlevel, "32","64","128","512","1024").grid(row=row, columnspan = 2, pady = 10, padx = 10)
		
		# Section Title
		row = 10

		row += 1
		self.codetype = Tk.StringVar()
		self.codetype.set ("Line Coding")
		codetype_menu = Tk.OptionMenu(modulation_frame, self.codetype, "GRAY", "LINEAR").grid(row=row, columnspan = 2, pady = 10)

		row += 1
		self.fec = Tk.IntVar()
		self.fec.set(0)
		fec = Tk.Checkbutton(modulation_frame, text="FEC", font=("Helvetica", 12), variable = self.fec).grid(row = row, column = 0, columnspan = 2)

		row += 1
		self.interleave = Tk.IntVar()
		self.interleave.set(0)
		interleave = Tk.Checkbutton(modulation_frame, text="Interlaver", font=("Helvetica", 12), variable = self.interleave).grid(row = row, column = 0, columnspan = 2)

	def savePlotBER(self, figure):
		figure.savefig("BERplot.png")
		print "Plot Saved"

	def savePlotConstellation(self, figure):
		figure.savefig("Constellationplot.png")
		print "Plot Saved"

	def clearPlot(self,f):
		f.clf()
		f.canvas.draw()
		print "Plot Cleared"
	
	# Plots points, instead of division int 4 axes, the main axes range from ngative value to positive to account for all values.
	def plotConstellationCurve(self):
		row = 0
		constellationCurveFrame = Tk.Frame(root, borderwidth=2, relief="raised", pady= 15, padx=10)
		constellationCurveFrame.grid(row = row, column = 2, rowspan = 9, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))

		self.calculate = Tk.IntVar()
		self.calculate.set(0)
		calculate = Tk.Checkbutton(constellationCurveFrame, text="  Calculate", font=("Helvetica", 12), variable = self.calculate).grid(row = 3, column = 21, columnspan = 2)
		

		f = Figure(figsize=(4.5, 4.5), dpi=100)
		a = f.add_subplot(111)	
		t = (-5, 5)
		s = (-5, 5)
		canvas = FigureCanvasTkAgg(f, constellationCurveFrame)
		canvas.show()
		canvas.get_tk_widget().grid(row=1,column = 0,rowspan = 6, columnspan = 6, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		a.plot(t, s,'bs')
		a.axhline(0, color = 'black')
		a.axvline(0, color = 'black')
		a.set_title('Constellation Curve')

		save = Tk.Button(constellationCurveFrame, text="Save", command = lambda: self.savePlotConstellation(f), bg = "cyan").grid(row=4, column = 21, columnspan = 2, sticky=(Tk.W, Tk.E))

	def plotBERcurve(self):
		row = 0
		berCurveFrame = Tk.Frame(root, borderwidth=2, relief="raised", pady= 15, padx=10)
		berCurveFrame.grid(row = row, column = 4, rowspan = 9, columnspan = 2, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))

		self.calculate = Tk.IntVar()
		self.calculate.set(0)
		calculate = Tk.Checkbutton(berCurveFrame, text="  Calculate", font=("Helvetica", 12), variable = self.calculate).grid(row = 2, column = 21, columnspan = 2, sticky=(Tk.W, Tk.E))

		self.hold = Tk.IntVar()
		self.hold.set(0)
		hold = Tk.Checkbutton(berCurveFrame, text="Hold", font=("Helvetica", 12), variable = self.hold).grid(row = 3, column = 21, columnspan = 2, sticky=(Tk.W, Tk.E))

		f = Figure(figsize=(4.5, 4.5), dpi=100)
		a = f.add_subplot(111)
		t = (1, 2, 3, 4)
		s = (1, 2, 3, 4)
		canvas = FigureCanvasTkAgg(f, berCurveFrame)
		canvas.show()
		canvas.get_tk_widget().grid(row= 1,column = 0,rowspan = 6, columnspan = 6, sticky = (Tk.N, Tk.W, Tk.E, Tk.S))
		a.plot(t, s)
		a.set_title('BER Curve')
		a.set_xlabel('Eb/Nq')
		a.set_ylabel('BER')

		save = Tk.Button(berCurveFrame, text="Save", command = lambda: self.savePlotBER(f), bg = "cyan").grid(row=4, column = 21, columnspan = 2, padx = 15, sticky=(Tk.W, Tk.E))

		clear = Tk.Button(berCurveFrame, text="Clear", command = lambda: self.clearPlot(f), bg = "cyan").grid(row=5, column = 21, columnspan = 2, padx = 15, sticky=(Tk.W, Tk.E))	

  

		
root = Tk.Tk()
a = GUI(root)
root.mainloop()

