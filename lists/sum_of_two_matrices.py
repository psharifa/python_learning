def add_two_matrices(first_matrix, second_matrix, m, n):
    res=[]
    for i in range(m):
        row=[]
        for j in range(n):
            mat=first_matrix[i][j]+second_matrix[i][j]
            row.append(mat)
        res.append(row)
    return res
    # Complete this function

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


def read_matrix_inputs(m):
    num_list = []
    for i in range(m):
        list_a = input().split()
        list_a = convert_string_to_int(list_a)
        num_list.append(list_a)
    return num_list


m, n = input().split()
m, n = int(m), int(n)

first_matrix = read_matrix_inputs(m)
second_matrix = read_matrix_inputs(m)

# call the add_two_matrices matrices
res=add_two_matrices(first_matrix, second_matrix, m, n)
for i in res:
    print(i)
    
    
    
'''
input:

3 3

1 2 3           (matrix-1)
10 20 30
5 10 15

2 4 6
11 22 33        (matrix-2)
7 14 21

output:

[3, 6, 9]
[21, 42, 63]   (sum of each element with respective element in other matrix)
[12, 24, 36]

'''





