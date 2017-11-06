#!/usr/bin/env python

data = open("cars.csv", 'r')
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

def max_data(lines, info_spot):
	group_list = all_data_of_group(lines, info_spot)
	total_of_data = number_of_each_data(lines, info_spot)

	for i in range(0, len(total_of_data)):
		maximum = max(total_of_data)
		for k in range(0, len(total_of_data)):
			if maximum == total_of_data[k]:
				return group_list[k]

def all_data_of_group(lines, info_spot):
	group_list = []
	for i in range(1, len(lines)):
		info = lines[i].rstrip().split(",")
		if info[info_spot] not in group_list:
			group_list.append(info[info_spot])
	return group_list

def number_of_each_data(lines, info_spot):
	group_list = all_data_of_group(lines, info_spot)

	total_of_data = []
	for i in range(0, len(group_list)):
		total = 0
		for k in range(0, len(lines)):
			info = lines[k].rstrip().split(",")
			if group_list[i] == info[info_spot]:
				total += 1
		total_of_data.append(total)

	return total_of_data




print max_data(lines, 4)
print number_of_each_data(lines, 4)


