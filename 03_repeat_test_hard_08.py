import random

# 컴퓨터 랜덤 3자리 숫자 출제.

# 3개의 숫자를 추가해주자.
# 랜덤 1~9 + 중복 허용 X. => 로또 당첨번호 생성 로직 참고.

cpu_numbers = random.sample( range(1, 10), 3 )

# 테스트 - 출제된 숫자들이 뭔지 확인.
print(cpu_numbers)

# 정답을 맞출때까지 계속 반복 입력.
while True:
    input_num = int( input('3자리 숫자 입력 : ') )
    
    # 숫자를 3자리로 분해해서 저장해줄 목록 생성.
    # 456 들어오면 => [4, 5, 6] => [100의자리, 10의자리, 1의자리]
    
    user_numbers = [ input_num // 100,  input_num // 10 % 10  , input_num % 10 ]
    
    print(user_numbers)