import paramiko
import time


key = 'path_for_your_pub_part_of_ssh_key'
commands = 'puppet agent -t'
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
host = open("list", "r")
for hostname in host:
    hostname = hostname.strip()
    hostname_logging = 'Connecting to host: ' + hostname
    print(hostname_logging)
    client.connect(hostname, username = 'root', port = 22, key_filename = key)
    stdin, stdout, stderr = client.exec_command(commands)
    print(stdout.read())
    time.sleep(1)
    client.close
