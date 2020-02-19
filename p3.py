#biopython 2| biopython_2.py
import Bio.Alphabet
from Bio.Alphabet import IUPAC
from Bio.Seq import Seq

pro_extend_dna=IUPAC.ExtendedIUPACProtein.letters;
print(pro_extend_dna);
print("\n"); 

seq1=Seq('CCGGGTT',Bio.Alphabet.IUPAC.unambiguous_dna);
print(seq1);

seq_transcribe=seq1.transcribe();
print(seq1.transcribe());

seq_translate=seq1.translate();
print(seq1.translate());

rna_seq=Seq('CCGGGUU',Bio.Alphabet.IUPAC.unambiguous_rna);
print(rna_seq);

rna_transcribe=rna_seq.transcribe();
print(rna_transcribe);

rna_translate=rna_seq.translate();
print(seq_translate);

