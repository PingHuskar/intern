import os
import re
from time import time, sleep
import pandas as pd
import numpy as np

def dataframe(folder_name):
	df1 = pd.read_csv(f"{folder_name}_import.csv",sep=",")
	df2 = pd.read_csv(f"{folder_name}_export.csv",sep=",")
	result = pd.concat([df1, df2.reindex(df1.index)], axis=1)
	print(folder_name)
	if (result.iloc[:, 0].equals(result.iloc[:, 4])):
		result['compare_rowscopied'] = np.where(result.iloc[:, 1]==result.iloc[:, 5],"Eq","No")
		result['compare_total'] = np.where(result.iloc[:, 2]==result.iloc[:, 6],"Eq","No")
		result.pop('file')
		result.insert(0, "Filename", df1.iloc[:, 0])
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
			folder_list.append(re.sub('_(im|ex)port','',it.path[2:]))
	folder_list = list(set(folder_list))
	for each in folder_list:
		dataframe(each)
		# sleep(1)

if __name__ == '__main__':
	print(f'Start compare_df.py')
	t = time()
	main()
	print(f'Stop compare_df.py')
	print("Runtime :",round(time()-t,2),"second(s)")
