import os
import sys
from glob import glob
import re
from time import time, sleep
print(os.getcwd())
def to_csv(folder_name):
	if os.path.exists(f"{folder_name}\\log.txt"):
		os.remove(f"{folder_name}\\log.txt")
		print(f'{folder_name}\\log.txt removed')
		sleep(1)
	if os.path.exists(f"{folder_name}\\log.csv"):
		os.remove(f"{folder_name}\\log.csv")
		print(f'{folder_name}\\log.csv removed')
		sleep(1)
	log_files_in_folder = glob(f"{os.getcwd()}\\{folder_name}/*.log")
	print(f"found {len(log_files_in_folder)} log file(s)")
	# print(log_files_in_folder)
	
	with open(f"{folder_name}\\log.txt",'w+') as f:
		f.writelines(f'file,rows_copied,total,error\n')
		for file in log_files_in_folder:
			with open(file,'r') as r:
				error_msg = ""
				read_log = r.readlines()
				for line in read_log[-8:]:
					line = line.replace("\n","")
					try:
						rows_copied = re.search(r"^(\d+) rows copied\.",line).group(1)
						continue
					except Exception as e:
						pass
					try:
						total = re.search(r"Clock.*?[tT]otal.*?(\d+)",line).group(1)
					except Exception as e:
						pass
				# for each error string pattern
				try: #Server Message
					error_msg += re.search(r"Server Message: (.+\n)+","".join(read_log),re.I).group(0)
				except Exception:
					pass

				try: #CTLIB Message
					error_msg += re.search(r"CTLIB Message: (.+\n)+","".join(read_log),re.I).group(0)
				except Exception:
					pass

				try: #SQLState NativeError Microsoft Something
					error_msg += re.search(r"SQLState (.+\n)+","".join(read_log),re.I).group(0)
				except Exception:
					pass
				r.close()
			file_name = re.search(r'[^\\]+\.log',file).group(0)
			if error_msg != "":
				f.writelines(f'{file_name},{rows_copied},{total},"{error_msg[:-1]}"\n')
			else:
				f.writelines(f'{file_name},{rows_copied},{total},\n')
		f.close()
	os.rename(f"{folder_name}\\log.txt", f"{folder_name}\\log.csv")
def main():
	folder_list = []
	for it in os.scandir():
		if it.is_dir():
			folder_list.append(it.path[2:])
	
	# select single folder

	# for i,j in enumerate(folder_list):
	# 	print(f'{str(i+1)} : {j}')
	# select_folder = int(input("Enter A Folder Index : "))
	# selected = folder_list[select_folder-1]
	# print(f'"{selected}" selected')
	# to_csv(selected)

	# run all folder
	for each in folder_list:
		to_csv(each)
if __name__ == '__main__':
	print(f'Start main.py')
	t = time()
	main()
	print(f'Stop main.py')
	print("Runtime :",round(time()-t,2),"second(s)")
	# input()