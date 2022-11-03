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

a,b,c=print_max_min_sum_for_row_wise(num_list)
print(a)
print(b)
print(c)


'''
input:

3 3
1 2 3
10 20 30
5 10 15

output:

[3, 30, 15]
[1, 10, 5]
[6, 60, 30]

'''









