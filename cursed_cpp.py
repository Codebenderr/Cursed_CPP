import sys



def tab_cnt(txt: str) -> int:
	"""Count the number of prefix tabs"""
	
	if len(txt) == 0:
		return 0
	elif txt[0] == '\t':
		return len(txt) - len(txt.lstrip())
	else:
		return (len(txt) - len(txt.lstrip()))//4



def is_empty(txt: str) -> bool:
	"""Check whether a string consists of whitespaces and tabs only"""

	return len(txt) == 0 or txt.isspace()



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



def _enumerate(seq):
	"""The same as the enumerate() function but the last element is not included"""

	for i, v in enumerate(seq):

		if i != len(seq)-1:
			yield i, v



def uncurse(txt: str) -> str:
	"""Convert a cursed CPP source into an uncursed CPP source"""


	lines = txt.splitlines()
	lines = [line for line in lines if not is_empty(line)]
	lines.append('')


	final = ''


	for i, line in _enumerate(lines):


		if line.lstrip().startswith('#'):
			final += line + '\n'
			continue



		if '//' in line:
			line = line.split('//')[0].rstrip()

			if is_empty(line):
				continue



		line_tab_cnt = tab_cnt(line)



		for keywrd in ['for', 'else if', 'if', 'while', 'switch']:
			if keywrd in line:
				line = line.replace(keywrd, '').strip()

				if not line.startswith('('):
					line = '(' + line

				if not line.endswith(')'):
					line += ')'

				line = line_tab_cnt*'\t' + keywrd + ' ' + line

				break



		diff = tab_cnt(lines[i+1]) - line_tab_cnt

		if diff > 0:
			final += line + '\n'
			final += format_opening_braces(line_tab_cnt, diff)
		elif diff < 0:
			final += line + ';\n'
			final += format_closing_braces(line_tab_cnt-1, -diff)
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