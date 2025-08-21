import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from .checker import check_syntax

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print("\n[Watcher] Checking:", event.src_path)
            check_syntax(event.src_path)

def watch(path="."):
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

def main():
    import sys
    folder = sys.argv[1] if len(sys.argv) > 1 else "."
    print(f"Watching folder: {folder}")
    watch(folder)

if __name__ == "__main__":
    main()
