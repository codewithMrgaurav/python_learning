import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):  # Check for Python files
            print(f"File {event.src_path} has been modified, running script...")
            subprocess.run(["python", event.src_path])

if __name__ == "__main__":
    path = "."  # Watch the current directory
    event_handler = Watcher()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
