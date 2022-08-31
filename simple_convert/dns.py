future_file = open('my_completed_file.json', 'w', encoding='UTF-8') 

with open ('my_file_ready_to_convert', 'r', encoding='UTF-8') as file_1:
    for el in file_1:
        el_mod = el.split(':')
        future_file.write(f'  {{"target":"{el_mod[0]}","data":"{el_mod[2].strip()}.","type":"{el_mod[1]}"}},\n')
