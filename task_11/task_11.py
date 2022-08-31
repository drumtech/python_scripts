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

