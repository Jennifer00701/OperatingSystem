import psutil
# 프로세스 아이디 조회 가능 (반복자를 통해 접근)
# 08.파이와 동일한 일치하는 프로세스 발견하면 출력하는 것 


for proc in psutil.process_iter(): #현재 실행 중인 모든 프로세스를 조회한다.
    ps_name = proc.name()  # 각 프로세스의 이름을 가져와 변수 ps_name에 저장한다.
    
    if '08.py' in ps_name: # 만약 프로세스이름이 Visual Studio Code이라면 아래 코드 실행한다.
        print(f' 실행 중 프로세스 이름은 : {ps_name}', proc.status()) # 해당 프로세스의 이름을 출력한다.
    
        # if child : 
        #     print(f'{ps_name}의 자식 프로세스', child)


