import plotly
import plotly.graph_objs as go
from cars_read import *

color_list = all_data_of_group(lines, 4)
total_of_colors = number_of_each_data(lines, 4)

data = [go.Bar(
			x = color_list,
			y = total_of_colors
	)]

plotly.offline.plot(data, filename = 'cars_read')