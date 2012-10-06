def search_items(credit, item_list, current_case):
	global result_list
	found = False
	for j in range(0, len(item_list)):
		for k in range(0, len(item_list)):
			if j != k :
				if item_list[j] + item_list[k] == credit:
					result_list.append("Case #%d: %d %d \n" % (current_case ,j+1  , k+1))
					found = True
					return
	if found == False:
		print "Items not found."
		return
	

def start(test_cases):
	for test_no in range(1,test_cases +1):
		
		while True:
			c = int(raw_input("Enter your credit: "))
			if not 5 <= c <= 1000:
				print "Your credit must be higher than 5 and lower than 1000"
			else:
				break
				
		if test_cases <= 25:
			while True:
				l = int(raw_input("Number of items : "))
				if not 3 <= l <= 100:
					print "Your items number must be higher than 2 and lower than 101"
				else:
					break
		elif test_cases > 25:
			while True:
				l = int(raw_input("Number of items : "))
				if not 3 <= l <= 2000:
					print "Your items number must be higher than 2 and lower than 2001"
				else:
					break
					
		items = raw_input("Enter item prices separated with a space :")
		p = items.split(" ")
		for i in range(0, len(p)):
			p[i] = int(p[i])		
		search_items(c, p, test_no)	

if __name__ == "__main__":
	n = int(raw_input("Enter number of tests: "))
	result_list = []
	start(n)
	f = open("result.txt", "w")
	for i in result_list:
		f.write(i)
	f.close()
