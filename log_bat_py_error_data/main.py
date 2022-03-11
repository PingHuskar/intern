import os
import sys
from glob import glob
import re
print(os.getcwd())
# print(glob(f"{os.getcwd()}/*/"))
def to_csv(folder_name):
	if os.path.exists(f"{folder_name}\\log.txt"):
		os.remove(f"{folder_name}\\log.txt")
	if os.path.exists(f"{folder_name}\\log.csv"):
		os.remove(f"{folder_name}\\log.csv")
	log_files_in_folder = glob(f"{os.getcwd()}\\{folder_name}/*.log")
	print(f"found {len(log_files_in_folder)} log file(s)")
	# print(log_files_in_folder)
	
	with open(f"{folder_name}\\log.txt",'w+') as f:
		f.writelines(f'file, rows_copied, total, error,,\n')
		for file in log_files_in_folder:
			print(f"file : {file}")
			with open(file,'r') as r:
				read_log = r.readlines()
				# print(read_log)
				for line in read_log[-6:]:
					line = line.replace("\n","")
					try:
						rows_copied = re.search(r"^(\d+) rows copied\.",line).group(1)
						# print(rows_copied)
					except Exception as e:
						pass
					try:
						total = re.search(r"Clock.*?[tT]otal.*?(\d+)",line).group(1)
						# print(total)
					except Exception as e:
						pass
					try:
						error_msg = re.search(r"^Server Message: (.+):",line).group(1)
						error_msg = f'"{error_msg}",,'
						print(error_msg)
					except Exception as e:
						pass
				r.close()
			file_name = re.search(r'[^\\]+\.log',file).group(0)
			try:
				f.writelines(f"{file_name},{rows_copied},{total},{error_msg}\n")
			except Exception:
				f.writelines(f"{file_name},{rows_copied},{total},\"\",\n")
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
	main()
	# input()