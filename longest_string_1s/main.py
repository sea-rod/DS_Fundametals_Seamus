mat = [[[0 for _ in range(3)] for _ in range(5)] for _ in range(7)]

def create_mat(mat):
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(len(mat[0][0])):
                if not ((i + j + k) % 10 == 2 or (i + j + k) % 10 == 4):
                    mat[i][j][k] = 1
    return mat


def count_1s(mat):
    count = max_count = 0
    pos = []
    max_pos = []
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            for k in range(len(mat[0][0])):
                if mat[i][j][k]==1:
                    count += 1
                    pos.append((i,j,k))
                else:
                    count = 0
                    pos = []
                max_count = max(max_count,count)
                max_pos = max(max_pos,pos,key=lambda arr:len(arr))
            count = 0
            pos = []

    count = 0
    pos = []

    for i in range(len(mat)):
        for k in range(len(mat[0][0])):
            for j in range(len(mat[0])):
                if mat[i][j][k]==1:
                    count += 1
                    pos.append((i,j,k))
                else:
                    count = 0
                    pos = []
                max_count = max(max_count,count)
                max_pos = max(max_pos,pos,key=lambda arr:len(arr))
            count = 0
            pos = []
    count = 0
    pos = []

    for k in range(len(mat[0][0])):
        for j in range(len(mat[0])):
            for i in range(len(mat)):
                if mat[i][j][k] == 1:
                    count += 1
                    pos.append((i, j, k))
                else:
                    count = 0
                    pos = []
                max_count = max(max_count, count)
                max_pos = max(max_pos, pos, key=lambda arr: len(arr))
            count = 0
            pos = []

    return max_count,max_pos

mat = create_mat(mat)
print(count_1s(mat))
