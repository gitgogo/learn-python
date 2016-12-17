while True:
	s=raw_input('input a number between 1 and 100: ')
	if s in [str(s) for s in xrange(1,101)]:
		s=int(s)
		if s<=100 and s>=1:
			print 'you just input %d' %s #why always output 100
			break
	else:
		print 'invalid try again: '