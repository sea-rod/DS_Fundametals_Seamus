def open_file(path):
    mat = []
    with open(path) as file:
        col = file.readline().strip("\n").split(",")
        for line in file.readlines():
            mat.append(line.strip("\n").split(","))
    return col, mat

def get_index(col:list,name):
    return col.index(name)
