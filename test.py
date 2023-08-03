import json
from datetime import datetime

with open('competitors2.json', 'r', encoding='utf-8') as f:
    competitors = json.load(f)

with open('results_RUN.txt', 'r', encoding='utf-8-sig') as f:
    results = f.read()

results_lst = results.split('\n')

if '' in results_lst:
    results_lst.remove('')

competitors_time = []
for i in range(0, len(results_lst), 2):
    competitors_time.append([results_lst[i].split()[0],
                datetime.strptime(results_lst[i+1].split()[2], '%H:%M:%S,%f') -
                datetime.strptime(results_lst[i].split()[2], '%H:%M:%S,%f')])

competitors_time.sort(key=lambda x: x[1])

res = []
for rate, competitor in enumerate(competitors_time, 1):
    res.append([str(rate),
                competitor[0],
                competitors[competitor[0]]['Name'],
                competitors[competitor[0]]['Surname'],
                datetime.strptime(str(competitor[1]), '%H:%M:%S.%f').strftime('%M:%S,%f')[:-4]
                ])

print('| Занятое место | Нагрудный номер |     Имя      |   Фамилия   | Результат |')
for i in res:
    print(f'| {i[0].ljust(14, " ")}'
          f'| {i[1].ljust(16, " ")}'
          f'| {i[2].ljust(13, " ")}'
          f'| {i[3].ljust(12, " ")}'
          f'| {i[4]}  |')
