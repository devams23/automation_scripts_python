import psutil
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style
from Log_file_monitoring.sendMail import send_mail

style.use('fivethirtyeight')

# Initialize figure and axes
fig = plt.figure(figsize=(10, 8))

# Subplots for CPU, Memory, and Disk Usage
ax1 = fig.add_subplot(3, 1, 1)  # CPU Usage
ax2 = fig.add_subplot(3, 1, 2)  # Memory Usage
ax3 = fig.add_subplot(3, 1, 3)  # Disk Usage

# Persistent data for the graph
xs = []    # Timestamps (or step numbers)
cpu = []   # CPU usage values
mem = []   # Memory usage values
disk = []  # Disk usage values

def animate(i):
    # Add the next data point
    xs.append(i)  # Increment step number

    cpu_val = psutil.cpu_percent(interval=1)
    mem_val = psutil.virtual_memory().percent
    disk_val = psutil.disk_usage('D:').percent

    #sending mail if the values exceeds the  threshold
    if cpu_val >= 95 or mem_val>= 80:
        print("sending mail")

        send_mail()
        
     
    cpu.append(cpu_val)  # CPU usage
    mem.append(mem_val)  # Memory usage
    disk.append(disk_val)  # Disk usage

    
    # Keep only the last 20 points to avoid overcrowding
    xs[:] = xs[-20:]
    cpu[:] = cpu[-20:]
    mem[:] = mem[-20:]
    disk[:] = disk[-20:]

    # Clear each axis and replot
    ax1.clear()
    ax2.clear()
    ax3.clear()

    ax1.plot(xs, cpu, label="CPU Usage (%)", color='b')
    ax2.plot(xs, mem, label="Memory Usage (%)", color='g')
    ax3.plot(xs, disk, label="Disk Usage (%)", color='r')

    # Add labels, titles, and formatting

    ax1.set_ylabel("CPU Usage (%)")
    ax1.set_ylim(0, 100)
    ax1.legend(loc='upper left')


    ax2.set_ylabel("Memory Usage (%)")
    ax2.set_ylim(0, 100)
    ax2.legend(loc='upper left')

    ax3.set_ylabel("Disk Usage (%)")
    ax3.set_ylim(0, 100)
    ax3.legend(loc='upper left')


# Set up the animation
ani = animation.FuncAnimation(fig, animate, interval=1000)

# Display the plot
plt.tight_layout()
plt.show()
