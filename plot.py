import plotly
import plotly.graph_objs as go
from cars_read import *


data = [go.Bar(
			x = color_list[x],
			y = total_of_color[y]
	)]

plotly.offline.plot(data, filename = 'cars_read')