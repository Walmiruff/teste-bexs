import csv
from services.graph_service import *

class FileService(object):

	def __init__(self, input_file = None):
		self.input_file = input_file
		self.input_data = []

	def openFile(self, file, type_exe):
		return open(file, type_exe)

	def readFile(self):
		listData = []
		with self.openFile(self.input_file, "r") as archive:
			reader = csv.reader(archive)
			try:
				for linha in reader:
					listData.append(linha)
			except csv.Error as e:
				print('Error ao abrir arquivo csv.')
		archive.close()
		self.input_data = listData
	
	def writeFile(self, origin, destiny, cost):
		try:
			newRoute = origin + ',' + destiny + ',' + cost
			with open(self.input_file, 'a+') as archive:
				archive.write('\n')
				archive.write(newRoute)
				archive.close()
			return True
		except:
			return False