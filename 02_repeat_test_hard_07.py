# 6개의 숫자 입력받기.

# 6개의 숫자가 담길 list
my_num_list = []

# for로 6회 반복.
for i  in range(6):
    
    # 제대로 된 숫자가 올때까지, 해당 위치의 숫자를 다시 입력받아야함.
    # 무한 반복 => 제대로 된 숫자면 break
    
    while True:
        input_num =  int( input(f'{i+1}번째 숫자 입력 : ') )
        
        # 받은 숫자가 목록에 추가해도 되는 숫자인가? 검사. => 통과시에만 추가하자.
        
        # 기준 1. 1~45 이내의 숫자가 맞는가?
        is_range_ok = (1 <= input_num) and (input_num <= 45)
        
        # 기준 2. 중복이 아닌가?
        # 기준 2. 이미 등록된 숫자인가? 중복이 아니어야 목록에 추가.
        # my_num_list 내부의 숫자들을 하나씩 꺼내보자. => input_num과 같은 숫자 발견하면? 중복검사 탈락.
        
        is_duplicated = False # 중복되지 않았다고 전제하자.
        
        for  my_num  in  my_num_list:
            if input_num == my_num:
                # 같은 숫자 발견 : 중복이다.
                is_duplicated = True
        
        # 범위 ok 이고, 중복은 아니어야 목록에 추가.
        
        if is_range_ok and not is_duplicated:
            # 입력받은 숫자를 목록에 추가.
            my_num_list.append( input_num )
            # 무한반복 종료 => 다음 숫자 받으러 이동.
            break
                
    
# test - 목록에 뭐가 들어있는지 출력.
print(my_num_list)