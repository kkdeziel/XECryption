#hackthissite realistic 5: xecryption
#takes 3 args: input, outputed addition of triplets, output of all possible decryptions

import sys

summ = 0
count = 0

with open(sys.argv[1], "r") as inp:
	with open(sys.argv[2], "w") as outp:
		for line in inp:

			nums = line.split(".")

			for l in nums:
				if len(l) > 1:
					summ = summ + int(l)
				else:
					continue
				if count != 2:
					count += 1
				else:
					outp.write(str(summ))
					outp.write('\n')
					summ = 0
					count = 0


allNums = list()

with open(sys.argv[2], "r") as inp:
	with open(sys.argv[3], "w") as outp:
		for line in inp:
			allNums.append(int(line))
		unsorted = list(allNums)
		allNums.sort()

		r = 128 - (allNums[len(allNums) - 1] - allNums[0])
		print (r)

		for hi in range (0, r):
			for fi in unsorted:
				newNum = fi + hi - allNums[0]
				try:
					outp.write(unichr(newNum))
				except:
					print (str(fi) + ' ' + str(hi) + ' ' + str(newNum))
			outp.write('\n')

