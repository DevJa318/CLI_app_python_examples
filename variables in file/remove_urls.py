def clean_urls_in(read_file, write_file ):
	with open(read_file, 'r') as f:
		with open(write_file, 'w+') as F: 
			for line in f:
				if 'https' in line:
					F.write(line[:line.find('http')-1]+'\n')
				else:
					F.write(line)

if __name__ == '__main__':
	
	file = "/run/media/devja318/My Passport/Systemy/Manjaro 10.2022/devja318/Dokumenty/PIERWSZA_BD/Notatki Stałe - Sprecyzowane/Notatki z Literatury/Książki/Alkabary, 2020 (1. kopia).md"
	file2 = "nowy_plik.md"
	
	clean_urls_in(file, file2)
