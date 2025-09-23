#!/usr/bin/env python3

taxa = "sapiens, erectus, neanderthalensis"
print(taxa)
print(taxa[1])
print(type(taxa))

print(taxa.split(", "))

species = taxa.split(", ")

print(species)

print(species[1])

print(type(species))

print(sorted(species))

print(sorted(species, key=len))
