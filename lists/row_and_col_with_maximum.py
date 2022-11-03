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
for i in num_list:
    mx=max(i)
    max_list.append(mx)

maxi=max(max_list)
ind=max_list.index(maxi)
last_max=num_list[ind]
print(last_max)
    
    
col=last_max.index(maxi)
m_col=[]
for i in num_list:
    m_col.append(i[col])
print(m_col)
    
    
'''
input:

3 3
1 2 3
10 20 30
5 10 15

output:

[10, 20, 30]
[3, 30, 15]

'''










