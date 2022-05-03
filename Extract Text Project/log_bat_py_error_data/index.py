import sys
import os
def main(arg1):
    with open(f"{arg1}/log.txt","r+") as f:
        a = f.readlines()
        try:
            while True:
                a.remove("\n")
        except ValueError:
            pass
        this_file = "anystring"
        pending = ["","","","",]
        new_log = """"""
        for line in a:
            line = line.replace("\n","")
            if line[0] == "-":
                if (pending[-1] != "") or (pending[1] != "" and pending[2] != ""):
                    new_log += f"""{",".join(pending)}\n""" 
                    pending = ["","","","",]
                    continue
                if line.split(" ")[1] != this_file:
                    pending[0] = line.split(" ")[1]
                this_file = line.split(" ")[1]
            elif line[0] in "0123456789":
                pending[1] = line.split(" ")[0]
            elif line[0] == "C":
                pending[2] = line.split(" ")[5]
            elif line[0] == "S":
                pending[3] = f'"{line[17:-1]}",,' #"BUAMS01 - Msg 2403, Level 10, State 0",,
        f.close()
    with open(f"{arg1}/log.txt","w+") as f:
        f.writelines(f'file, rows_copied, total, error,,\n')
        f.writelines(new_log.strip().replace(", \n, , , ",""))
        f.close()

if __name__ == '__main__':
    main(f'C:\\Users\\SF114-32\\Downloads\\AMS_UAT_LOG\\{sys.argv[1]}')