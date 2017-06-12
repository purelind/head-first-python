from sanitize import sanitize


def get_coach_data(filename):
    """

    :param filename: eg: 'james.txt'
    :return: list which has removed null and ','
    """
    try:
        with open(filename) as f:
            data = f.readline()
        return data.strip().split(',')
    except IOError as ioerr:
        print('File error: ' + str(ioerr))
        return None

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(sorted(set([sanitize(t) for t in james]))[0:3])
print(sorted(set([sanitize(t) for t in julie]))[0:3])
print(sorted(set([sanitize(t) for t in mikey]))[0:3])
print(sorted(set([sanitize(t) for t in sarah]))[0:3])
