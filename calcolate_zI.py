import random as rand
import math
import statistics as st
import multiprocessing as mp
import sys
from itertools import combinations



def integration(array):
	integration = 0
	for gene in array :
		single_entropy=0
		for elem in list(set(gene)):
			single_entropy -= gene.count(elem)/len(gene) * math.log(gene.count(elem)/len(gene))
		integration += single_entropy
	different_combination = []
	for o in range(len(array[0])):
		combination = []
		for gene in array:
			combination.append(gene[o])
		different_combination.append(combination)
	set_different_combination =[ele for ind, ele in enumerate(different_combination) if ele not in different_combination[:ind]]

	for elem in set_different_combination:
		integration += different_combination.count(elem) / len(gene) * math.log(different_combination.count(elem) / len(gene))
	return (integration)

def evaluate_d(array_d):
	result = 1
	for i in array_d:
		result = result*i
	for i in array_d:
		result = result -(i-1)
	return result-1

def calcolate_zi(max_dimension):
	num_line_to_print= 1000

	genes_num = 0
	trajectory = []
	timeline = []
	genes_line= ""
	with open("file.txt", "r") as f:
		genes = []

		for line in f:
			genes_line = line
			genes = line.split()
			break
		genes_num = len(genes)



		for line in f:
			timeline.append(list(map(int, line.split())))
		support = zip(*timeline)


		for i in support:
			trajectory.append(list(i))
	o = len(trajectory[0])
	num = [x for x in range (0, genes_num)]
	all = []
	dict = {}
	for k in range(2, min(int(max_dimension)+1, genes_num + 1)):
		print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ {} di {}".format(k, genes_num))
		for combination_num in list(combinations(num,k)):
			combination_num = list(combination_num)
			combination = []
			for i in combination_num:
				combination.append(trajectory[i])
			I = integration(combination)
			d = evaluate_d([len(set(x)) for x in combination])


			average = d
			dev = math.sqrt(2*d)
			zI = (2 * o * I - average) / dev
			all.append([combination_num, zI, I, d, o, average, dev])



	all.sort(key=lambda x: x[1], reverse=True)
	with open ("grind.txt", "w") as out:
		out.write(genes_line)
		for num, i in enumerate(all):
			for k in range (genes_num):
				if (k in i[0]):
					out.write("1\t")
				else:
					out.write("0\t")
			#if you whant to see all the index for every group
			#out.write("{}\t{}\t{}\t{}\t{}\t{}\t\n".format(i[1],i[2],i[3],i[4],i[5],i[6]))
			out.write("{}\n".format(i[1]))
			if(num>num_line_to_print):
				break
	if (genes_num <=1):
		exit(-1)

