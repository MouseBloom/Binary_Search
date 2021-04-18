# binary search in the list of numbers
# make sure you have file nubers.txt in the folder, where the program is
import time
l = []


def iterative_search(n, l):
    '''
    :param n: number you are searching for
    :param l: list of numbers
    :return: index of the number
    '''
    first_half = 0
    second_half = len(l)
    search_space = (first_half + second_half) // 2
    while l[search_space] != n:
        if first_half > second_half:
            return None
        if n > l[search_space]:
            first_half = search_space + 1
            search_space = (first_half + second_half) // 2
        else:
            second_half = search_space - 1
            search_space = (first_half + second_half) // 2
    return search_space


def recursive_search(n, l, d):
    '''

    :param n: number you are searching for
    :param l: list of numbers
    :param d: special parameter needed to find index, can`t explain better, further understanding can be founded by looking through the code
    :return:
    '''
    if len(l) == 1 and l[0] != n:
        return None
    first_half = -1
    second_half = len(l)
    search_space = (first_half + second_half) // 2
    if l[search_space] == n:
        return search_space + d
    if n < l[search_space]:
        d += 0
        return recursive_search(n,l[0:search_space+1], d)
    if n > l[search_space]:
        d += search_space + 1
        return recursive_search(n, l[search_space+1:len(l)+1],d)


number = int(input("What nuber are you searching for? "))

option = int(input('How your numbers are written?\n1- lines\n2- one string with spaces ')) # gives you option to choose what type of txt you have
if option == 1:
    with open('numbers.txt', 'r') as fil:
        for line in fil:
            l.append(int(line))
if option == 2:
    f = open('numbers.txt', 'r')
    l = list(map(int,f.readline().strip().split()))


start_time = time.time()
print(iterative_search(number,l), 'Iterative method answer')
print("--- %s ,seconds ---" % (time.time() - start_time), 'Time needed for the iterative method')


start_time = time.time()
print(recursive_search(number,l, 0), 'Recursive method answer ')
print("--- %s milliseconds ---" % (time.time() - start_time), 'Time needed for the recursive method ')
