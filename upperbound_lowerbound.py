def lower_bound(arr,start,end,key):
   
    while(start<=end):
        mid=(start+end)//2
        if arr[mid]<=key and arr[mid+1]>=key:
        	return arr[mid]
        if arr[mid]<key:
            start=mid+1
        else:
            high=mid-1
        
def upper_bound(arr,start,end,key):
	while(start<=end):
		mid=(start+end)//2
		if arr[mid]>=key  and arr[mid-1]<=key:
			return arr[mid]
		if arr[mid]<key:
			start=mid+1
		else:
			end=mid-1
