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
    
    # s와 b의 갯수를 구하자.
    strike_count = 0
    ball_count = 0
    
    # 내 숫자들과 문제 숫자들을 비교해서, S/B갯수 구하기.
    # 목록을 보는데, index가 몇인지도 파악하면서 확인해야 위치가 같은지 다른지 판단 가능.
    # Bubble Sort 코드 참고.
    
    
    
    
    # 구해진 S/B 갯수 출력.
    print(f'{strike_count}S {ball_count}B 입니다.')
    
    
    