#!/usr/bin/python

__author__		= "Sander Granneman"
__copyright__	= "Copyright 2021"
__version__		= "0.0.1"
__credits__		= ["Sander Granneman"]
__maintainer__	= "Sander Granneman"
__email__		= "sgrannem@ed.ac.uk"
__status__		= "beta"

##################################################################################
#
#	pyGTF2Fasta.py
#
#
#	Copyright (c) Sander Granneman 2021
#
#	Permission is hereby granted, free of charge, to any person obtaining a copy
#	of this software and associated documentation files (the "Software"), to deal
#	in the Software without restriction, including without limitation the rights
#	to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#	copies of the Software, and to permit persons to whom the Software is
#	furnished to do so, subject to the following conditions:
#
#	The above copyright notice and this permission notice shall be included in
#	all copies or substantial portions of the Software.
#
#	THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#	IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#	FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#	AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#	LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#	OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
#	THE SOFTWARE.
#
##################################################################################

import sys
import re
from optparse import *
from pyCRAC.Parsers import GTF2
from pyCRAC.Parsers.GTF2 import GenomeSeq
from pyCRAC.Classes.NGSFormatReaders import NGSFileReader

def gtf2Fasta(gtf_file,fasta_file,outfile=None,sequence_type="DNA"):
    """ converts 1-based inclusive gtf files to fasta files. Keeps the chromosome,
    gene_name, start and end coordinates and strand in the header
    of the fasta file for each sequence. You can also convert the
    sequence to RNA by setting type='RNA'. """

    gtfreader = NGSFileReader(gtf_file)
    genome = GenomeSeq()
    genome.read_FASTA(fasta_file)

    if outfile:
        out = open(outfile,"w")
    else:
        out = sys.stdout

    while gtfreader.readGTFLine():
        chromosome = gtfreader.chromosome
        start = gtfreader.start
        end = gtfreader.end
        strand = gtfreader.strand
        gene_name = gtfreader.gene_name
        sequence = genome.sequence(chromosome,strand,start+1,end+1).upper() # Convert back to 1-based coordinates
        if sequence_type == "RNA":
            sequence = sequence.replace("T","U")
        header = ":".join([gene_name,chromosome,str(start),str(end),strand])
        out.write(">%s\n%s\n" % (header,sequence))

    out.close()
    return True

def main():
    parser = OptionParser(usage="usage: %prog [options] --gtf gtf_file.gtf -g yeast_genome.fa", version="%s" % __version__)
    files = OptionGroup(parser, "File input options")
    files.add_option("--gtf",
                    dest="gtf_file",
                    metavar="Yourfavoritegtf.gtf",
                    help="type the path to the gtf file that you want to convert. Default is standard input",
                    default=None)
    files.add_option("-g",
                    dest="genome_file",
                    metavar="yeast.fa",
                    help="The fasta file of your strain/organisms genome sequence",
                    default=None)
    files.add_option("-o",
                    "--outfile",
                    dest="outfile",
                    metavar="converted.fasta",
                    help="type the name and path of the file you want to write the output to. Default is standard output",
                    default=None)
    files.add_option("--RNA",
                    dest="RNA",
                    help="Use this flag if you want to convert the sequences in the fasta file to RNA. Default is DNA",
                    action="store_true",
                    default=False)
    parser.add_option_group(files)
    (options, args) = parser.parse_args()

    seq_type = "DNA"
    if options.RNA:
        seq_type = "RNA"

    gtf2Fasta(options.gtf_file,options.genome_file,options.outfile,sequence_type=seq_type)

if __name__ == "__main__":
	main()
