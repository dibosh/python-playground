import sys
def canWin(n):
	if n%4 == 0:
		return False
	else:
		return True

if __name__ == '__main__':
	print canWin(int(sys.argv[1]))