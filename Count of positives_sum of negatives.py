def count_positives_sum_negatives(arr):
    res1=0
    res2=0
    res=[]
    if len(arr)<=0 : return res
    for i in range(len(arr)):
        if arr[i] < 0:            
            res1+=arr[i]    
        else:
            res2+=1
    res = [res2,res1]
    return res
print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]))
