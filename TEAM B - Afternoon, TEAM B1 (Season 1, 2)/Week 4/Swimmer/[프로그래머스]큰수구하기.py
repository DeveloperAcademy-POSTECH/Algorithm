num, m = map(int, input().split())
# 입력이 공백 없이 들어오는 숫자를 배열에 할당하는 방법
array = list(map(int, str(num))) #문자열(= 배열 개념)의 char 하나 하나를 int 값으로 형변환 해서 list에 넣는다.

# 빈 배열 stack 선언
stack = list()
for n in array :
    # list가 비어있지 않을 경우 true 리턴
    while stack and m>0  and stack[-1] < n : # stack에서 pop이 이루어지는 조건 : stack이 비어있지 않고, m이 0보다 크고, stack의 기존 끝 원소의 값이 n보다 작을 경우.
        stack.pop()
        m -= 1 # pop() 된 횟수 만큼 m의 count를 직접 줄여준다.   
    # 가능한 만큼 전부 pop()이 이루어진 뒤에 stack에 n을 append를 진행한다.
    stack.append(n)

# 만약 위의 과정을 거쳤음에도 m의 값이 남아있다면? (m!=0) => 남은 m의 수 만큼 stack의 뒷부분을 slicing 해준다.

if m!=0 :
    stack = stack[:-m]

# 배열에 있는 요소들을 '공백 없이' 출력하기
# join 함수 사용 => '구분자'.join(리스트) 형식 
#  -> 매개변수로 들어온 리스트에 있는 요소 하나하나를 합쳐서 하나의 문자열로 바꾸어 반환하는 함수.
# '구분자'.join(리스트)를 이용하면 리스트의 값과 값 사이에 '구분자'에 들어온 구분자를 넣어서 하나의 문자열로 합쳐준다.
result = ''.join(map(str, stack)) 
print(result)
