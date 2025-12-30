# Q1. sum_to_n()
# - 사용자로부터 숫자 1개(n)를 입력받습니다.
# - 1부터 사용자가 입력한 숫자 n까지의 합을 출력
# ex) 사용자가 10 입력하면 1+2+3+4+5+6+7+8+9+10

def sum_to_n():
    n = int(input("숫자1개를 입력해 주세요 : "))
    sum = 0
    for i in range(1, n + 1):
        sum += i
    print(sum)
sum_to_n()

# Q2. print_diff()
# - 매개변수로 숫자 2개를 전달받아 두 수의 차이를 출력하세요.
# - 조건 : 큰 수 - 작은수로 계산되어야 한다.
# - 첫번째 매개변수에 큰 수가 올수도, 두번재 매개변수에 큰 수가 올수도 있습니다.
def print_diff(num1, num2):
    if num1 > num2:
        print(num1 - num2)
    else:
        print(num2 - num1)
print_diff(1, 2)

# Q3. avg_of_three()
# - 매개변수 3개를 전달 받습니다.
# - 평균을 구한 후 반환하세요.
# - 반환 받은 값을 avg 변수에 저장 후 출력하세요.

def avg_of_three(num1,num2,num3):
    return (num1 + num2 + num3) // 3

avg = avg_of_three(1, 2, 3)
print(avg)

# Q4. is_even()
# - 리스트를 매개변수로 받아서 짝수의 개수만 반환
numbers = [1,2,3,4,5,6,7,11,15]
def is_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count
event_count = is_even(numbers)
print(event_count)