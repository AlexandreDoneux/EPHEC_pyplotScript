# Python 3.10
# UTF-8
# Alexandre Doneux

from matplotlib import pyplot


class Point:
    def __init__(self, name, x, y, color='black'):
        self.x = x
        self.y = y
        self.name = name
        self.color = color

    def draw_point(self):
        """
        Crée un plot du point
        :param: None
        :returns: None

        """
        pyplot.plot(self.x, self.y, self.color)
        pyplot.text(self.x + 0.1, self.y + 0.1, self.name, fontsize=10)
