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

cols = getTermSize()
for post in thread:
    #date = datetime.date.fromtimestamp(post['time']).strftime('%F %T')
    date = post["now"]

    print('╭─', end='')
    print('[31m', date, '[39m', end='')
    print('─', end='')
    print('[31m', post['no'], '[39m', end='')
    print('─' * (cols - len(str(post['no'])) - len(date) - 8 ), end='')
    print('╮')

    if 'com' not in post:
        post['com'] = ''

    if type(post['com']) is not str:
        post['com'] = ''

    for line in fixCom(post['com']).split('\n'):
        curr = 0
        end = len(line)
        while curr < end:
            print('│', end='')
            print(line[curr:curr+cols-2], end='')
            if curr + cols >= end:
                print(' ' * (cols - end + curr - 2), end='')
            print('│')
            curr = curr + cols - 2

    print('╰' + '─' * (cols - 2) + '╯')
    print()
