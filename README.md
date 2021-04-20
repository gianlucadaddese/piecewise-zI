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
The script can take in input multiple files at a time. Create a folder called  ``file_to_graph``to fill with all the text files that you want to analyze.

The input files must be generated as follows:

	- first row containing the system element names separated by tabulation. Element names must not contain spaces or "_" (used to divide the relevant set). All names must be unique

	- other rows containing the elements expression values ​​(discretized). The order of the rows is not important. The values on the rows must be consistent with the order of the titles (variable names) of the first row.
	
see ``example.txt`` as an example

## Preprocessing

Before starting with the main script it is required a preprocessing step.
```
"python3 deleter.py"
```
This script searches and eliminates all the columns of the input matrix where value remains constant for the whole column. This type of element does not carry information and could be included in any of the groups: it is therefore better that it be eliminated. IMPORTANT NOTE: this script will overwrite the starting file in the directory files.

After this first step is possible to proceed with the execution of the main script. Type on the command line: 

"python3 graph.py"

## Parameter
The program supports the following options

	``-g --gruop`` takes as input an integer which is used to set the maximum size of the subsets  to be analyzed. The default value is 3.

	``-z --zi`` takes in a float that is used to set the zI threshold  used to stop the iterative  merge. The default value is 3.0.

Example:
```
"python3 graph.py -g 4 -z 2.7"
```
Once the run is complete, a folder will be created for each file in input, containing the script output.

## Output
### Base Outoup
the output is defined as follows:

	- a PNG images representing the network. The color of the nodes allows to identify the division in the community

	- directory ``group``  containing the output of the iterative zI * for each community found

	- ``post_community.txt``: containing the list of relevant sets found by examining each partition individually

	- The ``final merge'' folder containing the union of the zI* outputs obtained from the individual parts, in order to verify the possibility of further mergers The file sequence.txt in this directory contain contains the final relevant sets of the sistem system 

### Iterative output
 * The output of  the iterative zI is defined as follows

	- Directory ``results``: Each iteration is stored in a dedicated folder, identified by the iteration number. Inside the folder there are two files:

		• ``file.txt``: the state of the system before the merge of the current iteration.

		• ``grind.txt``: a list of all the groups analyzed and the value of the zI calculated on them. The order of the group  is defined by zI, sorted in descending order. This type of information is useful for taking a closer look at how the system is organized. However, in many cases it could happen that the file is very large: in this case, creating it at each iteration can involve a high consumption of disk space. This problem can be circumvented by printing only the first 1000 most relevant groups. This value can be increased or decreased at will in the ``cacolate_zI.py`` file by changing the value of the variable at the beginning of the file ``num_line_to_print``.

	- ``sequence.txt``: the sequence of RSs groupings at each iteration. The second-last element of each row is the the join carried out in that iteration, followed by zI value assigned to it. The last line of this file represents the last merge that was possible using the threshold provided in input. This line then represents the relevant sets of the system. In each line the relevant sets are separated by tabs. The elements that form each RS are separated by the character "_"

