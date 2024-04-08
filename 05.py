from multiprocessing import Process
import os

def func():
    print('이것은 실험용으로 대충 만든 함수입니다.')
    print('프로세스 아이디 : ', os.getpid())
    print('나의 부모 프로세스 아이디 : ', os.getppid())

if __name__ == '__main__':
    print('05.py 프로세스 아이디 :', os.getpid())
    child = Process(target=func).start()