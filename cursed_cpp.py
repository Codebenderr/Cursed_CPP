
def prefix_tab_cnt(txt):

		if len( txt.strip() ) == 0:
			return 0

		if txt.startswith('\t'):
			return len(txt) - len(txt.lstrip())

		if txt.startswith(' '):
			return (len(txt) - len(txt.lstrip()))//4

		return 0



def uncommentify(txt):
	
	txt = ''.join([part.split('/*')[0] for part in txt.split('*/')])
	
	txt = '\n'.join([line.split('//')[0].rstrip() for line in txt.splitlines()])

	return txt



def semicolonify(txt):

	lines = txt.splitlines()

	final = []

	for i, line in enumerate(lines):

		if line.strip() in ('{', '}'):
			final.append(line)

		elif line.lstrip().startswith('#'):
			final.append(line)

		elif i != len(lines)-1 and lines[i+1].strip() == '{':
			final.append(line)

		elif line.rstrip().endswith(':'):
			final.append(line)

		else:

			if line.rstrip().endswith(';'):
				final.append(line)

			else:
				final.append(line + ';')



	stck = []

	for i, line in enumerate(final):

		if line.lstrip().startswith('struct') or line.lstrip().startswith('class'):
			stck.append( prefix_tab_cnt(line) )

		elif line.strip() == '}':

			if len(stck) > 0 and stck[-1] == prefix_tab_cnt(line):
				stck.pop()
				final[i] = line.rstrip() + ';'




	return '\n'.join(final)



def bracify(txt):

	def format_braces(n1, n2, brace_type):

		final = []

		if n1 < n2:
			for i in range(n1, n2):
				final.append(i*'\t' + brace_type)

		elif n1 > n2:
			for i in range(n1, n2, -1):
				final.append(i*'\t' + brace_type)

		return final


	lines = txt.splitlines()
	lines.append('')

	final = []

	for i, line in enumerate(lines):

		if i == 0:
			last_tab_cnt = prefix_tab_cnt(line)
			final.append(line)
			continue

		line_tab_cnt = prefix_tab_cnt(line)

		if line_tab_cnt > last_tab_cnt:

			final.extend(format_braces(last_tab_cnt, line_tab_cnt, '{'))
			final.append(line)

		elif line_tab_cnt < last_tab_cnt:

			final.extend(format_braces(last_tab_cnt-1, line_tab_cnt-1, '}'))
			final.append(line)

		else:
			final.append(line)


		last_tab_cnt = line_tab_cnt

	return '\n'.join(final)





def error_detection(txt):

	def mixed_tabs_spaces(_txt):
		spaces = False
		tabs = False
		for c in _txt:
			if c == ' ':
				spaces = True
			elif c == '\t':
				tabs = True
			else:
				break

		return (spaces and tabs)



	for i, line in enumerate(txt.splitlines()):

		if mixed_tabs_spaces(line):
			return (True, f'Error: Mixed tabs and spaces on line {i+1}')

		elif line.startswith(' '):

			if ( len(line) - len(line.lstrip()) ) % 4 != 0:
				return (True, f'Error: Number of prefix spaces on line {i+1} not a multiple of 4')

	return (False, '')






def uncurse(txt):

	is_error, error_text = error_detection(txt)
	if is_error:
		print('\n' + error_text)
		return error_text


	txt = uncommentify(txt)
	
	txt = '\n'.join([line for line in txt.splitlines() if not len(line.strip()) == 0])
	# Remove empty lines

	txt = bracify(txt)
	txt = semicolonify(txt)

	return txt




if __name__ == '__main__':

	import argparse

	parser = argparse.ArgumentParser()

	parser.add_argument('-f', '--file', help = 'input filename')

	args = parser.parse_args()

	if args.file:
		with open(args.file, 'r') as f:
			with open('uncursed_' + args.file, 'w') as f2:
				f2.write(uncurse(f.read()))
	else:
		import clipboard
		clipboard.copy(uncurse(clipboard.paste()))