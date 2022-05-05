def digital_division(n):
	if len(str(n)) == 1:
		return "Perfect"
	condition_1 = all(not n % int(i) for i in str(n).replace("0",""))
	condition_2 = not ( n % sum(int(i) for i in str(n)) )
	res = [int(str(n)[0])]
	res = [res[-1] * int(i) for i in str(n)[1:]][0]
	if res:
		condition_3 = not n % res
	else:
		condition_3 = False
	lst = [condition_1,condition_2,condition_3]
	if sum(lst) == 1:
		return 1
	if sum(lst) == 2:
		return 2
	if sum(lst) == 3:
		return "Perfect"
	if not sum(lst):
		return "Indivisible"
		
	