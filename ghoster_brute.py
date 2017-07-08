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
#n_1 = len(Alphabet)
#n_2 = n_1 - 1 # <-- total useless peice of garbage that could of been great in vurtual life
#n_3 = '0' * n_2
#n = '1' + n_3
x = range_num
y = len(Alphabet)
amount = math.pow(y, x)
total_items = amount
for CharLength in range(range_num, stopper):
    passwords = (itertools.product(Alphabet, repeat = CharLength))

    for i in passwords:
        counter += 1
        percentage = (counter / total_items) * 100
        amount -= 1
        i = str(i)
        f.write(i[0])
        f.write('\n')
        print "Password: %r\tPercentage: %r/100\tAmount left: %r" % (i, int(percentage), amount)
        if i == '0'* range_num:
            print "*Done"
            f.close()
            exit(0)
        else:
            pass

