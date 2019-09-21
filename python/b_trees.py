#!/usr/bin/python
# -*- coding: utf-8 -*-

test_arr = [8,0, 16, -3, 889, 19, 19, 0, 11, 6,4,56, -39, 48, 66, 300, 2, 5, 111]


#  Если работаешь с числовыми, то КЕЙ не нужен, чо, можно и вэлью, а так вэлью - текс, словарь, объект, а кей - или отдеьный или элемент вэлью. 
#  Допстим, из объекта его айди или возраст или еще какое-то значение ,ПО КОТОРОМУ НУЖНО ОТСОРТИРОВАТЬ

class BinaryTree:
	def __init__(self, node_value=None, node_key=None):
		self.node_key = node_key
		self.node_value = node_value
		self.left_child = None
		self.right_child = None

	def get_left_node(self):
		return self.left_child
		pass

	def get_right_node(self):
		return self.right_child
		pass

	def get_node_value(self):
		return self.node_value
		pass

	def get_node_key(self):
		return self.node_key
		pass

	def insert_left_node(self, value, key):
		if self.left_child == None:
			self.left_child =  BinaryTree(node_value=value, node_key=key)
		else:
			new_node = BinaryTree(node_value=value)
			new_node.left_child = self.left_child
			self.left_child = new_node
			pass

	def insert_right_node(self, value, key):
		if self.right_child == None:
			self.right_child =  BinaryTree(node_value=value,node_key=key)
		else:
			new_node = BinaryTree(node_value=value)
			new_node.right_child = self.right_child
			self.right_child = new_node
			pass



	def find_element_in_tree(self, value):
		if self.get_node_value() == value:
			return self.get_node_value()
		else:
			if value < self.get_node_value():
				return self.find_element_in_tree(self.get_left_node(), value)
			if value > self.get_node_value():
				return self.find_element_in_tree(self.get_right_node(), value)
				pass


"""
Julia = {"position": "Mother", "age": 51, "name": "Julia", "status": "Live","sex":"female"}
Nina = {"position": "Grandma", "age": 74, "name": "Nina", "status": "Live","sex":"female"}
Victor = {"position": "Grandfa", "age": None, "name": "Victor", "status": "Dead", "sex":"male"}
Nadia = {"position": "Grand-Grand-ma", "age": None, "name": "Nadia", "status": "Dead", "sex":"female"}
family_list = (Julia, Nina, Victor, Nadia)


def insert_into_tree(root_node, element):
	if element["sex"] == "female":
			#IF NOT ????????
		if root_node.get_right_node() == None:
			root_node.insert_right_node(element)
		else:
			insert_into_tree(root_node.get_right_node(), element)

	if element["sex"] == "male":
		print("HERE")
		if root_node.get_left_node() == None:
			root_node.insert_left_node(element)
		else:
			insert_into_tree(root_node.get_left_node(), element)

def create_binary_tree(node, elements_list):
	for element in elements_list:
		insert_into_tree(node, element)



Egor = BinaryTree(node_value={"name": "Egor", "age":25, "city":"Minsk"})

create_binary_tree(Egor, family_list)
print(Egor.get_right_node().get_right_node())
"""

def find_max_height(node):
	if not node:
		return 0
	else:
		l_height =  find_max_height(node.get_left_node())+1
		r_height = find_max_height(node.get_right_node())+1
		if l_height > r_height:
			return l_height
		else:
			return r_height
			pass

def insert_into_binary_tree(root_node, element, key):
	if root_node.get_node_key() != key:
		if root_node.get_node_key() < key:
			if not root_node.get_right_node():
				root_node.insert_right_node(element, key)
			else:
				insert_into_binary_tree(root_node.get_right_node(), element, key)
		if root_node.get_node_key() > key:
			if not root_node.get_left_node():
				root_node.insert_left_node(element, key)
			else:
				insert_into_binary_tree(root_node.get_left_node(), element, key)
				pass

def numbers_list_to_binary_tree(node, numbers_list):
	for element in numbers_list:
		insert_into_binary_tree(node, element, element)	
	return node
	pass

def sorted_list_from_tree(node):
	sorted_list = []
	if node:
		sorted_list += sorted_list_from_tree(node.get_left_node())
		sorted_list.append(node.get_node_value())
		sorted_list += sorted_list_from_tree(node.get_right_node())
	return sorted_list
	pass


def sorting_list_to_tree(node, numbers_list):
	numbers_list_to_binary_tree(node, numbers_list)
	return sorted_list_from_tree(node)
	pass


test_node = BinaryTree(node_value = test_arr[0], node_key = test_arr[0])
test = numbers_list_to_binary_tree(test_node, test_arr)
#print(test.get_right_node().get_right_node().get_node_value())
#print(sorting_list_to_tree(test_node, test_arr))
print(find_max_height(test))