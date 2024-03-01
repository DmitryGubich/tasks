import hashlib
import random
import string
from threading import Thread, Lock


class TinyUrl:
    def __init__(self):
        self.prefix = "https://www.tiny-url.com/"
        self.lock = Lock()
        self.storage = {}

    def get(self, url: str):
        return self.storage.get(url)

    def put(self, url: str):
        with self.lock:
            if not self.storage.get(url):
                self.storage[url] = self.prefix + hashlib.md5(b"url").hexdigest()

    def delete(self, url: str):
        with self.lock:
            if self.storage.get(url):
                del self.storage[url]


if __name__ == "__main__":
    tiny_url = TinyUrl()
    URL = "https://www.youtube.com/"

    num_threads = 8
    threads = [0] * num_threads

    for i in range(0, num_threads):
        url = "".join(random.choice(string.ascii_uppercase) for _ in range(10))
        threads[i] = Thread(target=tiny_url.put(url))

    for i in range(0, num_threads):
        threads[i].start()

    for i in range(0, num_threads):
        threads[i].join()
