# sep : 출력 중간에 추가할 문자
# end : 끝에 추가할 문자
print("python", "java", sep=",", end="?")
print("무엇이 더 재밌을까요?")

import sys
print("python", "java", file=sys.stdout)
print("python", "java", file=sys.stderr)

# ljust(8) : 8칸만큼의 공간을 확보후 왼쪽으로 정렬
# rjust(4) : 4칸만큼의 공간을 확보후 오른쪽으로 정렬
scores = {"수학":0, "영어":50, "코딩":100}
for subject, score in scores.items():
    print(subject.ljust(8), str(score).rjust(4), sep=":")

# zfill(3) : 3칸만큼의 공간을 확보후 비는 공간은 0으로 채움(001, 002, 003, ...)
for num in range(1,21):
    print("대기번호 : " + str(num).zfill(3))

# input : 항상 문자열로 값 입력을 받음
answer = input("아무 값이나 입력하세요 : ")
print("입력하신 값은 " + answer + "입니다.")