#  File: Books.py

#  Description: Program calculates the frequency of words in a novel and compares it to other authors. Input is a text file 
#  containing a novel and the program outputs the frequency of each word in the novel and compares it to another author

#  Student Name: Brian Tsai

#  Student UT EID: byt76

#  Partner Name: N/A

#  Partner UT EID: N/A

#  Course Name: CS 303E

#  Unique Number: 51850

#  Date Created: 5/5/17

#  Date Last Modified: 5/5/17

# Create word dictionary from the comprehensive word list 
word_dict = {}
def create_word_dict ():
	dictionary = open("words.txt", "r")
	# Go through each word and add it to the dictionary
	for word in dictionary:
		word = word.strip()
		word_dict[word] = 1
	dictionary.close()	

# Removes punctuation marks from a string
def parseString (st):
	newString = ""

	# Remove all punctuations except the apostrophes from the string
	for index in range(len(st)):
		
		# Add the character if it is an alphabet
		if (st[index].isalpha() == True or st[index] == "'"):
			newString = newString + st[index]
		
		# Else, replace the character with a space	
		else:
			newString = newString + " "	

	# Remove all apostrophe 's'
	newString.replace("'s", " ")
	finalString = ""
	
	# Remove all the apostrophe if it is not part of 's
	for index in range(len(newString)):
		# Replace the apostrophe with a space if it is by itself
		if (newString[index] == "'" and newString[index + 1] == " "):
			finalString = finalString + " "
		# Else, add the character
		else:
			finalString = finalString + newString[index]		
	
	# Return the corrected string
	return finalString			

# Returns a dictionary of words and their frequencies
def getWordFreq (file):

	book = open(file, "r", encoding='utf8')
	frequency_dict ={}
	
	# Parse each string into a dictionary of words and number of times it occurs
	for line in book:
		line = line.strip()
		
		# Parse the string
		line = parseString(line)
		word_list = line.split()
		
		# Add the word to the frequency dictionary
		for word in word_list:	
			# If the word is in the dictionary, increase the word frequency
			if (word in frequency_dict):
				frequency_dict[word] = frequency_dict[word] + 1
			# Else, create a new entry for the word if it doesn't exist	
			else:
				frequency_dict[word] = 1


	capital_list = []
	# Add all the capital words to a list
	for word in frequency_dict:
		if (word[0].isupper() == True):
			capital_list.append(word)
			
	
	# Remove all capital words from the frequency dictionary
	for word in capital_list:
		
		# If the word exists in the frequency dictionary, then add the capital word frequency to the lower case dictionary frequency
		if (word.lower() in frequency_dict):
			frequency_dict[word.lower()] = frequency_dict[word.lower()] + frequency_dict[word]
			del frequency_dict[word]
		
		# If the word is in the word dictionary, then add a new entry
		elif (word.lower() in word_dict):
			frequency_dict[word.lower()] = frequency_dict[word]
			del frequency_dict[word]
		
		# Else remove the capital word from the frequency dictionary
		else:
			del frequency_dict[word]	
	book.close()

	#for word in frequency_dict:
	#	print(word, frequency_dict[word])
	return frequency_dict					
  
# Compares the distinct words in two dictionaries
def wordComparison (author1, freq1, author2, freq2):
	
	set1 = set()
	set2 = set()
	
	# Create a new set from the first dictionary
	for word in freq1:
		set1.add(word)
	
	# Create a new set from the second dictionary 
	for word in freq2:
		set2.add(word)
	
	# Create a set of all words in set 1 not in set2 
	unused_words1 = set1 - set2

	# Create a set of all words in set2 not in set1
	unused_words2 = set2 - set1
	
	# Count the number of words used in the first dictionary
	total_words1 = int(sum(freq1.values()))

	# Count the number of words used in the second dictionary
	total_words2 = int(sum(freq2.values()))
	total_unused_words1 = 0
	

	# Count the number of words used in set1 not in set 2
	total_unused_words2 = 0
	for word in unused_words1:
		total_unused_words1 += freq1[word]

	# Count the number of words used in set2 not in set 1	
	for word in unused_words2:
		total_unused_words2 += freq2[word]

	unused_words1 = sorted(unused_words1)
	unused_words2 = sorted(unused_words2)


	# Format the output
	print()
	print(author1)
	print("Total distinct words =", len(freq1))
	print("Total words (including duplicates) =", sum(freq1.values()))
	print("Ratio (% of total distinct words to total words) =", format(len(freq1)/sum(freq1.values())*100, "0.10f"))

	print()
	print(author2)
	print("Total distinct words =", len(freq2))
	print("Total words (including duplicates) =", sum(freq2.values()))
	print("Ratio (% of total distinct words to total words) =", format(len(freq2)/sum(freq2.values())*100, "0.10f"))

	print()
	print(author1, "used", len(unused_words1), "that", author2, "did not use.")
	print("Relative frequency of words used by", author1, "not in common with", author2, "=", format((total_unused_words1/total_words1) * 100, "0.10f"))

	print()
	print(author2, "used", len(unused_words2), "that", author1, "did not use.")
	print("Relative frequency of words used by", author2, "not in common with", author1, "=", format((total_unused_words2/total_words2) * 100, "0.10f"))


def main():
  # Create word dictionary from comprehensive word list
  
  create_word_dict()

  #Enter names of the two books in electronic form
  book1 = input ("Enter name of first book: ")
  book2 = input ("Enter name of second book: ")
  print()

  # Enter names of the two authors
  author1 = input ("Enter last name of first author: ")
  author2 = input ("Enter last name of second author: ")
  print() 
  
  # Get the frequency of words used by the two authors
  wordFreq1 = getWordFreq (book1)
  wordFreq2 = getWordFreq (book2)

  # Compare the relative frequency of uncommon words used
  # by the two authors
  wordComparison (author1, wordFreq1, author2, wordFreq2)
main()