import numpy
import PIL
from PIL import Image
import os, sys
import csv



# output_dir = "tensor_data"
dir1 = '/Users/li-tigre/Desktop/Resized_data/tensor_data_untouched/'
dir2 = '/Users/li-tigre/Desktop/Resized_data/tensor_data_touched/'


with open('output.csv', 'w') as csvfile:
	fieldnames = ['image', 'label']

	writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

	for file in os.listdir(dir1):
		# Convert Image to array
		# print(file)

		writer.writeheader()

		img = Image.open('/Users/li-tigre/Desktop/Resized_data/tensor_data_untouched/' + file)
		arr = numpy.array(img)
		# print(arr)
		writer.writerow({'image': arr, 'label': 0})

	for file in os.listdir(dir2):
	# Convert Image to array
	# print(file)
	# writer.writeheader()

		img = Image.open('/Users/li-tigre/Desktop/Resized_data/tensor_data_touched/' + file)
		arr = numpy.array(img)
		# print(arr)
		writer.writerow({'image': arr, 'label': 1})




