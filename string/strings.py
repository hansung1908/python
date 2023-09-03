sentence = '나는 소년입니다'
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

url = "http://naver.com"
tmp = url.replace("http://", "")
tmp = tmp[:tmp.index(".")]
password = tmp[:3] + str(len(tmp)) + str(tmp.count("e")) + "!"
print(password)