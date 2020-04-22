def make_move(sticks):
    a=sticks %4
    return a if a!=0 else 1
print(make_move(20))
