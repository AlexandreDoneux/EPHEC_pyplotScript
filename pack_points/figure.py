# Python 3.10
# UTF-8
# Alexandre Doneux

from matplotlib import pyplot


class Figure:
    def __init__(self, points, color="black", line_style="solid"):
        self.list_x = []
        self.list_y = []
        self.point_names = []
        for point in points:
            self.list_x.append(point.x)
            self.list_y.append(point.y)
            self.point_names.append(point.name)

        self.color = color
        self.line_style = line_style


    def draw_figure(self):
        pyplot.plot(self.list_x, self.list_y, self.color, linestyle=self.line_style, marker="h", markerfacecolor="black")
        for i in range(len(self.list_x)):
            pyplot.text(self.list_x[i], self.list_y[i], self.point_names[i] + " (" + str(self.list_x[i])+", "
                        + str(self.list_y[i]) + ")", backgroundcolor="khaki", zorder=5, fontsize=10)



