import sympy as sp
import numpy as np
import tkinter as tk
import tkinter.ttk as ttk

WINDOW_WIDTH = 1600
WINDOW_HEIGHT = 900

root = tk.Tk(className="Grapher")
root.geometry(f"{WINDOW_WIDTH}x{WINDOW_HEIGHT}")
root.configure(bg="grey")


class Graph:
    def __init__(self):
        cvs_graph = tk.Canvas(root, bg="white", height=WINDOW_HEIGHT, width=WINDOW_WIDTH)
        cvs_graph.pack()
        functions = []
        self.functions = functions


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


graph = Graph()

root.mainloop()