from fixed_stack import FixedStack

def main():
    stack = FixedStack(10)

    for i in range(1, 6):
        stack.push(i)
    
    stack.dump()

    print("Peek:", stack.peek())

    print("Pop:", stack.pop())
    stack.dump()

    stack.push(6)
    stack.dump()

    print("Find 3:", stack.find(3))
    print("Count 3:", stack.count(3))
    print("Contains 3:", 3 in stack)

if __name__ == "__main__":
    main()