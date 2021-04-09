import math
from community import community_louvain
from itertools import combinations
import networkx as nx
import matplotlib.pyplot as plt
import os
import sys,getopt
import shutil
import subprocess
from random import random

short_options = "g:z:"
long_options = ["group=","zi="]
argument_list = sys.argv[1:]

max_dimension = 3
max_zI = 3

try:
    arguments, values = getopt.getopt(argument_list, short_options, long_options)
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

for current_argument, current_value in arguments:
    if current_argument in ("-g", "--group"):
        max_dimension = int(current_value)
    elif current_argument in ("-z", "--zi"):
        max_zI = float(current_value)
    else:
        print("missing argoument, take a look at the ReadMe for more information")
        sys.exit(2)

print(max_dimension)
print(max_zI)

def integration(array):
    integration = 0
    for gene in array:
        single_entropy = 0
        for elem in list(set(gene)):
            single_entropy -= gene.count(elem) / len(gene) * math.log(gene.count(elem) / len(gene))
        integration += single_entropy
    different_combination = []
    for o in range(len(array[0])):
        combination = []
        for gene in array:
            combination.append(gene[o])
        different_combination.append(combination)
    set_different_combination = [ele for ind, ele in enumerate(different_combination) if
                                 ele not in different_combination[:ind]]

    for elem in set_different_combination:
        integration += different_combination.count(elem) / len(gene) * math.log(
            different_combination.count(elem) / len(gene))
    return (integration)


def evaluate_d(composition):
    result = 1
    for i in composition:
        result = result * i
    for i in composition:
        result = result - (i - 1)
    return result - 1

def union (genes):
    new = []
    single = list(zip(*genes))
    dict ={}
    i=0
    for item in single:
        if item not in dict.keys():
            dict[item]=i
            new.append(i)
            i+=1
        else:
            new.append(dict[item])
    return new




if os.path.exists("community_dimension.txt"):
    os.remove("community_dimension.txt")

file_to_graph = os.listdir("file_to_graph")
file_to_graph.sort()
for ftg in file_to_graph:
    print("{}".format(ftg))
    shutil.copy("file_to_graph/{}".format(ftg),"file.txt")
    genes_num = 0
    trajectory = []
    timeline = []
    genes_line = ""
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
    num = [x for x in range(0, genes_num)]
    all = []
    dict = {}
    for k in range(2,3):
        print("evaluate graph of dimension: {}".format(genes_num))
        for combination_num in list(combinations(num, k)):
            combination_num = list(combination_num)
            combination = []
            for i in combination_num:
                combination.append(trajectory[i])
            I = integration(combination)
            d = evaluate_d([len(set(x)) for x in combination])

            average = d
            dev = math.sqrt(2*d)
            zI = (2 * o * I - average) / dev
            all.append([combination_num, zI, I, average, dev])

    all.sort(key=lambda x: x[1], reverse=True)




    #@@@@@@@@@@@@@@@@@@@@@@@@@@ parto con la creazione del grafo

    G=nx.Graph()

    for i in genes:
        G.add_node(i)
    for a in all:
        if a[1] >= max_zI:
            G.add_edge(genes[a[0][0]], genes[a[0][1]])




    com = community_louvain.best_partition(G)


    com_list=[]
    for i in range(0,max(com.values())+1):
        var = []
        for c in com:
            if com[c]== i:
                var.append(c)
        com_list.append(var)

    com_list_to_print = [len(x) for x in com_list]
    com_list_to_print.sort(reverse=True)
    with open("community_dimension.txt", "a") as outflen:
        for c in com_list_to_print:
            outflen.write("{}\t".format(c))
        outflen.write("\n")

    colormap = [0] * genes_num

    #use color for community
    for nodes in com_list:
        r =(random(), random(), random())
        for n in nodes:

            colormap[genes.index(n)] = r




    nx.draw_networkx(G, node_color =colormap)
    text_to_del = ftg.rfind('.')
    plt.savefig("graph_{}".format(ftg[0:text_to_del]))
    plt.clf()


    if os.path.isdir("files"):
        shutil.rmtree('files', ignore_errors=True)

    os.mkdir("files")
    with open ("post_community.txt","w") as final:
        for item in com_list:
            if len(item)< 2:
                final.write("{}\t".format(item[0]))
            elif len(item)>1 and len(item)<3:
                final.write("{}_{}\t".format(item[0],item[1]))
            else:
                to_print =[]
                name= "{}".format(item).replace(" ","_").replace("'","")
                name = name [0:250]
                with open(name,"w") as out:
                    for i in genes:
                        if i in item:
                            to_print.append(genes.index(i))
                            out.write("{}\t".format(i))
                    out.write("\n")
                    timeline2 = list(zip(*trajectory))

                    for i in timeline2:
                        for n,elem in enumerate(list(i)):
                            if n in to_print:
                                out.write("{}\t".format(elem))
                        out.write("\n")
                shutil.move(name,"./files/{}".format(name))

    subprocess.call('python3 run_zi.py -g {} -z {}'. format(max_dimension, max_zI), shell = True)

    all_file = os.listdir(".")

    for dir in all_file:
        if dir.startswith("["):
            shutil.move(dir, "group/{}".format(dir))


    all_file = os.listdir("group")
    with open("post_community.txt","a") as final:
        for dir in all_file:
            with open("group/{}/sequence.txt".format(dir), "r") as f:
                correct_line = ""
                p=0
                for line in f:
                    if (float(line.split()[-1]) < max_zI and float(line.split()[-1]) != 0):
                        for i in correct_line.split()[0:-1]:
                            final.write("{}\t".format(i))
                        p = 2
                        break
                    else:
                        correct_line = line
                        p = 1

                if p==1:
                    for i in correct_line.split()[0:-1]:
                        final.write("{}\t".format(i))


    with open("post_community.txt","r") as final:
        timeline_final = []
        riga_geni = final.readline()
        for group in riga_geni.split():
            timeline_group = []
            for g in group.split("_"):
                ind = genes.index(g)
                timeline_group.append(trajectory[ind])
            new_gene = union(timeline_group)
            timeline_final.append(new_gene)

    if os.path.exists(ftg) and os.path.isdir(ftg):
        shutil.rmtree(ftg)
    shutil.move("./group","{}/group".format(ftg))
    shutil.move("files","{}/files_start".format(ftg))

    with open ("final_merge","w") as inf:
        inf.write(riga_geni)
        inf.write("\n")
        support = list(zip(*timeline_final))

        for line in support:
            for elem in line:
                inf.write("{}\t".format(elem))
            inf.write("\n")

    os.mkdir("files")
    shutil.move("final_merge","files/final_merge")
    subprocess.call('python3 run_zi.py -g {} -z {}'.format(max_dimension, max_zI), shell=True)
    shutil.move("final_merge","{}/final_merge".format(ftg))
    shutil.move("post_community.txt","{}/".format(ftg))
    shutil.move("graph_{}.png".format(ftg[0:text_to_del]), "{}/".format(ftg))
    if os.path.exists("file.txt"):
        os.remove("file.txt")
    print("END OF {}".format(ftg))


