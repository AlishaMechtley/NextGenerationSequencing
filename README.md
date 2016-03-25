Assembly of Anchored Hybrid Enrichment Data
===========================================


### Background


Sequence assembly is the aligning and merging of fragments of a DNA sequence in order to reconstruct that sequence. For this project, the fragments (reads) are the result of utilizing enrichment probes of highly conserved regions to capture more rapidly evolving adjacent regions (anchored enrichment) and sequencing the resulting fragments using high-throughput sequencing. The probes were specifically designed for target enrichment of over 500 loci in highly conserved anchor regions of vertebrate genomes. The loci were chosen by the deveoper of Anchored Phylogenomics, Dr. Alan Lemmon, to be conserved in the middle and not conserved on the outside.


 ![Figure1](https://raw.githubusercontent.com/AlishaMechtley/NextGenerationSequencing/master/images/ProbePic.png)
 
*Figure 1: More than 500 probe sequences from highly conserved anchor regions of vertebrate genomes are used to map the forward reads. Only those forward read regions that line up with the probe region of the target sequence are investigated in this project.*


### Methods
I was given two types files to work with, a large file containing the forward reads and several smaller files containing the probe regions.


### Input Files

 ![Input Files](https://raw.githubusercontent.com/AlishaMechtley/NextGenerationSequencing/master/images/InputFiles.png)
 
*Figure 2: The two types of files to compare are the Pseudacris feriarum forward reads file in FASTQ format (left) and the FASTA files of probe sequences for various vertebrates (right).*

I wrote three programs to compare the files.  One program compares reads to probes and prints out the best match for each read. To run the program, type or paste into the command line:

```$ python CompareProbes2Reads.py ProbeRegionSeqsX.fasta seqsX.outputs```

The second argument (ProbeRegionSeqsX.fasta) is the name of the probe to compare to the forward reads and the second argument (seqsX.outputs) can be any name to give to the output file. The program takes 0.038 seconds to create the probe dictionary and another 1775.9 seconds (half an hour) to compare the probe dictionary to the reads and print the best match results for each read to the output file.The second program compares probes to probes and prints out the total percentage of loci that match to the command line. To run the program, type or paste into the command line: 

```$ python CompareProbes2Probes.py```

The match results for each individual locus are printed to an output file that is named within the program (e.g., seqsA2G.outputs). It takes approximately 0.06 seconds to create the dictionary and 0.27 seconds to compare the dictionary to the probe sequences you are comparing to.
 
### Output Files
 
The seqsX.outputs file

```
@HWI-ST1035:54:D03ERACXX:4…

{'>L221X': 1}

@HWI-ST1035:54:D03ERACXX:4:1101:…

{'>L89X': 1}

@HWI-ST1035:54:D03ERACXX:4:1101:…

{'None': 1}
```

The seqsA2G.outputs files resulting from the comparison programs

```
>L1G 10

>L2G None

>L3G NONE

>L4G 1
```

The third program takes the results of the first program and uses it to create a plot of the number of reads that map to each locus, placing them in increasing order of magnitude. To run the program, type into the command line:

```$ python probeStats seqsX.outputs```

This third program takes about 4½ minutes to run and produces two graphs: 1) a plot of the total number of matches for all reads vs. the individual loci and 2) a plot of the highest number of matches for a single read for each loci.

 
### Results

*Figure 3: Total number of matches for each read* 

 ![Results Figure 3](https://raw.githubusercontent.com/AlishaMechtley/NextGenerationSequencing/master/images/NumMatchesVsLoci_Sorted.png)



*Figure 4: The best number of matches for a single read shown in ascending order for each individual loci.*

 ![Results Figure 4](https://raw.githubusercontent.com/AlishaMechtley/NextGenerationSequencing/master/images/bestMatches.png)


The next result is a table of the percentage of loci that match for the two probe files
(A=Anolis, Z=Danio, G=Gallus, H=Homo, X=Xenopus).

|               | A             | G            | H           |      X      |       Z      |
| ------------- |:-------------:|:------------:|:-----------:|:-----------:|-------------:|
| A	            |   1.0	        | 0.6484375	   | 0.4296875   | 0.289062    | 0.140625     |
| G	            |   0.65234375	| 1.0	       | 0.5859375   | 0.328125    | 0.16796875   |
| H	            |   0.44921875	| 0.568359375  | 1.0	     | 0.255859375 | 0.14453125   |  
| X	            |   0.302734375	| 0.322265625  | 0.2421875   | 1.0	       | 0.13671875   |
| Z	            |   0.142578125	 | 0.181640625 | 0.146484375 | 0.134765625 | 0.99609375   |


*Table 1: Percentage of matching loci (compareProbe2Probes.py)*

Taking the complement of each percentage, I get the following table. This table resembles a cophenetic (adjacency) matrix.

|               | A             | G            | H           |      X      |       Z      |
| ------------- |:-------------:|:-------------:|:-------------:|:-----------:|-------------:|
| A	            | 0	            | 0.3515625	    | 0.5703125	    | 0.7109375	  | 0.859375     |
| G	            | 0.34765625	| 0	            | 0.4140625	    | 0.671875	  | 0.83203125   |
| H	            | 0.55078125	| 0.431640625	| 0  	        | 0.744140625 | 0.85546875   | 
| X	            | 0.697265625	| 0.677734375	| 0.7578125	    | 0	          | 0.86328125   |
| Z	            | 0.857421875	| 0.818359375	| 0.853515625	| 0.865234375 | 0.00390625   | 
*Table 2 : Complement of the percentage of matches.*

### Discussion

Although there is a simple way to convert a tree to a cophenetic matrix in the ape package of R, I did not find a simple way to do the reverse: convert a cophenetic matrix to a tree. I decided to simply compare the values to what I expect. The “distances” in Table 2 are smallest between Anolis and Gallus and they are largest between Danio and every other Genus as is expected.


 ![Discussion Figure 5](https://raw.githubusercontent.com/AlishaMechtley/NextGenerationSequencing/master/images/Tree3.png)
Note: I would like to change the size of the sequence that I am sliding across the probes and reads and see how it affects the results. 
