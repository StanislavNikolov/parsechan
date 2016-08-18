import datetime
import json
import re
import os

thread = json.loads(input())

def fixCom(str):
    str = str.replace('<br>', '\n')
    str = re.sub('<.*?>', '', str)
    str = str.replace('&gt;', '>').replace('&lt;', '<')
    str = str.replace('&#039;', '\'').replace('&quot;', '\"')

    return str

def getTermSize():
    fp = os.popen('tput cols', 'r')
    line = fp.readline()
    fp.close()

    return int(line)

def setColor(char):
    if char == 'r':
        print('[31m', end='')
    elif char == 'g':
        print('[32m', end='')
    else:
        print('[39m', end='')


cols = getTermSize()

for post in thread:
    #date = datetime.date.fromtimestamp(post['time']).strftime('%F %T')
    date = post["now"]

    setColor('d')
    print('╭─', end='')

    setColor('d')
    print(' ' + date + ' ', end='')

    setColor('d')
    print('──', end='')

    setColor('r')
    print(' ' + str(post['no']) + ' ', end='')

    setColor('d')
    print('─' * (cols - len(str(post['no'])) - len(date) - 9 ), end='')
    print('╮')

    if 'com' not in post:
        post['com'] = ''

    if type(post['com']) is not str:
        post['com'] = ''

    for line in fixCom(post['com']).split('\n'):
        curr = 0
        end = len(line)

        color = 'd'
        if end > 1 and line[0] == '>' and line[1] == '>':
            color = 'r'
        elif end > 1 and line[0] == '>' and line[1] != '>':
            color = 'g'

        while curr < end:
            setColor('d')
            print('│', end='')

            setColor(color)
            print(line[curr:curr+cols-2], end='')

            if curr + cols >= end:
                print(' ' * (cols - end + curr - 2), end='')

            setColor('d')
            print('│')

            curr = curr + cols - 2

    setColor('d')
    print('╰' + '─' * (cols - 2) + '╯')
    print()
