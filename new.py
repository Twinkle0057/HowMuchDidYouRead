import sys

def listToString(t):
	s = ""
	for i in t:
		s = s + " " + i
	return s[1:]

def process(arr):
	bookPages = []
	bookRead = []
	for line in arr:
		line = line.split()
		k = 1
		for word in line:
			if "pages" in word and k == 1:
				word = word.replace("pages", "")
				bookPages.append(int(word))
				k = k+1
			elif "pages" in word and k ==2:
				word = word.replace("pages", "")
				bookRead.append(int(word))
	print(bookRead)
	print(bookPages)
	temp = 0
	tempIndex = 0
	for i in range(len(bookRead)):
		k = float(bookRead[i]/bookPages[i])
		print(k)
		if temp<k:
			temp = k
			tempIndex=i

	sTemp = arr[tempIndex].split()
	t = []
	for word in sTemp:
		if "pages" not in word:
			t.append(word)
	t = listToString(t)
	return t

if __name__ == "__main__":
	input_line1 = sys.stdin.readline()
	n = int(input_line1)
	arr = []
	for i in range(n):
		arr.append(sys.stdin.readline().replace("\n", ""))
	print(process(arr))