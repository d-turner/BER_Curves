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
row = 0
root = Tk.Tk()
root.wm_title("BER Curves")
w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))

simulate_label = Tk.Label(root, text="Simulation Control").grid(row=row, column=0)
row += 1
lb1 = Tk.Label(root, text="Error Bits")
lb1.grid(row=row, sticky=W)
row += 1
error_bits = Tk.IntVar()
error_bits.set(0)
err_input = Tk.Entry(root, width=10, textvariable=error_bits)
err_input.grid(row=row, sticky=W)
row += 1


def run_program():
    print error_bits.get()
    #output1 = Generate(input)
    #output2 = Modulate(input)
    #output3 = Coding(input)
    #output4 = Noise(input)
    #output5 = SNR(i.get())

snr = Tk.StringVar()
snr.set("Default SNR")
snr_step = Tk.OptionMenu(root, snr, "one", "two", "three", "etc")
snr_step.grid(row=row, sticky=W)
row += 1
run = Tk.Button(root, text="Run", command=run_program)
run.grid(row=row, sticky=W)

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = (1, 2, 3, 4)
s = (1, 2, 3, 4)
canvas = FigureCanvasTkAgg(f, root)
canvas.show()
canvas.get_tk_widget().grid(row=5)

a.plot(t, s)

root.mainloop()
