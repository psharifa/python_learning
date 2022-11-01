def line(a):
    a=a.lower()
    b=set(a)
    b.discard(" ")
    b=sorted(b)
    for i in b:
        c=a.count(i)
        msg= "{char}:  {count}"
        print(msg.format(char=i,count=c))
    
    


a=input()      #  input  ::    tic Tac Toe
line(a)        # output  ::    a: 1 , c : 1 , e : 1..........
