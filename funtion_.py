# 함수(function)
# 함수란 어떤 기능을 하는 것으로 크게 이미 있는 함수와 직접 만든 함수가 있다.

# def function_name(parameter):
#       codes...
#       return value[variable]

# 위 형식으로 함수를 직접 만들 수 있으며 만든 함수 실행의 경우 아래와 같음
# funcation_name(argument)

# parameter : 함수 내부에서 사용하는 변수
# return    : 함수를 종료하며, 특정 값을 함수를 실행한 곳으로 돌려줄 수 있음
# argument  : 함수를 실행할 때 넘겨주는 값
# parameter, return, argument는 필수가 아님
# 함수를 정의할 때 parameter의 개수와 함수를 실행할 때의 argument의 개수는 같아야 함

def a():                # parameter, return이 없는 경우
    print("Hello")

def b(name):            # return이 없는 경우
    print(name,"Hi")

def c(a):
    return a+10

a()
b("Jeong")
var = c(5)              # 보통  return이 있는 함수의 경우 변수랑 같이 사용
print(var)
b(var)