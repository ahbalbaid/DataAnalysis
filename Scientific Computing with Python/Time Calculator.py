def add_time(start, duration,day=None): #"3:00 PM", "3:10"
    s = start.split()
    s1= s[0].split(':')
    d = duration.split(':')
    new_time = [0,1,2,3]
    new_time[0] = str(int(s1[0]) + int(d[0]))
    new_time[1] = ':'
    new_time[2] = str(int(s1[1]) + int(d[1]))
    new_time[3] = ' ' + s[1]
    new = ''
    h=0
    orgday=s[1]
    week = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    #count how many hours from mins and subtract mins
    while int(new_time[2]) >= 60:
        new_time[2] = str((int(new_time[2]) - 60))
        h+=1

    new_time[0] = str(int(new_time[0]) + h)
    #add a zero if min is one
    if len(new_time[2]) == 1:
        new_time[2] = '0' + new_time[2]

    #check if the hours are > 12 subtract from 12
    if int(new_time[0]) > 12:
        while int(new_time[0]) > 12:
            new_time[0] = str((int(new_time[0]) - 12))
            if s[1] == 'PM':
                s[1] = 'AM'
                new_time[3] = ' ' + 'AM'
            elif s[1] == 'AM':
                s[1] = 'PM'
                new_time[3] = ' ' + 'PM'

    if int(new_time[0]) == 12:
        if s[1] == 'PM':
            s[1] = 'AM'
            new_time[3] = ' ' + 'AM'
        elif s[1] == 'AM':
            s[1] = 'PM'
            new_time[3] = ' ' + 'PM'
    for i in new_time:
        new += i

    try:
        if orgday == 'PM' and s[1] =='AM' and  int(d[0])+h <=24:
            for i in range(len(week)):
                if week[i].lower() == day.lower():
                    new += f', {week[i+1]}'
        elif orgday == 'AM' and s[1] == 'AM' and int(d[0]) + h <= 24 and int(d[0]) + h >= 12:
            for i in range(len(week)):
                if week[i].lower() == day.lower():
                    new += f', {week[i+1]}'
        elif int(d[0])+h >=24:
            for i in range(len(week)):
                if week[i].lower() == day.lower():
                    A = i+(((int(d[0])+h)//24)+1)
                    while A >= 7:
                        A -= 7
                    new += f', {week[A]}'
        else:
            for i in range(len(week)):
                    if week[i].lower() == day.lower():
                        new += f', {week[i]}'
    except:
        pass

    if orgday == 'PM' and s[1] =='AM' and  int(d[0])+h <=24 :
        new += ' (next day)'
    elif orgday == 'AM' and s[1] =='AM' and int(d[0])+h <=24 and int(d[0])+h>=12:
        new += ' (next day)'
    elif int(d[0])+h >=24:
        new += f' ({ ((int(d[0])+h)//24)+1 } days later)'

    return new

if __name__ == '__main__':
    print(add_time("8:16 PM", "466:02", "tuesday"))