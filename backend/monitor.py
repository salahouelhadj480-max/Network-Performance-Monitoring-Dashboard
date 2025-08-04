import os
import subprocess

def ping_host(host):
    response = os.system(f"ping -c 1 {host}")
    return response == 0

def get_latency(host):
    try:
        output = subprocess.check_output(f"ping -c 1 {host}", shell=True).decode()
        for line in output.split('\n'):
            if "time=" in line:
                latency = float(line.split("time=")[1].split(" ")[0])
                return latency
    except Exception:
        return None
