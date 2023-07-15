import requests
import threading
import time
"""
Download example using threads and procedural
"""

urls = [
    "http://www.google.com",
    "http://www.amazon.com",
    "http://www.microsoft.com",
    "http://www.facebook.com"
]

def fetch_url(url):
    response = requests.get(url)
    print(f"{response.status_code}: {url}")

def procedural():
    start = time.time()
    for url in urls:
        fetch_url(url)
    end = time.time()

    print(f"procedural took: {end - start} secs")

def using_threads():
    start = time.time()
    threads = []
    for url in urls:
        thread = threading.Thread(target=fetch_url, args=(url,))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    end = time.time()
    print(f"Thread took: {end - start} secs")
    

procedural()
using_threads()