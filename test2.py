def countTrailingZero1(x): 
    count = 0
    while ((x & 1) == 0): 
        x = x >> 1
        count += 1
      
    return count 


from sys import stdin,stdout

def countTrailingZero2(x): 

    lookup = [32, 0, 1, 26, 2, 23, 27, 0, 
            3, 16, 24, 30, 28, 11, 0, 13, 
            4, 7, 17, 0, 25, 22, 31, 15, 
            29, 10, 12, 6, 0, 21, 14, 9, 
            5, 20, 8, 19, 18] 

    return lookup[(-x & x) % 37] 

for _ in range(int(stdin.readline())):
    n=int(stdin.readline())
    if n%2!=0:
        stdout.write(str(n//2)+'\n')

    else:
        count=0
        a=countTrailingZero2(n)
        for i in range(2,n,2):
            b=countTrailingZero2(i)
            if b>a:
                count+=1

        stdout.write(str(count)+'\n')
