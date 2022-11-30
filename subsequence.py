fs=input()
sub=input()
subind=0
sublen=len(sub)
for char in fs:
    if char==sub[subind]:
        subind += 1
        if subind==sublen:
            break
if subind==sublen:
    print("Yes")
else:
    print("No")
    
    
    
    
'''
input:abcde
      ace
output: yes
'''
