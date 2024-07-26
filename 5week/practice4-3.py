from fixed_queue import FixedQueue

def main():
    queue = FixedQueue(10)

    for i in range(1, 6):
        queue.enque(i)

    queue.dump()

    print("Peek:", queue.peek())

    print("Deque:", queue.deque())
    queue.dump()

    queue.enque(6)
    queue.dump()

    print("Find 3:", queue.find(3))
    print("Count 3:", queue.count(3))
    print("Contains 3:", 3 in queue)

if __name__ == "__main__":
    main()