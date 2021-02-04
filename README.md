# codes
Instructions for some of the codes here:

count_clusters.py: Input is an xyz file (no md trajectory - although in that case one can simply loop through the trajectory and at each frame apply the code). This was done with surfaces in mind. In those cases we don't want to include the surface atoms as atoms in the cluster calculation. Thus, we give it the height of the top-most surface atoms and let the code only handle the atoms above that height. The code calculates all nearest-neighbours of every atom (default value is 2.65Angström sphere around the atom) and if any of these clusters overlap they are merged into a bigger cluster containing both parties.
USAGE: python3 count_clusters.py xyz-file (you can change the code accordingly to also have the surface height as a parameter).
