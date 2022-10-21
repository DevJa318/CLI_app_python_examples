import sys

def clean_urls_in(read_file, write_file ):
	with open(read_file, 'r') as f:
		with open(write_file, 'w+') as F: 
			for line in f:
				if 'https' in line:
					F.write(line[:line.find('http')-1]+'\n')
				else:
					F.write(line)

if __name__ == '__main__':
	
	if '--help' in sys.argv:
		#sys arg[0] oznacza nazwę pliku
		help_message = f"\tSposób użycia: {sys.argv[0]} --read_file <localisation of file to change> --write_file <localisation of changed file>"
		print(help_message)
		sys.exit()
	
	if '--read_file' in sys.argv:
		file_index = sys.argv.index('--read_file') + 1
	
		if file_index < len(sys.argv):
			file = sys.argv[file_index]
		
		if '--write_file' in sys.argv:
			file2_index = sys.argv.index('--write_file') + 1
	
		if file2_index < len(sys.argv):
			file2 = sys.argv[file2_index]
		

	clean_urls_in(file, file2)
