import argparse

def clean_urls_in(read_file, write_file ):
	with open(read_file, 'r') as f:
		with open(write_file, 'w+') as F: 
			for line in f:
				if 'https' in line:
					F.write(line[:line.find('http')-1]+'\n')
				else:
					F.write(line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("read_file", help = 'localisation of file to change')
    parser.add_argument("write_file", help = 'where to safe new file')
    args = parser.parse_args()
    
    clean_urls_in(args.read_file, args.write_file)

    