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

    def __str__(self):
        text_list = [self.name, str(self.x), str(self.y)]
        text = " ".join(text_list)
        return text

    def draw_point(self, markerfacecolor):
        """
        Crée un plot du point
        :param: None
        :returns: None

        """
        pyplot.plot(self.x, self.y,  marker="h", markerfacecolor=self.color)
        pyplot.text(self.x + 0.2, self.y + 0.2, self.name + " (" + str(self.x)+", "
                    + str(self.y) + ")",  backgroundcolor="None", zorder=5, fontsize=5.5)
