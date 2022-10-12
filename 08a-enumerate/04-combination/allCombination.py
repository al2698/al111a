<<<<<<< HEAD
def combination(A, k):
	chooses = []
	c(A, len(A), k, chooses, k)

def c(A, n, k, chooses, kc):
	# print('chooses=', chooses, 'k=', k)
	if len(chooses)==kc:
		print(chooses)
		return
	if n <= 0: return
	c(A,n-1,k,chooses,kc) # C(n-1,k)

	chooses.append(A[n-1])
	c(A,n-1,k-1,chooses,kc) # C(n-1,k-1)
=======
def combination(A, m): # 從 A 陣列中取出 m 個的所有可能性
	chooses = []
	c(A, len(A), m, chooses, m)

def c(A, n, k, chooses, m): # 從 A[0..n] 中選取 k 個補進 chooses，如果滿 m 個就印出
	if len(chooses)==m:
		print(chooses)
		return
	if n <= 0: return
	c(A,n-1,k,chooses,m) # C(n-1,k)

	chooses.append(A[n-1])
	c(A,n-1,k-1,chooses,m) # C(n-1,k-1)
>>>>>>> c84f3b508c09d28b56ecd8cab3509e77b10099c4
	del chooses[-1]

combination([1,2,3,4,5], 3)
