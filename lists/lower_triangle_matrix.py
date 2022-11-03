def print_lower_triangle(matrix):
    for i in range(len(matrix)):
        row = matrix[i][:i+1]
        print(row)
    
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

# Call the print_lower_triangle function
print_lower_triangle(num_list)



'''

input:  

3 3
1 2 3
10 20 30
5 10 15

output:

[1]             (first element in 1st row)
[10, 20]        (first and second elements in second row)
[5, 10, 15]     (1st,2nd and 3rd elements in 3rd row)


'''




