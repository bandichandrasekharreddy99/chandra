# chandr

n = raw_input()
if(n >= 'a' and n <= 'z') or (n >= 'A' and n <= 'Z'):
	if n in ['a','e','i','o','u','A','E','I','O','U']:
		print('vowel')
	else:
		print('Consonant')
else:
	print('invalid')
