key = { '2':'`', '3':'1', '4':'2', '5':'3', '6':'4', '7':'5', '8':'6', '9':'7', '0':'8', '-':'9', '=':'0',
		'e':'q', 'r':'w', 't':'e', 'y':'r', 'u':'t', 'i':'y', 'o':'u', 'p':'i', '[':'o', ']':'p', '\\':'[',
		'd':'a', 'f':'s', 'g':'d', 'h':'f', 'j':'g', 'k':'h', 'l':'j', ';':'k', '\'':'l',
		'c':'z', 'v':'x', 'b':'c', 'n':'v', 'm':'b', ',':'n', '.':'m', '/':','}
		
while True:
	try:
		n = list(input())
	except EOFError:
		break
	
	for i in n:
		i = i.lower()
		if i != ' ':
			print(key[i], end="")
		else:
			print(" ", end="")
		
	print("")
