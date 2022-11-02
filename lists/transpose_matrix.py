def get_transpose_of_matrix(matrix, m, n):
    tr_m=[]
    for i in range(n):
        r_mat=[]
        for j in range(m):
           mat =matrix[j][i]
           r_mat.append(mat)
        tr_m.append(r_mat)
    return tr_m

    # Complete this function

def convert_string_to_int(list_a):
    new_list = []
    for item in list_a:
        num = int(item)
        new_list.append(num)
    return new_list


m, n = input().split()
m, n = int(m), int(n)
num_list = []

for i in range(m):
    list_a = input().split()
    list_a = convert_string_to_int(list_a)
    num_list.append(list_a)


# Call the get_transpose_of_matrix function
tr_mat=get_transpose_of_matrix(num_list, m,n )
for i in tr_mat:
    print(i)


'''
input:    
-----------------
3 3
1 2 3
10 20 30
5 10 15

output:
------------------

[1, 10, 5]
[2, 20, 10]
[3, 30, 15]

'''

