from math import pi, cos, sin
import random


class Robot:

    size = 2
    color = "red"
    widget = None
    display_noise = 4.0

    def __init__(self, x=0, y=0, orientation=(2 * pi)):
        self.x = x
        self.y = y
        self.orientation = orientation

    def erase(self, canvas):
        if self.widget:
            canvas.delete(self.widget)

    def display(self, canvas):
        size = self.size
        color = self.color
        self.erase(canvas)
        # random displacement to disclose items in same position
        x = self.x + random.gauss(0.0, self.display_noise)
        y = self.y + random.gauss(0.0, self.display_noise)
        if not color is None and color is not "None":
            self.widget = canvas.create_rectangle(
                x - size, y - size, x + size, y + size,
                fill=color, outline="gray20", activefill="red")

    def move(self, rotation, distance):
        self.orientation += rotation
        self.orientation %= 2 * pi
        self.x += (cos(self.orientation) * distance)
        self.y += (sin(self.orientation) * distance)

    def __repr__(self):
        return ('[x=%.6s y=%.6s orient=%.6s]' %
                (self.x, self.y, self.orientation))
