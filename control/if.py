weather = input("오늘 날씨는 어때요? ")

if weather == "비" or weather == "눈":
    print("우산을 챙기세요.")
elif weather == "미세먼지":
    print("마스크를 챙기세요.")
else:
    print("준비물 필요 없어요.")

temp = int(input("기온은 어때요?"))

if 30 <= temp:
    print("너무 더워요. 나가지 마세요.")
elif 0 <= temp and temp < 30:
    print("괜찮은 날씨에요.")
elif 0 <= temp < 10:
    print("외투를 챙기세요.")
else:
    print("너무 추워요. 나가지 마세요.")

from random import *

cnt = 0 # 총 탑승 승객 수

for i in range(1, 51): # 1 ~ 50 이라는 수 (승객)
    time = randrange(5, 51) # 5분 ~ 50분 소요 시간
    if 5 <= time <= 15: # 5분 ~ 15분 이내의 손님 (매칭 성공), 탑승 수 증가 처리
        print("[0] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else: # 매칭 실패한 경우
         print("[x] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}명".format(cnt))