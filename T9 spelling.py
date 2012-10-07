import string
if __name__ == "__main__":
	n = int(raw_input("Enter number of cases: "))
	t_dict = {"abc":"2", "def":"3", "ghi":"4", "jkl":"5", "mno":"6", "pqrs":"7", "tuv":"8", "wxyz":"9", " ":"0"}
	for case_count in range(0, n):
		while True:			
			sentence = raw_input("Enter the desired sentence : ")		
			get_out = False	
			for letter in range(0, len(sentence)):
				if sentence[letter] in string.ascii_letters or sentence[letter] == " ":
					get_out = True
				else:
					get_out = False
					break
			if get_out :
				sentence = sentence.lower()
				break
								
		result = ""
		for i in range(0, len(sentence)):				
			for ind, val in t_dict.iteritems():
				if sentence[i] in ind:
					rep = ind.index(sentence[i]) +1 
					result += val * rep
				if not (i == len(sentence) - 1):
					if sentence[i] in ind and sentence[i+1] in ind:
						result += " "
		print "Case #%d: %s" % (case_count+1, result)
