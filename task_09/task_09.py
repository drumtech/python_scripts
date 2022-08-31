import os
import psutil


user = os.getlogin()
tot_mem = psutil.virtual_memory().total
used_mem = psutil.virtual_memory().used
percent_mem = psutil.virtual_memory().percent


dictionary = {'user_name': user, 'memory_total': tot_mem, 'memory_used': used_mem, 'memory_percent': percent_mem}

for el,val in os.environ.items():
    print(f'Key = {el}        Value = {val}')
