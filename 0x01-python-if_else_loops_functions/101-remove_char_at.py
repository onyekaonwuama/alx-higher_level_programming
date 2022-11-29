#!/usr/bin/python3
def remove_char_at(str, n):
	list0 = list(str)
	i = n
	for i in range(n, len[list0]):
		list0[i] = list0[i + 1]
	str = ''.join(list0)
	return str
