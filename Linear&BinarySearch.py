#impletation of linear search alogrithm
#only for illustration as sequence types like List, Tuple, Range 
# all implements the __contains__() and 
# allows to search simply by using 'in' operator
from enum import IntEnum
from typing import List, Tuple

Nucleotide: IntEnum = IntEnum ('Nucleotide', ('A', 'C', 'G', 'T'))   #IntEnum gives us the comparsion operators
#codons are defined as triplets of nucleotides
Codon = Tuple[Nucleotide, Nucleotide, Nucleotide]
#genes are list of codons
Genes = List[Codon]

gene_str: str = "ACGTGGCTCTCTAACGTACGTACGTACGGGGTTTATATATACCCTAGGACTCCCTTTGTC"

def string_to_gene(s:str)->Genes:
    genes: Genes = []
    for i in range(0, len(s), 3):
        if (i + 2) > len(s):
            return genes
        codon: Codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        genes.append(codon)
    return genes

def linear_search(g:Genes, c:Codon)->bool:
    for codon in g:
        if codon == c:
            return True
    return False

def binary_search(g:Genes, key:Codon)->bool:
    low = 0
    high = len(g) - 1
    while low <= high:
        mid = (low + high) // 2
        if g[mid] < key:
            low = mid + 1
        elif g[mid] > key:
            high = mid - 1
        else :
            return True
    return False


if __name__ == "__main__":
    gene:Genes = string_to_gene(gene_str)
    gtc:Codon  = (Nucleotide.G, Nucleotide.T, Nucleotide.C)
    print(linear_search(gene, gtc))
    sorted_genes = sorted(gene)
    print(binary_search(sorted_genes, gtc))
    print()

