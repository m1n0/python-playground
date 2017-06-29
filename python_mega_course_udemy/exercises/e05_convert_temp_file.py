from python_mega_course_udemy.exercises.e03_convert_temp import celsius_to_f
from python_mega_course_udemy.exercises.e04_convert_temp_list import temperatures

file = open('python_mega_course_udemy/data/05.temperatures.txt', 'w')
for temp in temperatures:
    converted = celsius_to_f(temp)
    if isinstance(converted, float):
        file.write(str(converted) + "\n")

file.close()
