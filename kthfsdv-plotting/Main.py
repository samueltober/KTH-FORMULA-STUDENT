from Plot import Plot
import numpy as np
import tkinter


def main():
    x_data = np.linspace(-1000, 1000, 200)
    root = tkinter.Tk()
    plot = Plot(-500, 500, -500, 500, "g", root)
    plot.plot_data(x_data)

    root.mainloop()

main()

