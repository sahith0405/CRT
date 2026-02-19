def Student_Grade_System(name: str, n1: int, n2: int, n3: int) -> str:
    avg = (n1 + n2 + n3) / 3
    if avg >= 40:
        status = "Pass"
    else:
        status = "Fail"
    
    return f"Average grade: {avg:.2f}, Status: {status}"

if __name__ == '__main__':
    try:
        name = input().strip()
        n1, n2, n3 = map(int, input().replace(',', ' ').split())
        print(Student_Grade_System(name, n1, n2, n3))
    except EOFError:
        pass
