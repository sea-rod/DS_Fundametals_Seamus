def csv_to_matrix(path):
    mat = []
    with open(path) as file:
        for line in file.readlines():
            mat.append([int(i) for i in line.strip('\n').split(",")])
    return mat

def write_file(mat,path):
    with open(path,"wt") as file:
        for i in mat:
            file.write(",".join([str(j) for j in i])+"\n")
    print("file written")