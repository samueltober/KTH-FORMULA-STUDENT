import tkinter
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import math


class Plot:
    def __init__(self, xmin, xmax, ymin, ymax, grid_color, master):

        self.xmin, self.xmax, self.ymin, self.ymax = xmin, xmax, ymin, ymax

        # Create a container
        frame = tkinter.Frame(master)

        fig = Figure()
        self.ax = fig.add_subplot(111)
        self.ax.grid(color=grid_color)
        self.ax.set_xlim(self.xmin, self.xmax)
        self.ax.set_ylim(self.ymin, self.ymax)

        self.canvas = FigureCanvasTkAgg(fig,master=master)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side='top', fill='both', expand=1)

        # Create 3 buttons
        self.button_left = tkinter.Button(frame,text="Zoom In", command=self.zoom_in)
        self.button_left.pack(side="left")

        self.button_right = tkinter.Button(frame,text="Zoom Out", command=self.zoom_out)
        self.button_right.pack(side="left")

        self.button_3 = tkinter.Button(frame,text="Reset zoom", command=self.reset_zoom)
        self.button_3.pack(side="left")

        frame.pack()

    def h_function(self, x_data):
        lam = [5*math.sin(2*math.pi*1*i) for i in x_data]
        h_func = [3*math.pi*math.exp(i) for i in lam]

        return h_func

    def plot_data(self, x_data):
        self.ax.plot(x_data, self.h_function(x_data), "r")

    def update_plot(self):
        self.ax.set_xlim([self.xmin, self.xmax])
        self.ax.set_ylim([self.ymin, self.ymax])
        self.canvas.draw()

    def zoom_out(self):
        k=10 #zoom increment
        self.xmin -= k
        self.ymin -= k
        self.xmax += k
        self.ymax += k

        self.update_plot()

    def zoom_in(self):
        k=10

        if self.xmax > 10:
            self.xmin += k
            self.ymin += k
            self.xmax -= k
            self.ymax -= k
        else: #Makes sure we dont zoom-in too far
            self.xmin *= (1/2)
            self.ymin *= (1/2)
            self.xmax *= (1/2)
            self.ymax *= (1/2)

        self.update_plot()

    def reset_zoom(self):
        self.xmin = -500
        self.ymin = -500
        self.xmax = 500
        self.ymax = 500

        self.update_plot()
