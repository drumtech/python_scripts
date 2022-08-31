##### First part of task
first_string = 'May 24 12:48:31 ideapad systemd[1]: logrotate.service: Succeeded.'

part_one = first_string.split()
print(" ".join(part_one[0:3]))
print("".join(part_one[4]))
print(first_string.replace('ideapad', 'PC-12092'))
print(first_string.find('failed'))
print(first_string.upper().count('S'))

time = "".join(part_one[2])
summa_time = int(time.split(sep=':')[0]) + int(time.split(sep=':')[1]) + int(time.split(sep=':')[2])
print(summa_time)


##### Second part of task
second_string = 'May 24 14:03:01 ideapad colord[844]: failed to get session [pid 8279]: Нет доступных данных'

part_two = second_string.split()
PC_name = "".join(part_two[3])
service_name = "".join(part_two[4])
date = " ".join(part_two[0:2])
time = "".join(part_two[2])

part_two = second_string.split(sep=': ')
message = "".join(part_two[1])
reasone = "".join(part_two[-1])

print(f'The PC "{PC_name}" receive message from service "{service_name}" what says "{message}" because "{reasone}" at {date}, {time}')
