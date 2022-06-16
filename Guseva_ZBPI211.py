import json


# 1
def fact(x):
    if x == 1:
        return x
    else:
        return x * fact(x - 1)


# 2
def filter_even(li):
    return list(filter(lambda x: x % 2 == 0, li))


# 3
def square(li):
    return list(map(lambda x: x ** 2, li))


# 4
def bin_search(li, element):
    left = 0
    right = len(li)
    while left < right:
        half = (left + right) // 2
        if li[half] == element:
            return half
        elif li[half] < element:
            left = half + 1
        else:
            right = half
    return -1


# 5
def is_palindrome(string):
    string = ''.join(filter(lambda x: x.isalpha(), string))
    a = 0
    b = len(string) - 1
    while a != len(string) // 2:
        if string[a].lower() != string[b].lower():
            return "NO"
        a = a + 1
        b = b - 1
    return "YES"


# 6
def calculate(path2file):
    file = open(path2file, 'r')
    calc = ''
    a = str(file.read()).split('\n')
    file.close()
    lists = []
    for i in range(len(a)):
        n = a[i].split('    ')
        lists.append(n)
    for i in range(len(lists)):
        if lists[i][0] == '+':
            result = int(lists[i][1]) + int(lists[i][2])
            calc = calc + str(result) + ','
        if lists[i][0] == '-':
            result = int(lists[i][1]) - int(lists[i][2])
            calc = calc + str(result) + ','
        if lists[i][0] == '*':
            result = int(lists[i][1]) * int(lists[i][2])
            calc = calc + str(result) + ','
        if lists[i][0] == '//' and int(lists[i][1]) > 0 and int(lists[i][2]) > 0:
            result = int(lists[i][1]) // int(lists[i][2])
            calc = calc + str(result) + ','
        if lists[i][0] == '%' and int(lists[i][1]) > 0 and int(lists[i][2]) > 0:
            result = int(lists[i][1]) % int(lists[i][2])
            calc = calc + str(result) + ','
        if lists[i][0] == '**' and int(lists[i][1]) >= 0 and int(lists[i][2]) >= 0:
            result = int(lists[i][1]) ** int(lists[i][2])
            calc = calc + str(result) + ','
    calc = calc[:-1]
    return calc


# 7
def substring_slice(path2file_1, path2file_2):
    x = open(path2file_1, 'r')
    y = open(path2file_2, 'r')
    a = str(x.read()).split('\n')
    b = str(y.read()).split('\n')
    x.close()
    y.close()
    coordinates = []
    for i in range(len(b)):
        n = b[i].split()
        coordinates.append(n)
    result = ''
    for i in range(len(a)):
        result = result + a[i][int(coordinates[i][0]):int(coordinates[i][1]) + 1] + ' '
    result = result[:-1]
    return result


# 8
def decode_ch(sting_of_elements):
    capital_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    periodic_table = json.load(open('periodic_table.json'))
    result = ''
    for i in range(len(sting_of_elements)):
        if sting_of_elements[i:i + 1] in capital_letters:
            if sting_of_elements[i + 1:i + 2] not in capital_letters:
                if sting_of_elements[i:i + 1] + sting_of_elements[i + 1:i + 2] in periodic_table:
                    result = result + periodic_table[sting_of_elements[i:i + 1] + sting_of_elements[i + 1:i + 2]]
                else:
                    pass
            if sting_of_elements[i + 1:i + 2] in capital_letters:
                if sting_of_elements[i:i + 1] in periodic_table:
                    result = result + periodic_table[sting_of_elements[i:i + 1]]
                else:
                    pass
    return result


# 9
class Student:
    def __init__(self, name, surname, grades=[3, 4, 5]):
        self.name = name
        self.surname = surname
        self.fullname = name + ' ' + surname
        self.grades = grades

    def mean_grade(self):
        return sum(self.grades) // len(self.grades)

    def is_otlichnik(self):
        if self.mean_grade() >= 4.5:
            return 'YES'
        else:
            return 'NO'

    def greeting(self):
        return 'Hello, I am Student'

    def __add__(self, other):
        return self.name + ' is friends with ' + other.name

    def __repr__(self):
        return self.fullname


# 10
class MyError(Exception):
    def __init__(self, msg):
        self.msg = msg
