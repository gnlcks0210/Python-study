# 이터레이터
# - 한 번에 하나씩 값을 꺼낼 수 있는 객체를 의미
# - next() 함수를 통해 다음 값을 꺼내올 수 있음
# - 한 번 꺼내면 다시 꺼낼 수 없음
#   (map,filter도 이터레이터 객체로 반환을 해주는 것)

# 이터러블
# - 반복 가능한 객체를 의미
# - ex) 리스트, 튜플, 문자열 등 for문을 사용하여 거낼 수 있는 객체

numbers = [1, 2, 3]
it = iter(numbers) # 1, 2, 3이라는 값이 모두 들어가있는 이터레이터 객체로 변환
print(next(it)) # 1 출력
print(next(it)) # 2 출력
print(next(it)) # 3 출력
#print(next(it)) # 더이상 꺼낼 값이 없기 때문에 StopIteration 발생

str_list = ["Python", "AI", "BigData"]
it2 = iter(str_list)

for i in it2:
    print(i)

# 제너레이터
# - yield 키워드를 사용하여 값을 하나씩 반환하는 함수
# - 함수 호출 시점이 아니라 next()가 호출될 때 함수 실행
# - 메모리 효율성이 이터레이터에 비해서 좋음
#   (필요할 때만 메모리에 올리고 실행)

def gen():
    print("함수가 실행되었습니다!")# 4. 출력
    yield 10 # 5. 숫자 10을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("A") # 9. 출력
    yield 20 # 10. 숫자 20을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("B")# 14. 출력
    yield 30# 15. 숫자 30을 반환, yield 키워드를 만나면서 함수 대기 상태로 돌입
    print("C") # 19. 출력

result = gen() # 1. 메모리에 함수 올리기 (제너레이터 객체를 저장)
print("첫번째 next실행") # 2. 가장 먼저 실행
print(next(result)) # 3. next()가 호출되면서 함수 실행
#6. 10을 반환 받아서 10 출력 -> print(10)

print("두번째 next실행") # 7. 출력
print(next(result)) # 8. next()가 호출되면서 함수 호출(실행 상태로 돌입)
# 11. 20을 반환 받아서 20 출력 -> print(20)

print("세번째 next실행") # 12. 출력
print(next(result)) # 13. next()가 호출되면서 함수 호출(실행 상태로 돌입)
#16. 30을 반환 받아서 30 출력 -> print(30)

print("네번째 next실행")# 17. 출력
print(next(result))#18. next()가 호출되면서 함수 호출(실행 상태로 돌입)
# 20. 더이상 꺼낼 yield 키워드가 없기 때문에 StopIteration 발생