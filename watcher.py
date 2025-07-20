from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from parser import load_expenses
from embedder import embed_texts
from vector_store import build_index
import time

def refresh_index():
    texts = load_expenses()
    embeddings = embed_texts(texts)
    build_index(embeddings, texts)
    print("Vector DB updated ✅")

class Watcher(FileSystemEventHandler):
    def on_modified(self, event):
        if event.src_path.endswith(".csv"):
            print("📁 CSV updated...")
            refresh_index()

def start_watching():
    observer = Observer()
    observer.schedule(Watcher(), path="data", recursive=False)
    observer.start()
    refresh_index()
    try:
        while True:
            time.sleep(5)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
