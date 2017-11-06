import plotly
import plotly.graph_objs as go
from cars_read import *

years_list = all_data_of_group(lines, 3)
total_cars_in_year = number_of_each_data(lines, 3)

data = [go.Bar(
			x = years_list,
			y = total_cars_in_year
	)]

plotly.offline.plot(data, filename = 'cars_read')