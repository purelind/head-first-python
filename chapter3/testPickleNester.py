import pickle
import nester

new_man = []
new_othe = []

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
    with open('other_data.txt', 'rb') as other_file:
        new_other = pickle.load(other_file)
except IOError as err:
    print('File error: ' + str(err))
except pickle.pickleError as perr:
    print('pickling error: ' + str(perr))

nester.print_lol(new_man)
print(new_man[0])
print(new_man[-1])
