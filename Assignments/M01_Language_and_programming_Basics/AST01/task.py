def Ticket_Pricing(n: int):
    
    if n < 5:
        return "Free"
    elif 5 <= n <= 17:
        return 10
    elif 18 <= n <= 64:
        return 20
    else:
        return 15

if __name__ == '__main__':
    try:
        age_input = input().strip()
        if age_input:
            n = int(age_input)
            print(Ticket_Pricing(n))
    except (EOFError, ValueError):
        pass
