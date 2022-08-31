import psutil
import os
import socket

class PC_memory:
    def __init__(self, value, name, mem_tot, mem_used, mem_per=0):
        self.pc_id = value
        self.user_name = name
        self.memory_total = mem_tot
        self.memory_used = mem_used
        if mem_per > 0:
            self.memory_percent = mem_per
        else:
            self.memory_percent = (mem_used * 100) / mem_tot
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

a = PC_memory(socket.gethostname(), os.getlogin(), psutil.virtual_memory().total, psutil.virtual_memory().used)
a.show_used_percent()
print(a.is_enough_memory())

class PC_advanced(PC_memory):
    def __init__(self, value, name, mem_tot, mem_used, la_1, la_15, mem_per=0):
        PC_memory.__init__(self, value, name, mem_tot, mem_used, mem_per)
        self.ld_avg_1m = la_1
        self.ld_avg_15m = la_15
    def is_overloaded(self):
        x = self.ld_avg_1m / self.ld_avg_15m
        if x >= 3:
            return True
        else:
            return False
    def __call__(self, string='memory'):
        if string == 'memory':
            return self.is_enough_memory()
        elif string == 'load':
            return self.is_overloaded()
        else:
            return None
    def get_values_mod(self):
        return f'PC name is -  {self.pc_id}\nUser name is -  {self.user_name}\nMemory total are - {self.memory_total}\nMemory used are - {self.memory_used}\nPercent of used memory are -  {self.memory_percent}\nLA for 1 minute are - {self.ld_avg_1m}\nLA for 15 minutes are - {self.ld_avg_15m}'

b = PC_advanced(socket.gethostname(), os.getlogin(), psutil.virtual_memory().total, psutil.virtual_memory().used, os.getloadavg()[0], os.getloadavg()[2])
print(b.is_overloaded())
print(b())
