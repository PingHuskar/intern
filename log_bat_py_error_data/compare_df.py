import os
import re
from time import time, sleep
import pandas as pd

def dataframe(folder_name):
	df1 = pd.read_csv(f"{folder_name}_import.csv",sep=",")
	df2 = pd.read_csv(f"{folder_name}_export.csv",sep=",")
	result = pd.concat([df1, df2.reindex(df1.index)], axis=1)
	print(folder_name)
	print(result)
	print(result.columns)

def main():
	folder_list = []
	for it in os.scandir():
		if it.is_dir():
			folder_list.append(re.sub('_(im|ex)port','',it.path[2:]))
	folder_list = list(set(folder_list))
	# print(folder_list)
	for each in folder_list:
		dataframe(each)
		sleep(1)

if __name__ == '__main__':
	print(f'Start compare_df.py')
	t = time()
	main()
	print(f'Stop compare_df.py')
	print("Runtime :",round(time()-t,2),"second(s)")