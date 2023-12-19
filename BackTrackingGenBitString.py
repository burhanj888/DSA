
def AppendInFront(x, L):
    return [x + element for element in L]

def bitStrings(n):
    if n == 0: return []
    if n == 1: return ["0", "1"]
    else:
        return (AppendInFront("0", bitStrings(n-1)) + AppendInFront("1", bitStrings(n-1)))

print(bitStrings(4))