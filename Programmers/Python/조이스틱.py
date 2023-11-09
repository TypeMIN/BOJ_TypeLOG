def solution(name):
    answer = 10000
    
    A_pos = ord('A')
    Z_pos = ord('Z') + 1
    
    positions = [min(abs(ord(i) - A_pos), abs(ord(i) - Z_pos)) for i in name]
    _positions = list(reversed(positions[1:])) + positions
    
    for i in range(len(_positions)):
        direction = i - len(positions) + 1
        stack = []
        count = 0
        
        if direction > 0:
            for j in range(len(positions)):
                if _positions[i - j] == 0:
                    if not stack:
                        continue
                    else:
                        stack.append(_positions[i - j])
                else:
                    if stack[-1] == 0:
                        stack.append(_positions[i - j])
                        count = len(stack)
                    else:
                        stack.append(_positions[i - j])
                        count += 1
            answer = min(answer, sum(stack) + count - 1)
        else:
            for j in range(len(positions)):
                if _positions[i + j] == 0:
                    if not stack:
                        continue
                    else:
                        stack.append(_positions[i + j])
                else:
                    if stack[-1] == 0:
                        stack.append(_positions[i + j])
                        count = len(stack)
                    else:
                        stack.append(_positions[i + j])
                        count += 1
            answer = min(answer, sum(stack) + count - 1)
        
        
        # if direction > 0:
        #     for j in range(len(positions)):
        #         if _positions[i - j] == 0:
        #             if not stack:
        #                 continue
        #             else:
        #                 stack.append(_positions[i - j])
        #         else:
        #             if stack[-1] == 0:
        #                 stack.append(_positions[i - j])
        #                 count = len(stack)
        #             else:
        #                 stack.append(_positions[i - j])
        #                 count += 1
        #     answer = min(answer, sum(stack) + count - 1)         
        # else:
        #     for j in range(len(positions)):
        #         if _positions[i + j] == 0:
        #             if not stack:
        #                 continue
        #             else:
        #                 stack.append(_positions[i + j])
        #         else:
        #             if stack[-1] == 0:
        #                 stack.append(_positions[i + j])
        #                 count = len(stack)
        #             else:
        #                 stack.append(_positions[i + j])
        #                 count += 1
        #     answer = min(answer, sum(stack) + count - 1)      
    return answer