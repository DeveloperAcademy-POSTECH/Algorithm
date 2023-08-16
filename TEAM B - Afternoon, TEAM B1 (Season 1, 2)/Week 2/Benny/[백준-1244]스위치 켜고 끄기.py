#백준. 1244. 스위치 켜고 끄기.

def change(switches, student):
    if student[0] == 1:
        quotient = len(switches) // student[1]
        for i in range(1, quotient+1):
            index = student[1] * i - 1
            switches[index] = 0 if switches[index] == 1 else 1
            
    else:
        switches[student[1]-1] = 0 if switches[student[1]-1] == 1 else 1
        i = 1
        while 1 <= student[1] - i and student[1] + i <= len(switches):
            if switches[student[1]-i-1] != switches[student[1]+i-1]:
                break
            switches[student[1]-i-1] = 0 if switches[student[1]-i-1] == 1 else 1
            switches[student[1]+i-1] = 0 if switches[student[1]+i-1] == 1 else 1
            i += 1

n = int(input())
switches = list(map(int, input().split()))
student_count = int(input())
students = []
for _ in range(student_count):
    students.append(list(map(int, input().split())))

for student in students:
    change(switches, student)

print_count = len(switches) // 20 if len(switches) % 20 == 0 else len(switches) // 20 + 1
if print_count == 0:
    print(' '.join(map(str, switches)))
else:
    for i in range(print_count):
        print(' '.join(map(str, switches[20*i:20*(i+1)])))
    print(' '.join(map(str, switches[20*(i+1):])))
    
    