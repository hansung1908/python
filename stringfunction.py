python = "Python is Amazing"

print(python.lower())
print(python.upper())
print(python[0].isupper())
print(len(python))
print(python.replace("Python", "Java"))

index = python.index("n")
print(index)
index = python.index("n", index + 1)
print(index)

print(python.find("n"))
print(python.find("Java")) # 값이 없는 경우 -1, index는 에러

print(python.count("n"))