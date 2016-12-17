import sys

def readfile(filename):
	f=file(filename)
	while True:
		line=f.readline()
		if len(line)==0:
			break
		print line,
	f.close()

if len(sys.argv)<2:
	print "NO action specified"
	sys.exit()

if sys.argv[1].startswith("--"):
	option=sys.argv[1][2:]
	if option=="Version":
		print "Version1.2"
	elif option=="help":
		print "oh you need help, ok??"
	else:
		print 'Unknown option'
		sys.exit()
else:
	for filename in sys.argv[1:]:
		readfile(filename)