import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class SignatureCanvas(tk.Canvas):
    def __init__(self, *args, **kwargs):
        self.thickness = kwargs.pop('thickness', 1)
        tk.Canvas.__init__(self, *args, **kwargs)

        self.b1 = 'up'
        self._xold = None
        self._yold = None

        self.bind("<Motion>", self._on_motion)
        self.bind("<ButtonPress-1>", self._b1down)
        self.bind("<ButtonRelease-1>", self._b1up)

    def _on_motion(self, event):
        if self.b1 == "down":

            x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
            x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
            event.widget.create_oval(x1, y1, x2, y2, fill="black")
            if self._xold is not None and self._yold is not None:
                #python_green = "#476042"
                x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
                x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
                self.create_oval(x1, y1, x2, y2, fill="black")
                self.create_line(self._xold, self._yold, event.x, event.y, smooth=True, width=self.thickness*2+1)
            # here's where you draw it. smooth. neat.
            self._xold = event.x
            self._yold = event.y

    def _b1down(self, event):
        x1, y1 = (event.x - self.thickness), (event.y - self.thickness)
        x2, y2 = (event.x + self.thickness), (event.y + self.thickness)
        event.widget.create_oval(x1, y1, x2, y2, fill="black")
        self.b1 = "down"

    def _b1up(self, event):
        self.b1 = "up"
        self._xold = None  # reset the line when you let go of the button
        self._yold = None

