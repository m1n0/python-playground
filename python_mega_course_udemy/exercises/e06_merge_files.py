import glob2
import datetime

filenames = glob2.iglob('python_mega_course_udemy/data/06.file*.txt')

with open('python_mega_course_udemy/data/06.{}.txt'.format(datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S-%f')), 'w') as file:
    for filename in filenames:
        with open(filename, 'r') as f:
            file.write(f.read() + "\n")
