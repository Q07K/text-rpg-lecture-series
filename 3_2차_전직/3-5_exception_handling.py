try:
    data = input("입력해주세요: ")
    num = int(data)
    print(num)
except:
    print("error")
else:
    print("no error")
finally:
    print("finally")
