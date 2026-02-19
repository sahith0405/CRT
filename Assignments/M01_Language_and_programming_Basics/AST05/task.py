from typing import List

def Collatz_Sequence(n: int) -> List[int]:
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    sequence.append(1)
    return sequence

if __name__ == '__main__':
    try:
        line = input().strip()
        if line:
            n = int(line)
            # Standard list printing usually works, 
            # but ensure it matches the expected format.
            print(Collatz_Sequence(n))
    except (EOFError, ValueError):
        pass
