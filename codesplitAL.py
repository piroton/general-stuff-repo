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
	print("File", fname, "written.")
	return

def main():
	fname = input("Enter Table Name:")
	text = read_file(fname)
	septext = []
	codetext = []
	for line in text:
		splitted = line.split(maxsplit=1)
		print(splitted)
		septext.append(splitted[0]+"\n")
		codetext.append(splitted[1])
	fout = "splitout.txt"
	wtext = septext+codetext
	write_file(fout,wtext)
	input("Press Enter to Exit.")
	return
	
main()