import time

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


def makeProbeDictionary():
	# todo: handle same subsequence in multiple probes
	
	f=open("ProbeRegionSeqsA.fasta", 'r')
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
probeDict = makeProbeDictionary()
t2=time.time()
Time1=t2-t1
print Time1

# open reads file
f=open("ProbeRegionSeqsX.fasta", 'r')
outFile = open("seqsA2X.outputs",'w')
matchCount=0
t1=time.time()
while True:
	Name=f.readline()				# keep name
	seq=f.readline().strip()		# keep seq (100 chars), but cut off whitespace
	#blank=f.readline()				# pitch third line
	#quality=f.readline()			# pitch fourth line
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


#print entire countdictionary for the line.
	
	# could change this to write out number of matches from every probe sequence?
	#outFile.write( "\n"+ Name + " " + str(countDict) + "\n")
	outFile.write(Name + "\n" + bestMatch + " " + str(bestCount) + "\n")
	
	if Name[:-3]==bestMatch[:-1]:
		matchCount=matchCount+1
	#print bestMatch[:-1] 
	#print str(matchCount)


f.close()
outFile.close()
t2=time.time()
Time2=t2-t1
print Time2

print  matchCount/512.0


# make a loop to get a ten letter chunk out of the seq
# move one at a time, check each subsequence
# list of match counts same length as probeDict values
# have a counter for each one of the names of the probe sequences
# want to count how many times it looks up each one
# Make a dictionary with each of the seqs as keys and integer as value
# write to file the number of matches (counts) and where they mantch (most)


'''
print name from big file
and which of those (probname) that has the highest count
go through 
countdict.iteritems will give you tuple names and name
find which has the highest count
and will give you most matches
'''
# look up dictionary.iteritems 
#print name with biggest count and that count

# to look at the first few lines of a file
# Use "head" in the command line