########################################################
# Credit goes to thegeniesghost@gmail.com			   #
# You can now hack any password in the world with this #
# Whatever any person(S) do with this code is not      #
# my or any other developers fault                     #
# and have no legal obligation to require payments     #
# Just basicly dont be a c**t with this tool           #
########################################################
import itertools, math
import os
Alphabet = ("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890") # Add or remove whatevs you think will be in the password you're cracking (example, [symbols])
counter = 1
CharLength = 1
range_num = int(raw_input("Enter range: "))
stopper = range_num + 1
filename = "bruteforce_%r.txt" % (range_num)
f = open(filename, 'a')
x = range_num
y = len(Alphabet)
amount = math.pow(y, x)
total_items = math.pow(y, x)
for CharLength in range(range_num, stopper):
    passwords = (itertools.product(Alphabet, repeat = CharLength))

	for i in passwords:
		counter += 1
		percentage = (counter / total_items) * 100
		amount -= 1
		i = str(i)
		i = i.replace("[", "")
		i = i.replace("]", "")
		i = i.replace("'", "")
		i = i.replace(" ", "")
		i = i.replace(",", "")
		i = i.replace("(", "")
		i = i.replace(")", "")
        f.write(i)
		f.write('\n')
		print "Password: %r\tPercentage: %r/100\tAmount left: %r" % (i, int(percentage), amount)
		if i == '0'* range_num:
            print "*Done"
			f.close()
			exit(0)
		else:
			pass
