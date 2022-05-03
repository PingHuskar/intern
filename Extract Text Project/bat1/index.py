import re
with open("log.txt","r+") as f:
    a = f.readlines()
    try:
        while True:
            a.remove("\n")
    except ValueError:
        pass
    # print(a)
    current_filename = "a b"
    pending = []
    new_log = """"""
    for line in a:
        line = line.replace("\n","")
        if len(pending) == 3:
            # print(", ".join(pending))
            new_log += f"""{", ".join(pending)}\n"""
            pending.clear()
        if line[0] == "-":
            if current_filename != line.split(" ")[1]:
                current_filename = line.split(" ")[1]
                # print(current_filename,end=",")
                pending.append(current_filename)
            else:
                pass
                      
        elif line[0] in "0123456789":
            # print(line.split(" ")[0],end=",")
            pending.append(line.split(" ")[0])
        elif line[0] == "C":
            # print(line.split(" ")[5])
            pending.append(line.split(" ")[5])
    f.close()
with open("log.txt","w+") as f:
    f.writelines(new_log.strip())
    f.close
# input()