import statistics
import os
all_file = os.listdir("files")

for file in all_file:
	nome_file = file
	in_file = open("files/{0}".format(nome_file),"r")
	
	
	observations = []
	single = []
	for line in in_file:
		single = line.split()
		observations.append(single)
	in_file.close()

	genes = []
	for i in range(len(single)):
		gene = []
		for j,oss in enumerate(observations):
			if j==0:
				gene.append(oss[i])
			else:
				gene.append(int(oss[i]))
		genes.append(gene)
	print(len(genes))
	print("start")
	genes_remain=[]
	for i,g in enumerate(genes):
		print(i)
		if statistics.stdev(g[1:len(g)])==0:
			print ("gene to del found #####################")
			continue
		genes_remain.append(g)


	out_file = open("files/{0}".format(nome_file),"w")
	for o in range(len(genes_remain[0])):
		for g in genes_remain:
			out_file.write(str(g[o])+"\t")
		out_file.write("\n")
