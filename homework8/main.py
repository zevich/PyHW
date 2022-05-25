
from datetime import datetime, timedelta
from collections import defaultdict

days_name = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}
filename = 'users.txt'
dict ={}
finish_dict = defaultdict(list)

# Функция превращает нашу строку с датой в формат datetime и выводит день недели
#соответствующий этой дате
def day_of_week(date: str):
    d, m, y = date.split('.')
    date = datetime(day=int(d), month=int(m), year=int(y))
    d_name = days_name.get(date.weekday())
    return d_name


def get_birthdays_per_week(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        data = file.read()
    for i in data.split(','):
        k,v = i.split(' ')
        dict.update({k:v})
    print(dict)
    

    d = datetime.now()
    #d = datetime(year=2022, month=5, day=23, hour=19, minute=36, second=30)
    print(d)
    
    if (d.weekday() == 0):
        start_date = d + timedelta(days=-2)
        end_date = d + timedelta(days=4)
    else:
        start_date = d

        end_date = d + timedelta(6-start_date.weekday()-2)
        
    delta =  timedelta(days=1)
    print(end_date)

    while (start_date <= end_date):
    
        for k,v in dict.items():
            d_new = datetime.strptime(v, '%d.%m.%Y')
            if (d_new.month == start_date.month) and (d_new.day == start_date.day):
                #print (start_date.date())
                if (d > start_date):
                    new_v = days_name.get(0)
                    #print(new_v)
                    finish_dict[new_v].append(k)
                else:    
                    new_v = days_name.get(start_date.weekday())
                    #print(new_v)
                    finish_dict[new_v].append(k)
        start_date += delta  
    for k,v in finish_dict.items():
        v = ','.join(v)
        print(k + ':' +v)
get_birthdays_per_week(filename)
