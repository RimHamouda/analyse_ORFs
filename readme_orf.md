# Détection d'ORFs et Traduction en Protéines

Ce script Python permet de :

1. Lire une séquence ADN depuis un fichier FASTA,
2. Identifier les cadres de lecture ouverts (ORFs),
3. Traduire ces ORFs en séquences protéiques,
4. Sauvegarder les protéines obtenues dans un fichier texte.

# Fichier d'entrée

Le script attend un fichier FASTA ("genome_test.fasta") contenant une séquence ADN.

Exemple de contenu :


>sequence_exemple
ATGCGTACGTTAGCGTAAATGTAG


# Fonctionnalités

## "lire_sequence(nom_fichier)"

* Lit un fichier FASTA.
* Ignore les lignes commençant par ">".
* Retourne la séquence ADN en majuscules.

## "trouver_orfs(nom_sequence)"

* Recherche les ORFs (Open Reading Frames) dans les 3 cadres de lecture directs.
* Un ORF commence par "ATG" et se termine par un codon stop ("TAA", "TAG", "TGA").
* Retourne une liste des ORFs trouvés.

## Traduction en protéines

* Utilise "Bio.Seq.Seq.translate" de Biopython pour convertir chaque ORF en protéine (arrêt à la première occurrence d'un codon stop).
* Sauvegarde les protéines traduites dans "proteines_sav.txt".

## Dépendances

Le script nécessite **Biopython** :

Dans bash :
pip install biopython


## Exécution

Assurez-vous d'avoir un fichier "genome_test.fasta" dans le même répertoire. Puis, exécutez :

Dans bash:
python script.py


## Sortie

Les protéines traduites seront enregistrées dans "proteines_sav.txt" :


Protéine 1 : MR
...

##  Auteure

Rim Hamouda 

[🔗 https://www.linkedin.com/in/rim-hamouda-b33992214/) | (https://github.com/RimHamouda)
