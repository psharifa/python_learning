def replace_old_value_with_new_value(matrix, old_value, new_value):
    up_mat=[]
    for row in matrix:
        up_row=row 
        for i in range(len(row)):
            if row[i]==old_value:
                up_row[i]=new_value
        up_mat.append(up_row)
    return up_mat
    
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

values = input().split()
old_value, new_value = convert_string_to_int(values)

# Call the replace_old_value_with_new_value function
# Write your code here

res=replace_old_value_with_new_value(num_list, old_value, new_value)
for i in res:
    print(i)
    
 '''
 input:
 
 3 3
1 2 3
10 20 30
5 10 15
10 8      (old value and new value which is to be replaced)

output:

[1, 2, 3]
[8, 20, 30]
[5, 8, 15]


 '''
    
    
    
    
    
    
    
    
    
