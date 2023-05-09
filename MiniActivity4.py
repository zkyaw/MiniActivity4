import threading
import multiprocessing
import time

pasaloadTransaction = multiprocessing.Value('i', 0)
lock = threading.Lock()

def pasaload(amount):
    global pasaloadTransaction
    with lock:
        pasaloadTransaction.value += amount
        print(f"P{amount}.00 is loaded to - 09199999999")

def main():
    p1 = multiprocessing.Process(target=pasaload, args=(10,))
    p2 = multiprocessing.Process(target=pasaload, args=(50,))
    p3 = multiprocessing.Process(target=pasaload, args=(100,))

    p1.start()
    p2.start()
    p3.start()

    p1.join()
    p2.join()
    p3.join()

if __name__ == '__main__':
    main()
