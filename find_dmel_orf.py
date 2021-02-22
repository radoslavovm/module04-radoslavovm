#!/usr/bin/env python3

## Read Drosophila genome 
# Imports
import re
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio import SeqIO
from Bio.Alphabet import IUPAC

# Only for the full chromosomes 
infile = "/scratch/Drosophila/dmel-all-chromosome-r6.17.fasta"

for record in SeqIO.parse(infile, "fasta"):
        if re.match("^\d{1}\D*$", record.id):
            dna = record.seq
            rna = dna.transcribe()
            result = re.search('AUG([AUGC]{3})+?(UAA|UAG|UGA)', str(rna)).group()
            orf = Seq(result)
            protein = orf.translate()
            print(protein)

