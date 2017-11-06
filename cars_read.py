#!/usr/bin/env python

data = open("cars_test.csv", 'r')
lines = data.readlines()

def car_data_lists(lines):
	car_ids = []
	car_makes = []
	car_models = []
	car_years = []
	car_colors = []

	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")
		car_makes.append(info[1])
		car_models.append(info[2])
		car_years.append(int(info[3]))
		car_colors.append(info[4])

def cars_in_year(lines, year):
	car_makes = []
	car_models = []
	car_years = []
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")
		if int(info[3]) == year:
			car_makes.append(info[1])
			car_models.append(info[2])
			car_years.append(info[3])

	for i in range(0, len(car_years)):
		print "The %s %s is made in %s" % (car_makes[i], car_models[i], year)

def make_since_year(lines, make, year):
	car_makes = []
	car_years = []
	count = 0
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")
		if int(info[3]) >= year and info[1] == make:
			count += 1

	return "The amount of %ss since %s is %s" % (make, year, count)

def max_number_spot(numbers):
	current_max = numbers[0]
	for n in numbers:
		if n > current_max:
			current_max = n

	return current_max

def popular_color(lines):
	car_colors = []
	color_list = []
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")
		if info[4] not in color_list:
			color_list.append(info[4])

	total_of_color = []
	for i in range(0, len(color_list)):
		total = 0
		for k in range(0, len(lines)):
			info = lines[k].rstrip().split(",")
			if color_list[i] == info[4]:
				total += 1
		total_of_color.append(total)

	for i in range(0, len(total_of_color)):
		maximum = max(total_of_color)
		for k in range(0, len(total_of_color)):
			if maximum == total_of_color[k]:
				return color_list[k]




cars_in_year(lines, 2006)
print make_since_year(lines, "Toyota", 2000)
print popular_color(lines)
popular_color(lines)

