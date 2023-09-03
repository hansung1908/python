def profile(name, age, main_lang):
    print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석", 20, "파이썬")
profile("김태호", 25, "자바")

# 같은 학교, 학년, 반, 수업
def profile(name, age=17, main_lang="파이썬"):
    print("이름 : {0}\t나이: {1}\t주 사용 언어 : {2}".format(name, age, main_lang))

profile("유재석")
profile("김태호")

# 키워드값

def profile(name, age, main_lang):
    print(name, age, main_lang)

profile(name="유재석", main_lang="파이썬", age=20)
profile(main_lang="자바", age=25, name="김태호")

# 가변인자

def profile(name, age, lang1, lang2, lang3, lang4, lang5):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    print(lang1, lang2, lang3, lang4, lang5)

profile("유재석", 20, "python", "java", "c", "c#", "c++")
profile("김태호", 25, "kotlin", "swift", "", "", "")

def profile(name, age, *lang):
    print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
    for l in lang:
        print(l, end=" ")
    print()

profile("유재석", 20, "python", "java", "c", "c#", "c++", "javascript")
profile("김태호", 25, "kotlin", "swift")

# 지역변수와 전역변수

gun = 10

def checkpoint(soldiers): # 경계근무
    gun = 20
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총 : {0}".format(gun))

def checkpoint(soldiers): # 경계근무
    global gun # 전역 공간에 있는 gun 사용
    gun = gun - soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))

print("전체 총 : {0}".format(gun))
checkpoint(2) # 2명이 경계 근무를 나감
print("남은 총 : {0}".format(gun))

def checkpoint_return(gun, soldiers):
    gun = gun + soldiers
    print("[함수 내] 남은 총 : {0}".format(gun))
    return gun

print("전체 총 : {0}".format(gun))
gun = checkpoint_return(gun, 2)
print("남은 총 : {0}".format(gun))

def std_weight(height, gender): # 키 m 단위 (실수), 성별 " 남자" / "여자"
    if gender == "남자":
        return height * height * 22
    else:
        return height * height * 21
    
height = 175 # cm 단위
gender = "남자"
weight = round(std_weight(height / 100, gender), 2)

print("키 {0}cm {1}의 표준 체중은 {2}kg입니다.".format(height, gender, weight))