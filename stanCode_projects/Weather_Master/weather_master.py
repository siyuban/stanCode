"""
File: weather_master.py
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""

# This constant controls when to stop
EXIT = -100


def main():
	"""
	This program computes the average, highest, lowest, cold days among the inputs of weather data.
	"""
	print('stanCode "Weather Master 4.0"!')
	temperature = int(input('Next temperature: (or '+str(EXIT)+' to quit?)'))
	total = temperature
	# The sum of temperature data.
	day = 1
	# The sum of days, and it starts from 1.( If temperature != EXIT)
	cold_day = 0
	# The sum of cold days, and it starts from 0.
	if temperature < 16:
		cold_day += 1
		# determine whether the first data is a cold day.
	if temperature == EXIT:
		print('No temperatures were entered')
	else:
		maximum = temperature
		minimum = temperature
		while True:
			temperature = int(input('Next temperature: (or ' + str(EXIT) + ' to quit?)'))
			avg = float(average(total, day))
			if temperature == EXIT:
				print('Highest temperatures = ' + str(maximum))
				print('Lowest temperatures = ' + str(minimum))
				print('Average = ' + str(avg))
				print(str(cold_day)+' cold days(s)')
				break
			else:
				total += temperature
				if temperature < 16:
					cold_day += 1
					# determine whether the other data is a cold day.
				if temperature > maximum:
					maximum = temperature
				if temperature < minimum:
					minimum = temperature
				day = day + 1


def average(total, day):
	"""
	:param total: The sum of temperature data.
	:param day: The sum of days.
	:return: The average temperature.
	"""
	avg = total/day
	return avg



















###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
