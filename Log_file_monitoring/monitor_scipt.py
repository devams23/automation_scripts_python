import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from sendMail import send_mail


class LogFileHandler(FileSystemEventHandler):
    def __init__(self, file_path, keywords):
        self.file_path = file_path
        self.keywords = keywords
        self.last_position = 0  # Track the last read position in the file

        # Start from the end of the file
        with open(self.file_path, 'r') as file:
            self.last_position = file.tell()

    def on_modified(self, event):
        # Check if the modified file is the target log file
        print(event.src_path)
        if event.src_path.endswith(self.file_path):
            with open(self.file_path, 'r') as file:
                # Move to the last position to read new lines
                file.seek(self.last_position)
                lines = file.readlines()
                self.last_position = file.tell()  # Update the last position
                
                # Check each new line for keywords
                for line in lines:
                    for keyword in self.keywords:
                        if keyword in line:
                            self.alert(line)

    def alert(self, line):
        # Handle alerting (print, email, Slack, etc.)
        send_mail(
            sender_email="",
            sender_password="",
            recipient_email="",
            subject="Alert!",
            body=f"ALERT: Found keyword in log: {line.strip()}"
        )        
        


def monitor_log(file_path, keywords):
    # Get the directory path from the file path
    directory_path = '/'.join(file_path.split('/')[:-1]) 
    file_name = file_path.split('/')[-1]

    event_handler = LogFileHandler(file_name, keywords)
    observer = Observer()
    observer.schedule(event_handler, path=directory_path, recursive=False)
    observer.start()

    try:
        print(f"Monitoring log file: {file_path} for keywords: {keywords}")
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()


if __name__ == "__main__":
    # Path to the log file
    log_file_path = "path to the log file"

    # Keywords to look for
    keywords_to_monitor = ["ERROR", "CRITICAL"]

    # Start monitoring the log file
    monitor_log(log_file_path, keywords_to_monitor)
