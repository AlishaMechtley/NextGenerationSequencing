import ast	#abstract syntax trees
import matplotlib.pyplot
import sys

try:
	outputFile= str(sys.argv[1])
except:
	outputFile= "seqsX2.outputs"
	
def makeCountDictionary(outputFile):
	# todo: handle same subsequence in multiple probes
	locusDict=dict() # creates empty dictionary for file data
	countDict=dict() # all matches for all reads
	bestCounts=dict() # highest number of matches for a single read
	f=open(outputFile,'r')
	
	for line in f:			# go through each of the sequences 
		#line=f.readline()									# 512 names and sequences
		if "{" not in line:
			continue
		loci=line.strip()  	# probe sequence
		locusDict =  ast.literal_eval(loci)
		for key,value in locusDict.iteritems():
			countDict[key] = countDict.setdefault(key,0)+value
			if bestCounts.setdefault(key,0)<value:
				bestCounts[key]=value
	f.close()
	return countDict, bestCounts
			
			
# number 20 mean we found all of the forward and all of the complementary sequences?

countDict, bestCounts = makeCountDictionary(outputFile)
print countDict
# countDict.values() vs countDict.keys() using ticklabels?
del countDict['None']
matplotlib.pyplot.bar(range(len(countDict)),sorted(countDict.values()))
matplotlib.pyplot.xlabel("Loci")
matplotlib.pyplot.ylabel("Total Number of Matches")
matplotlib.pyplot.show()


matplotlib.pyplot.bar(range(len(bestCounts)),sorted(bestCounts.values()))
matplotlib.pyplot.xlabel("Loci")
matplotlib.pyplot.ylabel("Best number of Matches for a Single Read")
matplotlib.pyplot.show()





