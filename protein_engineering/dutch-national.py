arr= [2, 3, 2, 3, 5]
freq={}
for i in range(len(arr)):
    if arr[i] in freq:
        freq[arr[i]]+=1
    else:
        freq[arr[i]]=1
result=[0]*max(arr)
for k in freq:
    if k in freq:
        result[k-1]=freq[k]
print(result)

    

