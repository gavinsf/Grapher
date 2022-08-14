import sympy as sp
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900


class Main(tk.Frame):
    def __init__(self):
        self.graph = Graph()
        self.input = Input()


class Graph(tk.Frame):
    def __init__(self):
        cvs_graph = tk.Canvas(root, bg="white", height= 2*WINDOW_HEIGHT/3, width=WINDOW_WIDTH)
        cvs_graph.grid(row=0, column=0)
        functions = []
        self.functions = functions


class Input(tk.Frame):
    def __init__(self):
        ent = tk.Entry(root, bg="grey")
        ent.grid(row=1, column=0, ipadx=WINDOW_WIDTH/2-60, ipady=10)
        self.ent = ent


class Function:
    def __init__(self, function, colour):
        self.function = function
        self.colour = colour
    
    def get_function(self):
        return self.function
    
    def get_colour(self):
        return self.colour


class Draw:
    def __init__(self):
        pass


if __name__ == "__main__":
    root = tk.Tk(className="Grapher")
    root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
    root.configure(bg="black")
    main = Main()
    root.mainloop()