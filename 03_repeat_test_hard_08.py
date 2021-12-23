import random

# 컴퓨터 랜덤 3자리 숫자 출제.

# 3개의 숫자를 추가해주자.
# 랜덤 1~9 + 중복 허용 X. => 로또 당첨번호 생성 로직 참고.

cpu_numbers = random.sample( range(1, 10), 3 )

# 테스트 - 출제된 숫자들이 뭔지 확인.
print(cpu_numbers)