#define function_name 
def minSwap(s):
	strng = list(s)
	unmp = {}
	for i in strng:
		unmp[i] = unmp.get(i,0)+1
	odd = 0
	result = 0
	left = 0
	right = len(strng)-1

    #applying for loop
	for i in unmp:
		if unmp[i]%2 != 0:
			odd += 1
	# If we found more then one odd number
	if odd > 1:
		return -1
	while left < right:
		l = left
		r = right
		while strng[l] != strng[r]:
			r -= 1
		if l == r:
			# When we found odd element move towards middle
			strng[r],strng[r+1] = strng[r+1],strng[r]
			result += 1
			continue
		else:
			# Normal element move towards right of string
			while r < right:
				strng[r],strng[r+1] = strng[r+1],strng[r]
				r += 1
				result += 1
		left += 1
		right -= 1
	return result
s="aabcc"
print(minSwap(s))


