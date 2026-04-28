import os

def recursivelistdir(path):
	try:
		ans = os.listdir(path)
		for x in os.listdir(path):
			if os.path.isdir(os.path.join(path, x)):
				curr = recursivelistdir(os.path.join(path, x))
				for y in curr:
					ans.append(os.path.join(x, y))
		return sorted(set(ans))
	except PermissionError:
		return ["NO ACCESS TO: {0}".format(path)]

def create_list(path, listfilename="list.txt", levelmarker = '—\\'):
	with open(os.path.join(path, listfilename), mode='w+', encoding='utf8') as f:
		ld = recursivelistdir(path)
		for x in ld:
			if levelmarker is None:
				s = x + '\r\n'
			else:
				s = levelmarker * x.count('\\') + x.split('\\')[-1] + '\r\n'
			f.write(s)
