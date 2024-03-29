import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import os, platform

class Watcher:
    DIRECTORY_TO_WATCH = "."  # The directory to watch, "." means the current directory
    FILE_TO_WATCH = "character-counting.py"  # The specific file you want to watch

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.DIRECTORY_TO_WATCH, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except KeyboardInterrupt:
            self.observer.stop()
            print("Observer Stopped")

        self.observer.join()

class Handler(FileSystemEventHandler):
    @staticmethod
    def clear_screen():
        if platform.system == "Windows":
            os.system('cls')
        else:
            os.system('clear')

    last_modified = time.time()
    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None

        current_time = time.time()
        if current_time - Handler.last_modified < 0.01:
            return

        Handler.last_modified = current_time

        if event.event_type == 'modified':
            # Check if the modified file is the file to watch
            if event.src_path.endswith(Watcher.FILE_TO_WATCH):
                Handler.clear_screen()
                print(f"{Watcher.FILE_TO_WATCH} has been modified. Running it below here:\nv v v v v v v v v v v v v v v v v v\n")
                subprocess.run(["python", Watcher.FILE_TO_WATCH])


if __name__ == "__main__":
    w = Watcher()
    w.run()

