#!/usr/bin/python
# -*- coding: utf-8 -*-
#бинарная
#быстрая
#Сортировка вставками / Insertion sort
#Сортировка выбором / Selection sort
#Сортировка слиянием / Merge sort
test_arr = [8,0, 16, -3, 889, 19, 19, 0, 11, 6,4,56]

def bubble_sort(arr):
	for i in range(len(arr)-1):
		# идет простая проходка по циклу.
		for x in range(len(arr)-1-i):
			"""
			а вот здесь уже идет процесс смены.
			каждый внутренний цикл проходится по всему списку.
			и каждую проходку 
			ТОЛЬКО ПРОПИХИВАЕТ В КОНЕЦ БОЛЬШИЙ ЭЛЕМЕНТ.
			И все!
			ТОЛЬКО один элемент становится в конец.
			И каждый раз тебе нужно в конце поставть элемент ПЕРЕд самым последним.
			Бо в первую проходку в конце выдвинется самый толстый, за счет сравнения.
			В следующую - чуть  меньший и т.д.
			"""

			#print("Arr on big iteration",arr)
			if arr[x] > arr[x+1]:
				arr[x], arr[x+1] = arr[x+1], arr[x]

				#print("####arr on inside iters", arr)
	return arr
	pass


#bubble_sort(test_arr)

def find_min(arr):
	mini = None
	for element in arr:
		if not mini:
			mini = element
		if element < mini:
			mini = element
	return mini
	pass


def insert_sort(arr):
	#Важно помнить о большом и малм шаге. Внутренний цикл ВЕСЬ проходит на ОДНОМ большом шаге.
	#Соответственно на одном БОЛШОМ шаге мы концентрируемся на сортировке вокруг ОДНОГО большого элемента

	#И вот тут на каждом большом шаге мы берем один БОЛШОЙ элемент, и двигаем его в отсортированную зону. 
	#А потом сменяем БОЬШОЙ на следующий, который так же пропихиваем.

	for position in range(1, len(arr)):
		current_value = arr[position]

		while position > 0 and current_value < arr[position - 1]:
			arr[position] = arr[position-1]
			position = position-1
		
		arr[position] = current_value

	return arr
	pass


def insert_sort_2(arr):
	sorted_arr = []
	for i in range(len(arr)):
		min_el = find_min(arr)
		sorted_arr.append(arr.pop(arr.index(min_el)))
	return sorted_arr
	pass


def insert_sort_3(arr):
	sorted_arr = []
	for i in range(len(arr)):
		min_el = find_min(arr)
		sorted_arr.append(min_el)
		arr.remove(min_el)
	return sorted_arr
	pass


def insert_sort_4(arr):
	for position in range(1, len(arr)):
		current_value = arr[position]
		for x in range(0, position):
			if current_value < arr[x]:
				current_value, arr[x] = arr[x], current_value
		arr[position] = current_value

	return arr
	pass





def selection_sort(arr):
	for element in range(len(arr)):

		current_value = element
		print(current_value)

		for inner_element in range(element+1, len(arr)):
			if arr[inner_element] < arr[current_value]:
				#print(arr[inner_element], arr[current_value])
				current_value = inner_element
				#print(arr)

		arr[current_value], arr[element] = arr[element], arr[current_value]
		print("Смена:", arr)
	return arr
	pass



def qsort1(list):
    if list == []: 
        return []
    else:
        pivot = list[0]
        lesser = qsort1([x for x in list[1:] if x < pivot])
        greater = qsort1([x for x in list[1:] if x >= pivot])
        return lesser + [pivot] + greater




def quick_sort(arr):
	if arr == []:
		return []
	else:
		start_el = arr[0]
		middle = []
		maxi = []
		mini = []
		for x in arr:
			if x > start_el:
				maxi += [x]
			if x < start_el:
				mini += [x]
			if x == start_el:
				middle.append(x)

		return quick_sort(mini) + middle + quick_sort(maxi)

#print(qsort1(test_arr))
#print(quick_sort(test_arr))
#print(insert_sort(test_arr))
#print(insert_sort_4(test_arr))
#print(selection_sort(test_arr))
