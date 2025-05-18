import socket, paramiko, telnetlib



def find_vulnerable_machines():
    '''Scans IP addresses 10.13.4.x where x is between 0 and 255
    for open SSH and Telnet ports. if an open port is found, it writes the address
    to two files: open_ssh.log and open_telnet.log.'''
    
    #Opens the files in append mode
    ssh_file = open('open_ssh.log', 'a')
    telnet_file = open('open_telnet.log', 'a')

    #Iterate through all IP addresses in the range
    for i in range(256):
        #ip address being scanned
        ip = f'10.13.4.{i}'
        
        #Check for open SSH port
        ssh = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ssh.settimeout(1)
        #Set the timeout to 1 second so that the ports can be scanned quickly
        #check if the port is open, port 22 is the default SSH port
        result = ssh.connect_ex((ip, 22))
        #Note that connect_ex is used instead of connect. This is so we can avoid using a try/except block
        if result == 0:
            #write the IP address to the file
            print(f'SSH open on {ip}')
            ssh_file.write(f'{ip}\n')
        ssh.close() #Destroy the socket object

        #Check for open Telnet port
        telnet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        telnet.settimeout(1)
        #check if the port is open, port 23 is the default Telnet port
        result = telnet.connect_ex((ip, 23))
        if result == 0:
            #write the IP address to the file
            print(f'Telnet open on {ip}')
            telnet_file.write(f'{ip}\n')
        telnet.close()  #Destroy the socket object

    #Close the files
    ssh_file.close()
    telnet_file.close()

if __name__ == '__main__':
    find_vulnerable_machines()
