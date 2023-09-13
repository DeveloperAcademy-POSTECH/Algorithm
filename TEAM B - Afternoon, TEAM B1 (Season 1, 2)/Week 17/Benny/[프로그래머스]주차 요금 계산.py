def get_minute(time):
    time = time.split(":")
    
    return int(time[0]) * 60 + int(time[1])


def solution(fees, records):
    answer = []
    records = list(map(lambda x: x.split(), records))
    records = sorted(records, key=lambda x: (x[1], x[0]))
    print(records)
    
    cur_number = records[0][1]
    cur_time = get_minute(records[0][0])
    out = False
    
    diffs = {record[1]: 0 for record in records}
    for record in records[1:]:
        time, number, inout = record
        time = get_minute(time)
        
        if number == cur_number:
            if out:
                cur_time = time
                out = False
            else:
                diffs[number] += time - cur_time
                out = True
        
        else:
            if out:
                cur_number = number
                cur_time = time
                out = False
            else:
                diffs[cur_number] += get_minute("23:59") - cur_time
                cur_number = number
                cur_time = time
                out = False

    if out == False:
        diffs[cur_number] += get_minute("23:59") - cur_time
        
    print(diffs)
             
    for n in diffs.keys():
        if diffs[n] <= fees[0]:
            answer.append(fees[1])
        else:
            fee = fees[1]
            exceed_time = diffs[n] - fees[0]
            if exceed_time % fees[2] == 0:
                fee += (exceed_time // fees[2]) * fees[3]
            else:
                fee += (exceed_time // fees[2] + 1) * fees[3]
            answer.append(fee)
        
    return answer