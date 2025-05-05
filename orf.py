def lire_sequence(nom_fichier):
    file=open(nom_fichier)
    lines= file.readlines()
    sequence = " "
    for lig in lines:
        lig = lig.rstrip()
        if not lig.startswith('>'):
            sequence +=lig
    return sequence.upper()

seq=lire_sequence("genome_test.fasta")
#print(seq)

def trouver_orfs(nom_sequence):
    list_orfs =[]
    stop_codons = ['TAA', 'TAG', 'TGA']
    
    for frame in range(3):# 3 frames : 0, 1, 2
        seq_frame = nom_sequence[frame : ]
        
        #parcourir la séquence par groupe de codons(longueur 3)
        for i in range(0, len(seq_frame)-2, 3):
            
            codon = seq_frame[i:i+3]
            if codon =='ATG': #codon de départ
                
            
                #boucle de recherche du codon stop
                #2ème compteur par groupe de 3 à partir du codon ATG trouvé
                for j in range(i+3, len(seq_frame)-2, 3):
                    stop= seq_frame[j: j+3]
                    if stop in stop_codons:
                   
                        orf= seq_frame[i:j+3]
                        #récupérer l'orf dans une liste
                        list_orfs.append(orf)
                        break #ne pas chercher d'autres ORF car biologiquement c'est incorrect
  
    return (list_orfs)
        
        
    

orfs=trouver_orfs(seq)
print(orfs)


#importer Seq de biopython
from Bio.Seq import Seq
#traduire les ORFS obtenus
proteines = []
for i, orf in enumerate(orfs):
    prot = Seq(orf).translate(to_stop=True)
    proteines.append(prot)

    #sauvegarde des proétines dans un fichier
    with open("proteines_sav.txt", "w") as fichier:
        for i, prot in enumerate(proteines):
            fichier.write(f"Protéine {i+1} : {prot}\n")
            
    
