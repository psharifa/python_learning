def convert_str_int(a):
    s = []
    for i in a:
        s.append(int(i))
    return s

def nested_list(n):
    result = []
    for i in range(n):
        a=input().split(" ")
        result.append(convert_str_int(a))
    return result

if __name__ == '__main__':
    n=int(input())                           
    result = nested_list(n
    print(result)
                         
                         
'''
input:  3
        1 2 3 4
        10 20 30
        5 10 15 20
        
output:  [[1, 2, 3, 4], [10, 20, 30], [5, 10, 15, 20]]
'''
                     
