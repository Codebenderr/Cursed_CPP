import sys



def prefix_tab_cnt(txt):

		if len( txt.strip() ) == 0:
			return 0

		if txt.startswith('\t'):
			return len(txt) - len(txt.lstrip())

		if txt.startswith(' '):
			return (len(txt) - len(txt.lstrip()))//4

		return 0




def semicolonify(txt):

	lines = txt.splitlines()

	final = []


	for i, line in enumerate(lines):

		if line.strip() == '{':
			for x in range(i-1, -1, -1):
				if len( final[x].strip() ) > 0:

					if final[x].rstrip().endswith(';'):
						final[x] = final[x].rstrip()[0:-1]

					break

			final.append(line)

		elif line.strip() == '}':
			final.append(line)

		elif line.lstrip().startswith('#'):
			final.append(line)

		elif len( line.strip() ) == 0:
			final.append(line)

		else:

			if line.rstrip().endswith(';'):
				final.append(line)

			else:
				final.append(line + ';')



	return '\n'.join(final)




def bracify(txt):


	def format_braces(n1, n2, brace_type):

		final = []

		if n1 <= n2:
			for i in range(n1, n2):
				final.append(i*'\t' + brace_type)

		else:
			for i in range(n1, n2, -1):
				final.append(i*'\t' + brace_type)

		return final



	lines = txt.splitlines()
	lines.append('')


	final = []


	for i, line in enumerate(lines):

		if i == 0:
			last_tab_cnt = prefix_tab_cnt(line)
			continue

		if len( line.strip() ) == 0 and i != len(lines)-1:
			final.append(line)
			continue


		line_tab_cnt = prefix_tab_cnt(line)


		diff = line_tab_cnt - last_tab_cnt


		if diff > 0:

			final.extend(format_braces(last_tab_cnt, line_tab_cnt, '{'))
			final.append(line)

		elif diff < 0:

			final.extend(format_braces(last_tab_cnt-1, line_tab_cnt-1, '}'))
			final.append(line)

		else:
			final.append(line)


		last_tab_cnt = line_tab_cnt


	return '\n'.join(final)





def uncurse(txt):
	
	txt = bracify(txt)
	txt = semicolonify(txt)

	return txt





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
		print('\u001b[31m' + '\n[!] Invalid number of arguments [!]' + '\u001b[0m')