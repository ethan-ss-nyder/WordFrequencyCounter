# This script was made to expedite the process of cluster criticism for ENGL3060.
# Whatever the artifact of choice is, paste the raw text into a text file in the same folder or directory as this
 # script. If there are many artifacts, paste all contents into the same text file. Whitespace does not matter.
# Ethan Snyder, 2024

import re
from collections import defaultdict
import csv

# Editable variables
filename = 'Words.txt' # Make this match the input text file name!
exclude_words = ['a', 'the', 'of', 'to', 'be', 'in', 'am'] # Add words you'd like to exclude from being counted.

def file_to_string():
	with open(filename, 'r') as file:
		return re.findall(r"\b\w+(?:'\w+)?\b", file.read().lower()) # String parsing magic
		
def make_dictionary(word_list):
	word_counts = defaultdict(int)
	for word in word_list:
		if word not in exclude_words:
			word_counts[word] += 1
	return sorted(word_counts.items(), key=lambda item: item[1], reverse=True)

def print_to_CSV(printable):
	with open('WordFrequencyCount.csv', 'w', newline='') as csvfile:
		writer = csv.writer(csvfile)
		writer.writerow(['Word', 'Count'])
		for word, count in printable:
			writer.writerow([word, count])

def main():
	print_to_CSV(make_dictionary(file_to_string()))
	
main()
