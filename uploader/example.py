import re
import string

def handle_uploaded_file(f):
    frequency = {}
	document_text = open('f', 'r')
	text_string = document_text.read().lower()
	match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)
	for word in match_pattern:
    	count = frequency.get(word,0)
    	frequency[word] = count + 1
		frequency_list = frequency.keys()[:5]
	return frequency
			# for words in frequency_list:
   #  			print words, frequency[words]