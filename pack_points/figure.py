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


    def draw_figure(self, color="black"):
        self.color = color
        pyplot.plot(self.list_x, self.list_y, color=self.color, linestyle=self.line_style, marker="h", markerfacecolor="black")
        # on referme la figure
        end_list_x = [self.list_x[-1], self.list_x[0]]
        end_list_y = [self.list_y[-1], self.list_y[0]]
        pyplot.plot(end_list_x, end_list_y, color=self.color, linestyle=self.line_style, marker="h", markerfacecolor="black")
        for i in range(len(self.list_x)):
            pyplot.text(self.list_x[i]+0.2, self.list_y[i]+0.2, self.point_names[i] + " (" + str(self.list_x[i])+", "
                        + str(self.list_y[i]) + ")", backgroundcolor="None", zorder=5, fontsize=5.5)



