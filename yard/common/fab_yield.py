#READ - http://www.liaoxuefeng.com/article/001373892916170b88313a39f294309970ad53fc6851243000

def fab1(max):
    n, a, b = 0, 0, 1
    while n < max:
        print b
        a, b = b, a + b
        n = n + 1

def fab2(max):
    n, a, b = 0, 0, 1
    print "call b -",str(b)
    while n < max:
        print "before yield b:",str(b)
        yield b
        print "after yield b:",str(b)
        a, b = b, a + b
        print "after process b:",str(b)
        n += 1
        print "after process n:", str(n)
        print "*"*30

if __name__ == "__main__":
    # print "fab1"
    # fab1(4)
    print "fab2" 
    print "#"*30
    for x in fab2(4):
        print 'get yield value x:', x

    print "#"*30
