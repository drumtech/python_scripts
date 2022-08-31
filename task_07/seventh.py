list_1 = ['May 18 11:59:18 PC-00102 plasmashell[1312]: kf.plasma.core: findInCache with a lastModified timestamp of 0 is deprecated', 'May 18 13:06:54 ideapad kwin_x11[1273]: Qt Quick Layouts: Detected recursive rearrange. Aborting after two iterations.', 'May 20 09:16:28 PC0078 systemd[1]: Starting PackageKit Daemon...', 'May 20 11:01:12 PC-00102 PackageKit: daemon start', 'May 20 12:48:18 PC0078 systemd[1]: Starting Message of the Day...', 'May 21 14:33:55 PC0078 kernel: [221558.992188] usb 1-4: New USB device found, idVendor=1395, idProduct=0025, bcdDevice= 1.00', 'May 22 11:48:30 ideapad mtp-probe: checking bus 1, device 3: "/sys/devices/pci0000:00/0000:00:08.1/0000:03:00.3/usb1/1-4"', 'May 22 11:50:09 ideapad mtp-probe: bus: 1, device: 3 was not an MTP device', 'May 23 08:06:14 PC-00233 kernel: [221559.381614] usbcore: registered new interface driver snd-usb-audio', 'May 24 16:19:52 PC-00233 systemd[1116]: Reached target Sound Card.', 'May 24 19:26:40 PC-00102 rtkit-daemon[1131]: Supervising 5 threads of 2 processes of 1 users.']

output_list = []
def parse_log_string(output_list, *args):
    for el in args:
        el_mod = el.split()
        time = "".join(el_mod[2])
        pc_name = "".join(el_mod[3])
        service_name = ("".join(el_mod[4]))[0:-1]
        message = " ".join(el_mod[5:])
        dict_1 = {'time': time, 'pc_name': pc_name, 'service_name': service_name, 'message': message}
        output_list.append(dict_1)




parse_log_string(output_list, list_1[0], list_1[1], list_1[3])
print(output_list)


hdd_state = [
    {'id': 382, 'total': 999641890816, 'used': 228013805568},
    {'id': 385, 'total': 61686008768, 'used': 52522710872},
    {'id': 398, 'total': 149023482194, 'used': 83612310700},
    {'id': 400, 'total': 498830397039, 'used': 459995976927},
    {'id': 401, 'total': 93386008768, 'used': 65371350065},
    {'id': 402, 'total': 988242468378, 'used': 892424683789},
    {'id': 430, 'total': 49705846287, 'used': 9522710872},
]

hdd = {'memory_critical': [], 'memory_not_enough': [], 'memory_ok': []}
def check_free_space(hdd_state):
    for el in hdd_state:
        quantity = ((((int(el['total']) - int(el['used'])) / 1024) / 1024) / 1024)
        percent = 100 - ((int(el['used']) / int(el['total'])) * 100)
        if quantity < 10 or percent < 5:
            hdd['memory_critical'].append(el['id'])
        elif 30 > quantity > 10 or percent < 10:
            hdd['memory_not_enough'].append(el['id'])
        else:
            hdd['memory_ok'].append(el['id'])
check_free_space(hdd_state)
print(hdd)
