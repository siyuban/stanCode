"""
File: boggle.py
Name: 萬思妤
----------------------------------------
TODO:
"""

# This is the file name of the dictionary txt file
# we will be checking if a word exists by searching through it
FILE = 'dictionary.txt'
dictionary = []
count = 0


def main():
	"""""
	TODO:
	"""
	boggle_board = []
	read_dictionary()
	for i in range(4):
		row = input(f'{i+1} row of letters: ')
		row = row.lower()
		if len(row) != 8:
			print('Illegal input')
			break
		row = row.split()
		if len(row) != 4:
			print('Illegal input')
			break
		boggle_board.append(row)
	for r in range(len(boggle_board)):
		for c in range(len(boggle_board[0])):
			start = boggle_board[r][c]
			current_position = (r, c)
			find_word(start, boggle_board, current_position, [current_position], [])
	print('There are', count, 'words in total')


def find_word(current, boggle_board, current_position, visited, ans_list):
	global count
	if not has_prefix(current):
		return
	else:
		for i in range(-1, 2):
			for j in range(-1, 2):
				r_ = current_position[0]+i
				c_ = current_position[1]+j
				if i == 0 and j == 0:
					pass
				else:
					if 0 <= r_ < 4:
						if 0 <= c_ < 4:
							if (r_, c_) not in visited:
								temp_current = current+boggle_board[r_][c_]
								visited.append((r_, c_))
								if len(temp_current) >= 4 and temp_current in dictionary:
									if temp_current not in ans_list:
										ans_list.append(temp_current)
										count += 1
										print('Found: "', temp_current, '"')
										find_word(temp_current, boggle_board, (r_, c_), visited, ans_list)
								else:
									find_word(temp_current, boggle_board, (r_, c_), visited, ans_list)
								visited.pop()


def read_dictionary():
	"""
	This function reads file "dictionary.txt" stored in FILE
	and appends words in each line into a Python list
	"""
	with open(FILE, 'r') as f:
		for line in f:
			word = line.split()
			word = word[0]
			dictionary.append(word)


def has_prefix(sub_s):
	"""
	:param sub_s: (str) A substring that is constructed by neighboring letters on a 4x4 square grid
	:return: (bool) If there is any words with prefix stored in sub_s
	"""
	for word in dictionary:
		if word.startswith(sub_s):
			return True
	return False


if __name__ == '__main__':
	main()
