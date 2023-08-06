import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import asyncio
import websockets


FILE_PATH = "/home/exnovo/PycharmProjects/network/data/switch/inventory/inventory.ini"


class InventoryChangeHandler(FileSystemEventHandler):
    def __init__(self, websocket):
        with open(FILE_PATH, 'r') as f:
            self._previous_lines = f.readlines()
        self.websocket = websocket

    async def on_modified(self, event):
        if event.src_path == FILE_PATH:
            with open(event.src_path, 'r') as f:
                lines = f.readlines()
                for line_num, line in enumerate(lines):
                    if line != self._previous_lines[line_num]:
                        message = f"Line {line_num + 1} changed from: {self._previous_lines[line_num].strip()} to: {line.strip()}"
                        print(message)
                        await self.websocket.send_text(message)
                self._previous_lines = lines



async def main():
    async with websockets.connect('ws://localhost:8500/ws') as websocket:
        handler = InventoryChangeHandler(websocket)
        observer = Observer()
        observer.schedule(handler, os.path.dirname(FILE_PATH), recursive=False)
        observer.start()
        try:
            while True:
                await asyncio.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        observer.join()

if __name__ == "__main__":
    asyncio.run(main())
