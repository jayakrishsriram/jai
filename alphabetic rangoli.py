def print_rangoli(size):
    Str = 'abcdefghijklmnopqrstuvwxyz'[0:size]
    
    for i in range(size-1, -size, -1):
        x = abs(i)
        line = Str[size:x:-1]+Str[x:size]
        print ("--"*x+ '-'.join(line)+"--"*x)
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
