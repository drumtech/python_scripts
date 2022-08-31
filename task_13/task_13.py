import psutil
import os
import socket

class PC_memory:
    def __init__(self, value, name, mem_tot, mem_used, mem_per=0):
        self.pc_id = value
        self.user_name = name
        try:
            self.memory_total = int(mem_tot)
            if self.memory_total < 0:
                raise ValueError
        except ValueError:
            print('wrong memory value, default value used')
            self.memory_total = 107374182400
            self.memory_used = 0
            self.memory_percent = 0
        try:
            self.memory_used = int(mem_used)
            if self.memory_used > self.memory_total:
                raise ValueError
            elif self.memory_used < 0:
                raise ValueError
        except ValueError:
            print('wrong memory value, default value used')
            self.memory_total = 107374182400
            self.memory_used = 0
            self.memory_percent = 0
        try:
            memory_proc = float(mem_per)
            if 100 >= memory_proc > 0:
                self.memory_percent = memory_proc
            else:
                self.memory_percent = round((self.memory_used * 100) / self.memory_total, 2)
                try:
                    if memory_proc < 0 or memory_proc > 100:
                        raise PercentError
                except Exception:
                    print('Percent value must be between 0 and 100')
        except ValueError:
            print('wrong percent value, value calculated automatically')
            self.memory_percent = round(((self.memory_used * 100) / self.memory_total), 2)
    def show_used_percent(self):
        print(f'PC with id {self.pc_id} used {round(self.memory_percent, 2)} percent of memory')
    def is_enough_memory(self):
        mem_left = ((((self.memory_total - self.memory_used) / 1024) / 1024) / 1024)
        if self.memory_percent > 90 or mem_left < 1:
            return False
        else:
            return True
    def get_values(self):
        return f'{self.pc_id} {self.user_name} {self.memory_total} {self.memory_used} {self.memory_percent}'


class PercentError(Exception):
    pass

### Доверимся машине
a = PC_memory(socket.gethostname(), os.getlogin(), psutil.virtual_memory().total, psutil.virtual_memory().used)
print(a.get_values())

### Пользователь адекватный
b = PC_memory(socket.gethostname(), os.getlogin(), 33351860224, 13351860224, 38)
print(b.get_values())
### tot = 33351860224 used = 13351860224
### Пользователь не адекватный
c = PC_memory(socket.gethostname(), os.getlogin(), '53351860224', '13351860224', 'dnina')
print(c.get_values())
