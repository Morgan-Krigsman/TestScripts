import subprocess
import platform
import re

def ping_test(host, count=4):
    # Determine the command based on the operating system
    param = '-n' if platform.system().lower()=='windows' else '-c'
    command = ['ping', param, str(count), host]

    try:
        output = subprocess.check_output(command).decode()
        print(output)

        # Extract latency information
        if platform.system().lower() == 'windows':
            match = re.search(r'Average = (\d+)ms', output)
        else:
            match = re.search(r'avg\/([\d\.]+)', output)
        if match:
            avg_latency = match.group(1)
            print(f'Average Latency to {host}: {avg_latency} ms')
        else:
            print('Could not determine average latency.')
    except subprocess.CalledProcessError:
        print(f'Failed to reach {host}')

if __name__ == '__main__':
    host = input('Enter the host to ping: ')
    count = input('Enter the number of packets to send (default 4): ') or 4
    ping_test(host, int(count))
