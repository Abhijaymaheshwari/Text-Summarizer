
import math
from preprocess import readData
import operator
import sys


data=[]
final_list=[]
finaldata=[]
sorted_x=[]

class Node:


	def __init__(self,name,count):
		self.name=name
		self.position=count
		self.PRscore=0


	def __repr__(self):
		return self.name

	def __eq__(self, other):
		return self.name == other.name

	def __hash__(self):
		return hash(self.name)



class Graph:
	
	def __init__(self):
		self.structure={}
		self.nodeHash = {}

	def printStructure(self):
		for key in self.structure:
			print(key.name.encode('utf-8'),key.PRscore)

	def similarity(self,si,sj):
		
		si1=set(si)
		sj1=set(sj)
		return len(si1.intersection(sj1))/(math.log(len(si))+math.log(len(sj)))

	def setNode(self,word,count):
		if word in self.nodeHash:
			node = self.nodeHash[word]
		else:
			node = Node(word,count)
			self.nodeHash[word] = node
		return node

	def set_structure(self,wordlist):
		
		count=0
		structure=self.structure
		for sentence in wordlist:
			count+=1
			curr_node=self.setNode(sentence,count)
			for j in range(len(wordlist)):
				next_node=self.setNode(wordlist[j],j+1)
				#print next_node, curr_node
				if(next_node == curr_node):
					continue
				if curr_node not in structure:
					structure[curr_node]={}
					structure[curr_node][next_node]=self.similarity(sentence,wordlist[j])
					#print self.similarity(sentence,wordlist[j])
				else:
					structure[curr_node][next_node]=self.similarity(sentence,wordlist[j])
				# 	print self.similarity(sentence,wordlist[j])
				# raw_input()
		# for key in self.structure:
		# 	for value in self.structure[key]:
		# 		print key.name.encode('utf-8'),value.name.encode('utf-8'),self.structure[key][value]


	def sort_nodes_textsummarize(self,m):
		
		global final_list,sorted_x
		final_list = sorted(self.structure.keys(), key=operator.attrgetter('PRscore'),reverse=True)[:m]
		sorted_x = sorted(final_list, key=operator.attrgetter('position'))
		# print
		result=[]
		for i in range(1,len(sorted_x)):
			result.append(sorted_x[i].name)

		#print result
		return result


	1


def textSummarizeMain(input_file,m):
	global countWords,data,finaldata

	print("Running default TextRank on", input_file,"....")

	graph=Graph()
	data,finaldata,countWords=readData(input_file)
	# print finaldata
	# print countWords
	# raw_input()
	countWords=len(finaldata)
	graph.set_structure(finaldata)
	graph.textSummarize()
	print("Finished TextRank.")
	return graph.sort_nodes_textsummarize(m)
