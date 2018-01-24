import os

def glossary_dict(fname):
	with open(fname, mode='r', encoding='utf8') as document:
		table = document.readlines()
		#initialise key table and value table
		k = []
		v = []
		#read lines and sort into key-value pairs
		for n in range(len(table)):
			#strip newline character from line
			tab = table[n].rstrip("\n")
			splitted = tab.split("**")
			'''print(splitted)'''
			print(n)
			#text is formatted into key-value pairs in format k=v
			k.append(splitted[0])
			v.append(splitted[1])
		#creates dict based on zip iterable
		match = dict(zip(k,v))
	print("Dictionary Loaded.")
	#returns both list of keys and dictionary
	return match, k

def read_file(fname):
	text = []
	with open(fname, mode='r', encoding='utf8') as document:
		text = document.readlines()
	print("File",fname, "Read.")
	return text
	
def write_file(fname, text):
	with open(fname, mode='w', encoding='utf8') as document:
		for line in text:
			document.write(line)
	print("File written.")
	return
	
def main():
	#read files, get dictionary
	glossary = input("Enter Glossary file name: ")
	match, keys = glossary_dict(glossary)
	filename = input("Enter File Name to be replaced:")
	text = read_file(filename)
	
	#sort keys by length for efficiency purposes: longer words get priority. Initialise new text list
	new_text = []
	keys = sorted(keys, key=len, reverse=True)
	
	#replaces lines by longest key first
	for line in text:
		for key in keys:
			line = line.replace(key, match[key])
		new_text.append(line)
		
	#write to file
	write_file(filename, new_text)
	print("Complete.")
	return
	

main()
