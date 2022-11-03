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


def print_max_min_sum_for_row_wise(num_list):
    max_list=[]
    min_list=[]
    sum_list=[]
    for i in num_list:
        mx=max(i)
        max_list.append(mx)
        mn=min(i)
        min_list.append(mn)
        sm=sum(i)
        sum_list.append(sm)
    return max_list,min_list,sum_list
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


# Write your code here
# Call the get_transpose_of_matrix function
tr  =  get_transpose_of_matrix(num_list, m, n)
# Call the print_max_min_sum_for_row_wise function
ma,mn,sm = print_max_min_sum_for_row_wise(tr)
print(ma)
print(mn)
print(sm)


'''
input:

3 3
1 2 3
10 20 30
5 10 15

output:

[10, 20, 30]  (max of each col)
[1, 2, 3]     (min of each col)
[16, 32, 48]  (sum of each col)

'''
