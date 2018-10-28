import random
import urllib.request
import shutil

PROTEINS_TO_DOWNLOAD = 5
PATH_TO_SAVE = "C:\\Users\\DELL\\Desktop\\pdb\\"
FIRST = "1234567890"
OTHER = "abcdefghijklmnopqrstuvwxyz" + FIRST 


def generate_all_pdb_codes():
	all = []
	for i in range(len(FIRST)):
		for j in range(len(OTHER)):
			for k in range(len(OTHER)):
				for l in range(len(OTHER)):
					all.append(FIRST[i] + OTHER[j] + OTHER[k] + OTHER[l])
	return all

def download_pdbs(pdbs, amount):
	i = 0
	while i < amount:
		num = random.randint(0, len(pdbs))
		url = "https://files.rcsb.org/download/"+str(pdbs[num])+".pdb"
		file_name = url.split('/')[-1]
		try:
			with urllib.request.urlopen(url) as response, open(PATH_TO_SAVE+file_name, 'wb') as out_file:
				data = response.read()
				out_file.write(data)
			i += 1
			print("DONE: ", url)
		except:
			print("FAIL: ", url)

pdbs = generate_all_pdb_codes()
print(len(pdbs))
download_pdbs(pdbs, PROTEINS_TO_DOWNLOAD)
