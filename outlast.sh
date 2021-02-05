#!/bin/bash
for i in 10
do
	#x=$((386+$i))
	let "n = 386 + $i"
	tail -n $n $i.xyz > last$i.xyz
done
