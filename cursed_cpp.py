import sys



def tab_cnt(txt: str) -> int:
	"""Count the number of prefix tabs"""
	
	count = 0

	for i in txt:
		if i == '\t':
			count += 1
		else:
			break

	return count



def is_empty(txt: str) -> bool:
	"""Check whether a string consists of whitespaces and tabs only"""

	return (txt.replace('\t', '') + ' ').isspace()



def format_closing_braces(tab: int, n = 1) -> str:
	"""Format descending '}' characters starting from 'tab'"""

	_str = ''

	for i in range(n):
		_str += (tab - i)*'\t' + '}\n'

	return _str



def format_opening_braces(tab: int, n = 1) -> str:
	"""Format ascending '{' characters starting from 'tab'"""

	_str = ''

	for i in range(n):
		_str += (tab + i)*'\t' + '{\n'

	return _str



def uncurse(txt: str) -> str:
	"""Convert a pythonic CPP source into a regular CPP source"""


	lines = txt.splitlines()
	lines = [line for line in lines if (not is_empty(line)) and (not line.replace('\t', '').startswith('#'))]
	lines.append('')


	tab_cnts = [tab_cnt(line) for line in lines]


	final = ''


	for i, line in enumerate(lines):

		if i == len(lines)-1:
			break



		for keywrd in ['for', 'if', 'while', 'elif']:
			if keywrd in line:
				line = line.replace(keywrd, '').replace('\t', '').strip()

				if not line.startswith('('):
					line = '(' + line

				if not line.endswith(')'):
					line += ')'

				line = tab_cnts[i]*'\t' + keywrd + ' ' + line

				break



		diff = tab_cnts[i+1] - tab_cnts[i]

		if diff > 0:
			final += line + '\n'
			final += format_opening_braces(tab_cnts[i], diff)
		elif diff < 0:
			final += line + ';\n'
			final += format_closing_braces(tab_cnts[i]-1, -diff)
		else:
			final += line + ';\n'


	return final



if __name__ == '__main__':
	if len(sys.argv) == 1:
		import clipboard
		clipboard.copy(uncurse(clipboard.paste()))

	elif len(sys.argv) == 2:
		with open(sys.argv[1], 'r') as f:
			with open('uncursed_' + sys.argv[1], 'w') as f2:
				f2.write(uncurse(f.read()))

	elif len(sys.argv) == 3:
		with open(sys.argv[1], 'r') as f:
			with open(sys.argv[2], 'w') as f2:
				f2.write(uncurse(f.read()))

	else:
		print('[!] Too many arguments [!]')
# The last line number is the square of a repunit ;) ... HOLD UP