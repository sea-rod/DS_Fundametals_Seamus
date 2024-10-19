from read_file import csv_to_matrix,write_file
from mutiplication import mutiplication

if __name__ == "__main__":
    mat1 = csv_to_matrix("mat1.csv")
    mat2 = csv_to_matrix("mat2.csv")
    res  = mutiplication(mat1,mat2)
    write_file(res,"res.csv")