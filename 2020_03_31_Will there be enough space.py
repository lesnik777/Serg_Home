def enough(cap, on, wait):
    f= cap - on
    if f >= wait:
        return 0
    else: 
        c=wait-f
        return c
print(enough(10,5,20))
########################################################        
#     return 0 if cap - on >=wait else wait - (cap-on)
# print(enough(10,5,5))