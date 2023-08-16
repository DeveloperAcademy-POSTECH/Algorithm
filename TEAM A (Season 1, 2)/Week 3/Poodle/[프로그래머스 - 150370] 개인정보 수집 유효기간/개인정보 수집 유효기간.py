def string_to_days(string):
    years, months, days = map(int, string.split("."))
    
    return ((years - 2000) * 12 * 28) + ((months - 1) * 28) + days

def solution(today, terms, privacies):
    today_days = string_to_days(today)
    
    valid_days = {}
    for line in terms:
        key, value = line.split()
        valid_days[key] = int(value) * 28
    
    answer = []
    
    for idx, line in enumerate(privacies):
        date, term = line.split()
        date = string_to_days(date)
        
        # print(f"{idx + 1}: {today_days - date} <= {valid_days[term]}")
        
        if today_days - date >= valid_days[term]:
            answer.append(idx + 1)

    return answer
