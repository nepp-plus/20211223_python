# 필요 변수 세팅.
# ex. 두개의 정수 입력
# ex. 최소공배수를 저장해둘 변수.

num1 = int( input('첫 숫자 입력 : ') )
num2 = int( input('두번째 숫자 입력 : ') )

# 최소공배수 (least common multiple)
lcm = num1 # 둘중 하나의 숫자에서 출발. (연산 횟수 줄이기)

# 최대공약수 (greatest common factor)
gcf = 0

# 결과 변수에 올바른 답을 저장하기 위한 로직.
# ex. for / while 등 반복, if / elif / else 조건

# 최소공배수 로직

# 공배수 : 공통된 배수 ->  숫자 % num1 == 0  이고,  숫자 % num2 == 0 동시에 나눠지면 num1의 배수이고, num2의 배수.
# 최소 : 공배수 중 제일 작은 것. => 숫자를 늘려가면서 발견한 최초의 숫자가 제일 작을것임.

# 두 숫자를 곱한 값은 => 무조건 공배수. => 여기까지만 반복을 돌려봐도 공배수는 찾아낼 수 있다.
# 반복 범위가 명확한 반복문. => for로 변경.

# num1 ~ i ~ num1, num2곱한값까지 (포함).
for i in range(num1, num1*num2+1):
    
    # 로직 변경. 들어온 숫자 검사부터.
    if (i % num1 == 0) and (i % num2 == 0):
        # i값이 늘어나다가, 공배수를 발견했다!
        # 최초로 발견한 공배수가, 제일 작을것이다. => 하나만 찾으면 반복 그만해도 됨.
        # 발견한 공배수 (i)값을 lcm에 저장하자.
        lcm = i
        break


# 최대공약수 로직.
# 공약수 : num1 % i == 0 and num2 % i == 0
# 최대 : (num1 or num2) ~ 내려오면서 공약수? 검사. 1까지 내려오면서 검사. (for 반복)


# 결과가 몇인지? 출력
# 상황에 따라 조건/반복 이용 출력.

# lcm에는 발견된 최소공배수가 저장됨.
print(f'최소 공배수 : {lcm}')
