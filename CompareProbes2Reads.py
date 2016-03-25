import time
import sys

try:
	probeFile= str(sys.argv[1])
	outputFile= str(sys.argv[2])
except:
	print "file not found"

def chunkComplement(aString):
	# need a reverse comlement change A ==> Z, T to A, Z ==> T
	# Then C==> X, G to C, X==>G
	aString.replace("A","Z")
	aString.replace("T","A")
	aString.replace("Z","T")
	aString.replace("C","X")
	aString.replace("G","C")
	aString.replace("X","G")
	return aString


def makeProbeDictionary(probeFile):
	# todo: handle same subsequence in multiple probes
	
	f=open(probeFile, 'r')
	lines=f.readlines()									# 512 names and sequences
	f.close()
	
	#now we have a list where each element in the list is a linenexgen
	locusNames=[line.strip() for line in lines[0::2]] 	# location, white space stripped
	sequences=[line.strip() for line in lines[1::2]]  	# probe sequence
	probeDict=dict() #creates empty dictionary
	
	for name,seq in zip(locusNames,sequences):			# go through each of the sequences 
		#10 digit sequence keys, and locus name (L1x) as value # subsequence points to a locus name
		chunks=[seq[i:i+10] for i in range(0,len(seq),10)] #will that chop off the end?
		for chunk in chunks:
			probeDict[chunk]=name
			probeDict[chunkComplement(chunk)]=name
			# probeDict[chunk[::-1]]=name
			# doing sequence[::-1] reverses a sequence, but need complement as well
	return probeDict
	
t1=time.time()	
probeDict = makeProbeDictionary(probeFile)
t2=time.time()
Time1=t2-t1
print Time1

# open reads file
f=open("s_9_900_U1.fastq", 'r')
outFile = open(outputFile,'w')

t1=time.time()
while True:
	Name=f.readline()				# keep name
	seq=f.readline().strip()		# keep seq (100 chars), but cut off whitespace
	blank=f.readline()				# pitch third line
	quality=f.readline()			# pitch fourth line
	if Name == '' or seq =='':		# Empty line means end of file
		break
	
	countDict=dict()				# reset counts
	
	for i in range(0,len(seq)-10):
		subseq=seq[i:i+10]
		try:
			probeName=probeDict[subseq]
		except KeyError:
			probeName = None
		
		if probeName is not None:
			#increase counter for name
			countDict[probeName] = countDict.setdefault(probeName,0)+1

	# find which probe sequence had the most matches
	bestMatch = "None"
	bestCount = 0
	for locus, count in countDict.iteritems():
		if count == bestCount:
			bestMatch = "None"
			'''remove None?'''
		if count > bestCount:
			bestMatch = locus # locus that matches the most 
			bestCount = count
	
	outFile.write(Name+ "\n")
	outFile.write("{'"+ bestMatch + "': " + str(bestCount) + "}" + "\n")
	
f.close()
outFile.close()
t2=time.time()
Time2=t2-t1
print Time2