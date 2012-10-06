if __name__ == "__main__":
	phrase = ""
	p_list = []
	n = int(raw_input("Enter number of cases : "))
	for i in range(0, n):
		phrase = raw_input("Enter a phrase to reverse: ")
		p_list = phrase.split(" ")
		p_list.reverse()
		print "Case #%d: %s" % (i+1, " ".join(p_list))
