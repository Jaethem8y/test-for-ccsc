import threading
import requests
import time

def ping():
    for i in range(100):
        res = requests.get("http://127.0.0.1:8000/audit/data_dict")
        res = requests.get("http://127.0.0.1:8080/audit/CALL8786")
        res = requests.get("http://127.0.0.1:8080/audit/RCFA5311")
        res = requests.get("http://127.0.0.1:8080/audit/RCFD0090")
        res = requests.get("http://127.0.0.1:8080/audit/RCFD0081")

        print(i)


def main():
    threads = []
    for i in range(10):
        thread = threading.Thread(target=ping)
        threads.append(thread)
    start = time.perf_counter()
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    end = time.perf_counter()
    print(f"{end - start:0.4f} seconds")

if __name__ == "__main__":
    main()