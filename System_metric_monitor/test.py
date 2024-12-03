import psutil

mem = psutil.virtual_memory().percent
print(mem)