a,b=input().split()
a,b=int(a),int(b)
s=[]
for i in range(a):
    n=input().split()
    c=[]
    for j in n:
        c.append(int(j))
    s.append(c)
max_sum = a + b - 2
for sum in range(max_sum+1):
    for i in range(sum+1):
        if i < a and sum - i < b:
            print(s[i][sum - i], end=" ")
    print()
    
    
 '''
 input:
 
 3 4
1 2 3 4
5 6 7 8
9 10 11 12


output:

1 
2 5 
3 6 9 
4 7 10 
8 11 
12 

 '''
