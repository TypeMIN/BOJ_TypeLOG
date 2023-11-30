stack = []
stack_size = 0

N = int(input())

for i in range(N):
    opcode = list(input().split())
    if opcode[0] == "1":
        stack.append(int(opcode[1]))
        stack_size += 1
    elif opcode[0] == "2":
        if stack_size > 0:
            print(stack.pop())
            stack_size -= 1
        else:
            print(-1)
    elif opcode[0] == "3":
        print(stack_size)
    elif opcode[0] == "4":
        if stack_size > 0:
            print(0)
        else:
            print(1)
    elif opcode[0] == "5":
        if stack_size > 0:
            print(stack[stack_size - 1])
        else:
            print(-1)
# time outedc