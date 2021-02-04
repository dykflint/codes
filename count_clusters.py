import math
from collections import defaultdict
import os
import re
import sys

if len(sys.argv) != 2:
    print("USAGE: python3 cluster.py xyz-file (and maybe height criterium)")
    sys.exit(0)

xyzfile = sys.argv[1]

with open(str(xyzfile), "r") as f:
    tmp = [line.split() for line in f][2:]
    lines = [line for line in tmp if float(line[3])>12.0] 
    numerated_lines = [i for i in range(len(lines))]

#print(numerated_lines)       


#? Calculate the distances between the atoms on the surface
count = 0
try:
    os.remove("islands.txt")
except OSError:
    pass

file = open("out.txt","a")
tmp = open("islands.txt", "a")
clusters = defaultdict(list)
dclusters = defaultdict(list)
for line in lines:
    in_count = 0
    se_count = 0
    j=0
    tmp.write(str(line))
    tmp.write("\n              ")
    for i in range(len(lines)):
        dist = math.sqrt((float(lines[count][1])-float(lines[i][1]))**2+(float(lines[count][2])-float(lines[i][2]))**2+(float(lines[count][3])-float(lines[i][3]))**2)
        if dist < 2.65:
            if lines[i][0] == "In":
                in_count += 1
            else:
                se_count += 1
            clusters[count] += [lines[i]]
            dclusters[count] += [numerated_lines[i]]
            j += 1

    tmp.write("\n")
    #print(j)
    count += 1

#print(dclusters)

tmp.close()


#TODO: merge keys with common values of cluster dict

d = dclusters
processed = set([None])
while processed:
    dict_out = {}
    processed = set()
    for k1, v1 in d.items():
        if k1 not in processed:
            vo = v1
            for k2, v2 in d.items():
                if k1 is not k2 and set(vo) & set(v2):
                    vo = sorted(list(set(vo + v2)))
                    processed.add(k2)
            dict_out[k1] = vo
    d = dict_out
#print(d)
#print(len(d))
converted_d = d.copy()
#? Convert the numerical signature into its original xyz coordinates with the element name at the beginning
for key, value in converted_d.items():
    for i in range(len(value)):
        value[i] = lines[value[i]]
    #print(value)
#print(converted_d)
#? Get the composition of the clusters using the dict of the converted dict
cluster_composition = defaultdict(list)
for key, value in converted_d.items():
    in_cluster = 0
    se_cluster = 0
    for i in range(len(value)):
        if value[i][0] == "In":
            in_cluster += 1
        else:
            se_cluster += 1
    if (in_cluster + se_cluster) > 1: # only include clusters of sizes containing more than one atom
        cluster_composition[key] = "In"+str(in_cluster)+"Se"+str(se_cluster)  
    
#? Create the dict giving the number of same kind clusters
#test = {0: "In1Se1", 1: "In1Se1"}
num_dist_clusters = defaultdict(list)
for key, value in cluster_composition.items():
    if value not in num_dist_clusters:
        num_dist_clusters[value] = 1
    else:
        num_dist_clusters[value] += 1

#? Number of the clusters in num_dist_clusters
total_number = 0
for key, value in num_dist_clusters.items():
    total_number += value

print("xyz-file ",str(xyzfile), "has the following clusters:\n")
#print(cluster_composition)
print(num_dist_clusters)
print("\n i.e. #/MoSe2 surface:",total_number)