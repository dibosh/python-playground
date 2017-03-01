import sys
import string

def count_hop(ladder_map, snake_map):
	hop = 0
		start = 1
		while start != 100:
			check = start
			for incr in range(1, 7):
				check += incr
				print 'check %d' % check
				print 'start %d' % start
				if check in ladder_map.keys():
					check = ladder_map[check]
					break
				if check in snake_map.keys():
					continue
			start = check
			hop += 1

				# if start in snake_map.keys():
				# 	continue 
			# hop += 1

		

		print hop

def solve_ladders_and_snakes():
	T = int(sys.stdin.readline())
	while T>0:
		ladder_map = dict()
		snake_map = dict()
		N = int(sys.stdin.readline())
		while N>0:
			line = sys.stdin.readline()
			ladder = line.split()
			ladder_map[int(ladder[0])] = int(ladder[1])
			N -= 1

		M = int(sys.stdin.readline())
		while M>0:
			line = sys.stdin.readline()
			snake = line.split()
			snake_map[int(snake[0])] = int(snake[1])
			M -= 1

		# for x, y in ladder_map.iteritems():
		# 	print x, y
		

		T -= 1


def run():
	solve_ladders_and_snakes()

if __name__ == '__main__':
	run()