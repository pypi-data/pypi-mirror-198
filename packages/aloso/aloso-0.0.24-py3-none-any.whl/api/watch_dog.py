import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

FILE_PATH = "/home/exnovo/PycharmProjects/network/data/switch/inventory/inventory.ini"


class InventoryChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path == FILE_PATH:
            with open(event.src_path, 'r') as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines):
                    if line != self._previous_lines[line_num]:
                        print(f"Line {line_num + 1} changed from: {self._previous_lines[line_num].strip()}")
                        print(f"\t\t\t\t to: {line.strip()}")
                self._previous_lines = lines

    def __init__(self):
        with open(FILE_PATH, 'r') as f:
            self._previous_lines = f.readlines()


if __name__ == "__main__":
    event_handler = InventoryChangeHandler()
    observer = Observer()
    observer.schedule(event_handler, os.path.dirname(FILE_PATH), recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
