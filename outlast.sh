#!/bin/bash
for i in {1..100}
do
	x=$((386+$i))
	let "n = 386 + $i"
	tail -n $n $i.xyz > $(i)last.xyz
done
