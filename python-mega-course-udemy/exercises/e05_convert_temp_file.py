from exercises.e03_convert_temp import celsius_to_f

temperatures = [10, -20, -289, 100]

file = open('05.temperatures.txt', 'a+')
for temp in temperatures:
    if isinstance(celsius_to_f(temp), float):
        file.write(str(temp))

file.close()