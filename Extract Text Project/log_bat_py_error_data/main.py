import os
import sys
from glob import glob
import re
from time import time, sleep
import numpy as np
import pandas as pd

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
	if os.path.exists(f"{folder_name}.csv"):
		os.remove(f"{folder_name}.csv")
		print(f'{folder_name}.csv removed')
		sleep(1)
	log_files_in_folder = glob(f"{os.getcwd()}\\{folder_name}/*.log")
	print(f"found {len(log_files_in_folder)} log file(s)")
	
	with open(f"{folder_name}.txt",'w+') as f:
		f.writelines(f'file{folder_name[-7:]},rows_copied{folder_name[-7:]},total{folder_name[-7:]},error{folder_name[-7:]}\n')
		for file in log_files_in_folder:
			# print(f"file : {file}")
			with open(file,'r') as r:
				rows_copied = total = error_msg = ""
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
						# print(total)
						continue
					except Exception as e:
						pass
				try: #Server Message
					error_msg += re.search(r"Server Message: (.+\n)+","".join(read_log),re.I).group(0)
				except Exception:
					pass

				try: #CTLIB Message
					error_msg += re.search(r"CTLIB Message: (.+\n)+","".join(read_log),re.I).group(0)
				except Exception:
					pass

				try: #SQLState NativeError Microsoft Something
					unique_SQLState = set(re.findall(r"(SQLState (?:.+\n.+))","".join(read_log),re.I))
					for each_SQLState in unique_SQLState:
						error_msg += f"{each_SQLState}\n"
				except Exception:
					pass

				r.close()
			file_name = re.search(r'[^\\]+\.log',file).group(0)
			if error_msg != "":
				f.writelines(f'{file_name},{rows_copied},{total},"{error_msg[:-1]}"\n')
			else:
				f.writelines(f'{file_name},{rows_copied},{total},\n')
		f.close()
	os.rename(f"{folder_name}.txt", f"{folder_name}.csv")

def dataframe(folder_name):
	df1 = pd.read_csv(f"{folder_name}_import.csv",sep=",")
	df2 = pd.read_csv(f"{folder_name}_export.csv",sep=",")
	result = pd.concat([df1, df2.reindex(df1.index)], axis=1)
	# print(folder_name)
	if (result['file_import'].equals(result['file_export'])):
		result['compare_rowscopied'] = np.where(result['rows_copied_import']==result['rows_copied_export'],"Eq","No")
		result['compare_total'] = np.where(result['total_import']==result['total_export'],"Eq","No")
		result.pop('file_import')
		result.pop('file_export')
		result.insert(0, "file", df1.iloc[:, 0])
		print(result)
		print(result.columns)
		print(result['compare_rowscopied'].value_counts())
		print(result['compare_total'].value_counts())
		result.to_csv(f"{folder_name}.csv", index=False)
	else:
		print(f'Filename in {folder_name}_import & {folder_name}_export  differents!')

def main():
	folder_list = []
	for it in os.scandir():
		if it.is_dir():
			folder_list.append(it.path[2:])

	for each in folder_list:
		to_csv(each)

	print(f'Start Compare File')
	folder_list = []
	for it in os.scandir():
		if it.is_dir():
			folder_list.append(re.sub('_(im|ex)port','',it.path[2:]))
	folder_list = list(set(folder_list))
	for each in folder_list:
		dataframe(each)
	print(f'Stop Compare File')
if __name__ == '__main__':
	print(f'Start main.py')
	t = time()
	main()
	print(f'Stop main.py')
	print(round(time()-t,2),"second(s)")
