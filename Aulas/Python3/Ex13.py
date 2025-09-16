#!/usr/bin/env python3

dna = "GATGGGATTggggttttccccTCCCATGTGCTCAAGACTGGCGCTaaaaGttttGAGCTTCTCaaaaGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCggggACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGccccCTCTGAGTCAGGAAACAttttCAGACCTATGGAAACTACTTCCTGaaaaCAACGTTCTGTccccCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTccccGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTccccCCGTGGccccTGCACCAGCAGCTCCTACACCGGCGGccccTGCACCAGccccCTCCTGGccccTGTCATCTTCTGTCCCTTCCCAGaaaaCCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTccccTGCCCTCAACAAGATGttttGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACAccccCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGccccCACCATGAGCGCT"

dna = dna.upper() #DNA corrigido para ficar todo em maiúscula

#Substituindo os nucleotídeos por seus complementares (minúscula temporária para evitar problemas)
comp_dna = dna.replace("G","c")
comp_dna = comp_dna.replace("C","g")
comp_dna = comp_dna.replace("A","t")
comp_dna = comp_dna.replace("T","a")

comp_dna = comp_dna.upper() #voltando a sequência à maiúscula

#Fazendo o complemento reverso
rev_comp_dna = comp_dna[::-1]

#Imprimindo bonito
print("{:<20} 5' {} 3'".format("Sequência Original", dna[:20]))
print("{:<20} 3' {} 5'".format("Complemento", comp_dna[:20]))
print("{:<20} 5' {} 3'".format("Complemento Reverso", rev_comp_dna[:20]))
