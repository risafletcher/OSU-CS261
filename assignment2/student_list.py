# student_list.py
# ===================================================
# Reimplementation of Pythons List
# ===================================================

import numpy as np


# StudentList class is our implementation of Python's List
class StudentList:
	def __init__(self):
        # creates an empty array of length 4, change the [4] to another value to make an
        # array of different length.
		self._list = np.empty([4], np.int16)
		self._capacity = 4
		self._size = 0

	def __str__(self):
		return str(self._list[:self._size])

# You may want an internal function that handles resizing the array.
# Dont modify get_list or get_capacity, they are for testing

	def get_list(self):
		return self._list[:self._size]

	def get_capacity(self):
		return self._capacity

	def append(self, val):
		if self._size == self._capacity:
			self._capacity = self._capacity * 2
			new_list = np.empty(self._capacity, np.int16)
			for i in range(self._size):
				new_list[i] = self._list[i]
			self._list = new_list
		self._list[self._size] = val
		self._size = self._size + 1
		
	def pop(self):
		last_element = self._list[self._size - 1]
		new_size = self._size - 1
		new_list = np.empty(self._capacity, np.int16)
		for i in range(new_size):
			new_list[i] = self._list[i]
		self._size = new_size
		self._list = new_list
		return last_element

	def insert(self, index, val):
		if index >= self._size:
			self.append(val)
		else:
			new_capacity = self._capacity
			if self._size == self._capacity:
				new_capacity = self._capacity * 2
			new_size = self._size + 1
			self._size = new_size
			new_list = np.empty(new_capacity, np.int16)
			for i in range(new_size):
				if (i == index):
					new_list[i] = val
				elif (i > index):
					new_list[i] = self._list[i - 1]
				else:
					new_list[i] = self._list[i]
			self._list = new_list
			

	def remove(self, val):
		new_list = np.empty(self._capacity, np.int16)
		index = 0
		removed = False
		for i in range(self._size):
			if (removed == False):
				if self._list[i] != val:
					new_list[index] = self._list[i]
					index = index + 1
				else:
					removed = True
			else:
				new_list[index] = self._list[index + 1]
				index = index + 1
		self._list = new_list
		if removed == True:
			self._size = self._size - 1

	def clear(self):
		self._list = np.empty(0, np.int16)
		self.size = 0

	def count(self):
		return self._size

	def get(self, index):
		if (index >= self._size):
			return 'None'
		return self._list[index]
