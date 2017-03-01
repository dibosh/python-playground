import string
import sys
import math
from itertools import permutations

alphabets = list(string.ascii_lowercase)
alphabet_freq_map = dict((el,0) for el in alphabets)
white_spaces = [' ', '\t', '\n', '\r\n']

# checks if a string is palindrome or not
def is_palindrome(str):
	str = str.replace(" ", "").lower()
	rev_str = str[::-1]
	return str == rev_str

# v1
# prints how many changes needed to turn a string to palindrome
# a change is like 'b->a or c->b' the letters can change from 
# higher order letter to lower but not vice versa(i.g. d->c is only valid)
# and can change upto character 'a' (i.e. d->c->b->a->stop.)
# pr: https://www.hackerrank.com/challenges/the-love-letter-mystery
def turn_palindrome():
	str = sys.stdin.readline()
	str = str.strip().replace(" ", "").lower()
	rev_str = str[::-1]
	no_of_changes = 0
	for i in range(0, len(str)):
		# print "diff: %d, str[i]: %d, rev_str[i]: %d" % (abs(ord(str[i])-ord(rev_str[i])), ord(str[i]), ord(rev_str[i]))
		no_of_changes += abs(ord(str[i])-ord(rev_str[i]))
	# as the string is reversed one change is always counted twice during the loop
	print no_of_changes/2

# v2
# remarks : much efficient
# prints how many changes needed to turn a string to palindrome
# a change is like 'b->a or c->b' the letters can change from 
# higher order letter to lower but not vice versa(i.g. d->c is only valid)
# and can change upto character 'a' (i.e. d->c->b->a->stop.)
# pr: https://www.hackerrank.com/challenges/the-love-letter-mystery
def turn_palindrome2():
	str = sys.stdin.readline()
	str = str.strip().replace(" ", "").lower()
	length = len(str)
	mid_point = int(math.floor(length/2))
	no_of_changes = 0
	for i in range(0, mid_point):
		j = length - i - 1
		no_of_changes += abs(ord(str[i])-ord(str[j]))
	print no_of_changes


def find_palindromes(seq,y):
  return [(seq.index(seq[x:x+y]),y) for x in range(len(seq)-y) if seq[x:x+y] == seq[x:x+y][::-1]]

# checks all the permutations of a given string for if there is any palindrome or not
# pr: https://www.hackerrank.com/challenges/game-of-thrones
def is_palindrome_possible():
	str = sys.stdin.readline()
	str = str.strip().replace(" ", "").lower()
	letters = []

	for c in str:
		letters.append(c)
			
	letter_freq_map = dict((el,0) for el in letters)
	print_palindrome = True

	for c in str:
		letter_freq_map[c] += 1

	odd_frequency = 0

	for key in letter_freq_map.keys():
		frequency = letter_freq_map[key]
		if frequency % 2 == 1:
			odd_frequency += 1

	if odd_frequency <= 1:
		print "YES"
	else:
		print "NO"


# count number of necessary deletions to turn a string consisting of
# consecutive alternating characters. e.g. ABAB, A, B, BABA are valid, AAA not valid.
# pr: https://www.hackerrank.com/challenges/alternating-characters
def alternating_chars():
	line = sys.stdin.readline()
	line = line.strip().lower()
	list=[]
	#init
	list.append(line[0])

	for i in range(0, len(line)):
		if line[i] in white_spaces:
			continue
		if list[-1] != line[i]:
			list.append(line[i])
	print (len(line) - len(list))
		
# given a sentence detect if it's pangram or not
# a pangram will contain all the letters from alphabet
# e.g. The quick brown fox jumps over the lazy dog
# pr: https://www.hackerrank.com/challenges/pangrams
def pangram():
	isPangram = True
	line = sys.stdin.readline()
	line = line.lower()

	for c in line:
		if c in white_spaces:
			continue
		alphabet_freq_map[c] += 1
	for key in alphabet_freq_map.keys():
		if alphabet_freq_map[key] == 0:
			isPangram = False
			break

	if isPangram:
		print 'pangram'
	else:
		print 'not pangram'

# used when multiple test cases are given
def iterable_input_solution():
	T = int(sys.stdin.readline())
	while (T>0):
		# alternating_chars()
		# pangram()
		turn_palindrome2()
		T -= 1

def run():
	# iterable_input_solution()
	is_palindrome_possible()

if __name__ == '__main__':
	run()
