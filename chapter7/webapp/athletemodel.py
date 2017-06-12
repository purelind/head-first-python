import pickle

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)
    (mins, secs) = time_string.split(splitter)
    return mins + '.' + secs


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)

    def top3(self):
        return sorted(set([sanitize(t) for t in self]))[0:3]


def get_coach_data(filename):
    """

    :param filename: type **.txt, a txt file including name/birthday/training time imformations
    :return: type AthleteList class, example.name/example.dob/example.times
    """
    try:
        with open(filename) as f:
            data = f.readline()
        templ = data.strip().split(',')
        return AthleteList(templ.pop(0), templ.pop(0), templ)
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None


def put_to_store(files_list):
    """

    :param files_list: type list: eg: ['sarah.txt', 'james.txt']
    :return: all_athletes: type dict, dict which store all athletes' training imformaion/name
    """
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        # each athlete's name as key
        # the value is object instance of AthleteList
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error(put_and_store):' + str(ioerr))
    return all_athletes


def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            # put the all pickle into all_athletes dict
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error(get_from_store): ' + str(ioerr))
    return all_athletes

the_files = ['sarah2.txt', 'james2.txt', 'mikey2.txt', 'julie2.txt']
data = put_to_store(the_files)
print(data)

for each_athlete in data:
    print(data[each_athlete].name + " " + data[each_athlete].dob)


data_copy = get_from_store()
for each_athlete in data_copy:
    print(data_copy[each_athlete].name + " " + data_copy[each_athlete].dob)
