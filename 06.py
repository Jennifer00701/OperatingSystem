from multiprocessing import Process
import os
import time

def func():
    print('이것은 실험용으로 대충 만든 함수입니다.')
    print('프로세스 아이디 : ', os.getpid())
    print('나의 부모 프로세스 아이디 : ', os.getppid())

if __name__ == '__main__':
    print('06.py 프로세스 아이디 :', os.getpid())
    child1 = Process(target=func)
    child1.start()
    time.sleep(1)
    child2 = Process(target=func)
    child2.start()
    time.sleep(1)
    child = Process(target=func)
    child.start()
    time.sleep(1)
