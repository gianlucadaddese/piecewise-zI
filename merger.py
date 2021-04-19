import sys
def hash(array):
	x=""
	for i in array:
		x+=str(i)
	return (x)

def merge (max_zI):
	genes_num= 0
	gene_to_merge = []
	genes_timeline = []
	timeline = []
	best = 0
	max_zI = float(max_zI)

	with open("grind.txt")as in1:
		line1 = in1.readline()
		genes_name = line1.split()
		genes_num = len(genes_name)

		if (genes_num <= 1):
			return(3)

		line2 = in1.readline()
		gene_to_merge = line2.split()[0:genes_num]
		best = line2.split()[genes_num]
		if (float(best)<max_zI):
			#if you want to print the first group under treshold
			#with open ("sequence.txt","a") as out:
			#	for i in genes_name:
			#		out.write("{}\t".format(i))
			#	out.write("{}\n".format(best))
			return(3)

	with open("file.txt", "r") as f:
		geni = []

		for line in f:
			linea_geni = line
			geni = line.split()
			break
		genes_num = len(geni)

		for line in f:
			timeline.append(list(map(int, line.split())))
		support = zip(*timeline)
		for i in support:
			genes_timeline.append(list(i))


	dict_new_gene= {}
	new_gene = []
	num = 0
	for riga in timeline:
		support=[]
		for n in range(genes_num):

			if (gene_to_merge[n]== "1"):
				support.append(riga[n])

		support = hash(support)

		if support not in dict_new_gene.keys():

			dict_new_gene[support]=num
			num+=1
			new_gene.append(dict_new_gene[support])
		else:
			new_gene.append(dict_new_gene[support])


	name_new_gene = ""
	to_pop = []
	for n,i in enumerate(gene_to_merge):
		if (i=="1"):
			to_pop.append(n)
			name_new_gene += "_{}".format(genes_name[n])
	name_new_gene = name_new_gene[1:]



	to_pop.sort(reverse=True)
	for i in to_pop:
		genes_timeline.pop(i)
		genes_name.pop(i)

	genes_name.append(name_new_gene)
	genes_timeline.append(new_gene)


	with open ("file.txt","w") as out:
		for i in genes_name:
			out.write("{}\t".format(i))
		out.write("\n")
		timeline = zip(*genes_timeline)
		for i in timeline:
			for elem in list(i):
				out.write("{}\t".format(elem))
			out.write("\n")

	with open ("sequence.txt","a") as out:
		for i in genes_name:
			out.write("{}\t".format(i))
		out.write("{}\n".format(best))
	if len(genes_name) == 1:
		return 3
	else: 
		return 0
