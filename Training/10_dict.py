# Q1. 빈 딕셔너리 생성(person) 후 아래의 정보를 추가하세요
# - name : Alice
# - age : 25
# -city : Seoul
# - 다 만들면 "age" 값을 1 증가시키고 전체 딕셔너리를 출력하세요.

person = {}
person["name"]  = "Alice"
person["age"] = 25
person["city"] = "Seoul"
person["age"] += 1
print(person)


#Q2. 과목 점수가 담긴 딕셔너리를 생성하세요.
# - scores = {"kor" : 85, "eng" : 90, "math": 70}
# - 평균 점수 계산 후 출력
# - 80점 미만 과목의 이름과 점수 출력
scores = {"kor" : 85, "eng" : 90, "math" : 70}
total = 0
for key,value in scores.items():
    total += value
    if value < 80:
        print(f"{key} : {value}")
print(f"평균 : {total//len(scores.keys())}")
#2번 문제 빠르게 풀면
# - 사용자로부터 국어, 영어, 수학 성적을 직접 입력받아 딕셔너리에 추가
# - 가장 높은 점수를 받은 과목과 가장 낮은 점수를 받은 과목 출력

for key in scores.keys():
    scores[key] = int(input("점수를 입력하세요 : "))

values = scores.values()
sort_values = sorted(values,reverse = True)
print(f"가장 높은 점수 : {sort_values[0]}")
print(f"가장 낮은 점수 : {sort_values[len(sort_values)-1]}")