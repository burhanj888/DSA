
mystring = "reverse"

#using for loop
def loopRev(s):
    revstring = ""
    for char in s:
        revstring = char + revstring
    return revstring

print("Reverse using loop")
print(loopRev(mystring))

#using slicing 

def sliceRev(s):
    return s[::-1]

print("Reverse using Slicing")
print(sliceRev(mystring))

#using reversed()

def revReversed(s):
    return ''.join(reversed(s))

print("Reverse using reversed()")
print(revReversed(mystring))

#using recursion
def revRecursion(s):
    if len(s) == 0:
        return s
    else:
        return revRecursion(s[1:]) + s[0]
    
print("Reverse using recursion")
print(revRecursion(mystring))
    
#using list reverse and join()

def revJoinList(s):
    temp_list = list(s)
    temp_list.reverse()
    return ''.join(temp_list)

print("Reverse using reversed list")
print(revJoinList(mystring))

#using stack list

def revStack(s):
    stack = list()
    reversedString = ''
    while stack:
        reversedString += stack.pop()
    return reversedString 

print("Reverse using stack")
print(revStack(mystring))