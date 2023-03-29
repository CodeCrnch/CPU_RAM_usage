import psutil


cpu_percent = psutil.cpu_percent(percpu=True, interval=1)

ram_percent = psutil.virtual_memory().percent

print("CPU usage/cores: {}%, RAM usage: {}%".format(cpu_percent,ram_percent))
