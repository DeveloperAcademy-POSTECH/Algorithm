from collections import defaultdict

def time_to_money(fees, minutes):
    if minutes <= fees[0]:
        return fees[1]
    
    if (minutes - fees[0]) % fees[2] == 0:
        return fees[1] + ((minutes - fees[0]) // fees[2]) * fees[3]
    else:
        return fees[1] + ((minutes - fees[0]) // fees[2] + 1) * fees[3]

def solution(fees, records):
    answer = []
    
    charges = defaultdict(int)
    inouts = {}
    
    # fees = [기본 시간, 기본 요금, 추가 시간, 추가 요금]
    
    for rec in records:
        timestamp, number, action = rec.split()
        
        hour, minute = map(int, timestamp.split(':'))
        
        if action == 'IN':
            inouts[number] = hour * 60 + minute
        elif action == 'OUT':
            charged_time = (hour * 60 + minute) - inouts[number]
            del inouts[number]
            charges[number] += charged_time
        
    for number, times in inouts.items():
        charged_time = (23 * 60 + 59) - times
        charges[number] += charged_time
        
    for number in sorted(charges.keys()):
        answer.append(time_to_money(fees, charges[number]))
    
    return answer
