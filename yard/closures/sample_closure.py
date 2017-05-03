#Here is a closure in python:
def makeInc(x):
    def inc(y):
     # x is "closed" in the definition of inc
        return y + x
    return inc

inc5 = makeInc(5)
inc10 = makeInc(10)

print inc5(5) # returns 10
print inc10(5) # returns 15



f = lambda x: x + 1 if x < 10 else x - 1

foo = [1, 2, 3, 4, 5, 6]

foo2 = [x if x >3  else None for x in foo]

print(foo2)