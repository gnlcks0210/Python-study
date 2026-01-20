# property를 사용해보는 것
# getter, setter를 사용해서 비공개 변수를 가져오고 수정해보기
#Person으로 class를 선언할꺼다.
class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    # 이 아래가 중요
    # 1. property에서 getter를 선언하는 방법
    # getter : 접근할 수 없는 변수를 가져오게 해주는 것
