import json
import email.utils
import matplotlib.pyplot as plt

with open('table.json', encoding='utf8') as f:
    table = json.loads(f.read())  # Таблица решений задач

with open('failed.json', encoding='utf8') as f:
    failed = json.loads(f.read())  # Данные по ошибкам

with open('messages.json', encoding='utf8') as f:
    messages = json.loads(f.read())  # Полученные сообщения

days = [m['date'][:3] for m in messages]

messages = [(m['subj'].upper(), email.utils.parsedate(m['date']))  for m in messages]
#task 1 Как по времени суток распределяется активность студентов?
lst = list()
for i in messages:
    lst.append(i[1][3])

fig = plt.figure()
plt.plot([i for i in range(24)], [lst.count(i) for i in range(24)], marker='o', color='black')
plt.xlabel('Время суток')
plt.ylabel('Колличество сообщений')
plt.xticks([i for i in range(24)])
#plt.show()

#task 2 Как по дням недели распределяется активность студентов?

#fig = plt.figure()
mp = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
plt.plot(mp, [days.count(i) for i in mp], marker='o', color='black')
#plt.show()

#task 3 В каких группах было отправлено больше всего сообщений?

lst1 = list()

for i in messages:
    lst1.append(i[0][:3].replace(' ', ''))

# fig = plt.figure()
mp1 = set(lst1)
mp1 = list(mp1)
mp1.sort()
plt.plot(mp1, [lst1.count(i) for i in mp1], marker='o', color='black')
#plt.show()

#task 4 В каких группах было получено больше всего правильных решений?

lst2 = list()
for i in table['data']:
    if i[3] == 1:
        lst2.append(i[0])

mp2 = set(lst2)
mp2 = list(mp2)
mp2.sort()
plt.plot(mp2, [lst2.count(i) for i in mp2], marker='o', color='black')
#plt.show()

#task 5 Какие задачи оказались самыми легкими, самыми сложными?

lst3 = list()
for i in table['data']:
    if i[3] == 0:
        lst3.append(i[2])

mp3 = set(lst3)
mp3 = list(mp3)
mp3.sort()
plt.plot(mp3, [lst3.count(i) for i in mp3], marker='o', color='black')
#plt.show()

#task 6 Какие распространенные ошибки совершали студенты?

lst4 = list()
print(failed['Н5 10'])
