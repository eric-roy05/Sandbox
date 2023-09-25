password = input("Password (More that 7 characters): ")
min_password_length = 7
while len(password) < min_password_length:
    print("Invalid input")
    password = input("Password (More that 7 characters): ")
print(len(password) * '*')
