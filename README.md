# piecewise-zI

## Overview

The identification of emergent structures in complex dynamical systems is a very difficult task with broad applications. In particular, the formation of intermediate-level dynamical structures could allow a high-level description of the organization of the system itself, and thus to its better understanding.
We here present a method based on the Relevance Index method aimed at revealing these dynamical structures (Relevant Sets, or RSs in the following).
The basic method involves two steps: (i) the detection of the candidate RSs based on the computation of the Relevance Index, and (ii) the iterated application of a process composed by a sieving action followed by the merger of the grouped variables and a new candidate RSs detection, till reaching the final grouping (composed by the “real” RSs). 
This method however requires a heavy computational cost in several real-world cases. Here we introduce a modified version of our approach, which significantly reduces the computational burden. The main approach used by the “Piecewise RI method” consists in dividing the system into sections and proceeding to the analysis of each single section, in order to reduce the number of groups to be evaluated. This procedure could divide some RS into different parts: at the end of the single analyses all the groupings found (be they the "pre-final RSs") are then collected and a final overall analysis is carried out, allowing in such a way the final merger of the erroneously separated parts into the final RSs (the “real” RSs). In this way the combinatorial explosion is greatly reduced, and so is the time necessary for the analysis.

The reference papers in which the details of the method are presented are:

Villani, M., Sani, L., Pecori, R., Amoretti, M., Roli, A., Mordonini, M., Serra R., Cagnoni, S. An iterative information-theoretic approach to the detection of structures in complex systems. Complexity 2018

D’Addese G., Sani L., La Rocca L., Serra R., Villani M. Asymptotic Information-Theoretic Detection of Dynamical Organization in Complex Systems Entropy 2021, 23(4), 398

D’Addese G., Casari M., Serra R., Villani M. A fast and effective method to identify relevant sets of variables in complex systems (submitted)

The script takes as input:

	- discretized matrix representing the data set - a matrix composed of N variables (the columns) and M observations (the rows) 
	
and give as output:

	- the file sequence.txt within the directory “final merge”, containing the final grouping
	
	- set of files and folders containing intermediate results (see details below)

The code is optimized for Python versions 3.6 or higher

## Requirements
```
pip3 install python-louvain
```

## Input
The script can take in input more files at the time. Create a folder called  ``file_to_graph``to fill with all the text files that you want to analyze.

The input files must be generated as follows:

	- first line containing the sistem element names separated by tabulation. Element names must not contain spaces or "_" (used to divide the relevant set). All the name must be unique

	- other line containing the elements expression values ​​(discretized). The order of the lines is not important. The values ​​on the row must appear in the same order as the elements in the first row.

see ``example.txt`` as an example

## Preprocessing

Before starting with the main script it is required a preprocessing step.
```
"python3 deleter.py"
```
This script searches and eliminates all the columns of the input matrix where value remains constant for the whole column. This type of elements does not bring information to the system and therefore will not join any of the relevant sets. IMPORTANT NOTE: this script will overwrite the starting file in the directory files.

After this first step is possible to proceed with the execution of the main script. from command line: 

"python3 graph.py"

## Parameter
The program supports the following options

	``-g --gruop`` takes as input an integer which is used to set the maximum size of the groups to be analyzed. The default value is 3.

	``-z --zi`` takes in a float that is used to set the zI treshold used for arrest the iterarive merge. The default value is 3.

Example:
```
"python3 graph.py -g 4 -z 2.7"
```
Once the run is complete, a folder will be created for each file in input, containing the script output.

## Output
### Base Outoup
the output is defined as follows:

	- a PNG images representing the network. the color of the node deline the division in community

	- directory ``group``  containing the output of the iterative zI * for each community found

	- post_community.txt: contains the list of relevant sets found by uniting the communities individually

	-directory ``final merge`` directory containing the output of the iterative zI * on the resulting relevant sets of the individual communities to check if there are further possible mergers. The file sequence.txt in this directory contain the final relevant sets of the sistem 

### Iterative output
 * The output of  the iterative zI is defined as follo

	- Directory ``results``: Each iteration are stored here indentified with the iteration number.  inside there are 2 text file related to that specific iteration:

		• ``file.txt``: the state of the system before the merge of the current iteration.

		• ``grind.txt``: a list of all the groups analyzed and the value of the zI calculated on them. the order of the gruop is defined by zI, sorted in descending order. This type of information is useful for taking a closer look at how the system is organized. However it turns out, most of the time, this file is really large and being able to build it for each iteration proves to be high disk-space consuming. this problem was circumvented by printing only the first 1000 most relevant groups. This value can be increased or decreased at will in the ``cacolate_zI.py`` file by changing the value of the variable at the beginning of the file ``num_line_to_print``.

	- ``sequence.txt``: the sequence of the relevant sets merging line by line. The last element of each row is the join carried out in that iteration followed by the zI value assigned to it. the last line of this file represents the last merge that was possible using the threshold provided in input. This line then represents the relevant sets of the system. In each line the relevant sets are separated by tabs. Within each relevant set the elements that compose it are separated by "_"

