from __future__ import print_function
import smtplib
import sched, time
import random
import datetime

def send_email(username):
    with open('addresses.txt') as f:
        plain = f.readlines()
    nums = []
    for p in plain:
        nums.append(p.rstrip('\n'))

    for num in nums:
        server.sendmail(username, num, msg)
    print('Sent: %s\n' % msg)

with open('animals.txt') as f:
    pre = f.readlines()

animals = []

for p in pre:
    animals.append(p.rstrip('\n'))

with open('credentials.txt') as f:
    content = f.readlines()

username = content[0].rstrip('\n')
password = content[1].rstrip('\n')

while 1:
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)

    my_int = int(random.random() * (len(animals) - 1));
    msg = "Need a cute pic of " + animals[my_int]

    send_email(username)
    minute_delay = 10 + random.random() * 20 # number of minutes between each text (random between 10 and 30)
    print (datetime.datetime.now())

    server.quit()
    time.sleep(60 * minute_delay)
