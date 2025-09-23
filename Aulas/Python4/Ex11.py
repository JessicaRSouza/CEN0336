#!/usr/bin/env python3

sequencias = ['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']

for seq in sequencias:
	print(seq)

for seq in sequencias:
	print("{:<4}{}".format(len(seq),seq))
