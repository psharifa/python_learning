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
print(max(max_list))
print(min(min_list))
print(sum(sum_list))

'''
input:
---------------
3 3
1 2 3
10 20 30
5 10 15


output:
---------------
30   (max)
1    (min)
96   (sum)
'''







