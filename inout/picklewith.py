import pickle

# pickle을 쓰기 위해 wb(write binary) 모드로 실행
profile_file = open("profile.pickle", "wb")
profile = {"이름":"박명수", "나이":30, "취미":["축구", "골프", "코딩"]}
print(profile)
pickle.dump(profile, profile_file) # profile에 저장된 정보를 profile_file에 저장
profile_file.close()

# rb(read binary) 모드로 실행
profile_file = open("profile.pickle", "rb")
profile = pickle.load(profile_file) # profile_file에 저장된 정보를 profile에 저장
print(profile)
profile_file.close()

# with
# 위 내용과 동일, 자동 close
with open("profile.pickle", "rb") as profile_file:
    print(pickle.load(profile_file))

with open("study.txt", "w", encoding="utf8") as study_file:
    study_file.write("파이썬을 열심히 공부하고 있어요.")

with open("study.txt", "r", encoding="utf8") as study_file:
    print(study_file.read())

for i in range(1, 51):
    with open(str(i) + "주차.txt", "w", encoding="utf8") as report_file:
        report_file.write("- {0} 주차 주간보고 -".format(i))
        report_file.write("부서 : ")
        report_file.write("이름 : ")
        report_file.write("업무 요약 : ")