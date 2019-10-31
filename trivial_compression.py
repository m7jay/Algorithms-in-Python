#program to implement a simple compression and decompression
from sys import getsizeof
from typing import Dict
class GeneCompression:
    """
    class with compression and decompression behaviors
    """
    Nucleotide_to_Bits: Dict[str:int] = {"A":0, "T":1, "G":2, "C":3}
    Bits_to_Nucleotide: Dict[int:str] = {0b00:"A", 0b01:"T", 0b10:"G", 0b11:"C"}

    def __init__ (self,gene:str)->None:
        """
        constructor for GeneCompression class
        it initializes the class with the compressed string
        params:
        gene        the string to be compressed
        """
        self._compress (gene)

    def _compress (self,gene:str)->None:
        """
        function to compress a string into bits  {"A" : 0, "T" : 1, "G" : 2, "C" : 3}
        params:
        gene        the string to be compressed
        """
        self.bit_string:int = 1
        for nucleotide in gene.upper ():
            self.bit_string <<= 2
            try:
                self.bit_string |= self.Nucleotide_to_Bits.get (nucleotide)
            except KeyError:
                print ("Invalid Nucleotide :{}".format (nucleotide))

    def decompress (self)->str:
        """
        function to decompress the string
        retunrs the decompressed string
        """
        gene:str = ""
        for i in range (0, self.bit_string.bit_length ()-1, 2):
            bits: int = self.bit_string >> i & 0b11
            try:
                gene += self.Bits_to_Nucleotide.get (bits)
            except KeyError:
                print ("Invalid bits :{}".format (bits))
        return gene[::-1]

    def __str__ (self):
        return  self.decompress ()

original:str = "TAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATATAGGGATTAACCGTTATATATATATAGCCATGGATCGATTATA" * 100
print ("Original is {} bytes.".format (getsizeof (original)))
compressed: GeneCompression = GeneCompression (original)
print ("Compressed is {} bytes".format (getsizeof (compressed.bit_string)))
print (compressed)
print ("Original and the decompressed strings are the same: {}".format (original == compressed.decompress ()))
