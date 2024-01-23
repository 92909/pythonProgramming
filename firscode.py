
num1 = 30
num2 = 30
sum = num1 + num2
message1 = str("The numbers are equal")
message2 = str("The numbers are not equal")
if num1 == num2:
     print(message1[:16])
else:
    print(message2[4:-2])

message = "welcome to python 101 : strings"
mess = (message[18] + ' ' + message[:8] + message[26:30] + message[7:10] + " " + message[13] + message[12] + message[2] + message[1] + message[26])
mess1 = mess.title()
mess2 = message[::-1]
print(message.title())
print(mess1)
print(mess2)


vacancies = "kimutai"
vacancy = "very great"
print(f"{vacancies} is very {vacancy}")


your_name = input("Enter your name : ")
distance_covered = int(input("Enter the distance you ran in kilometres : "))
distance_miles = distance_covered * 1.609
print(f"Hello {your_name} !".title())
print(f"You ran {distance_miles} miles")
print("Have a great day".upper())
name = "Kimutai"
if distance_covered <= 20:
    print(f"Hey {name}. You ran {distance_miles} today. You need to work harder!")
else:
    print(f"Great job {your_name} 👊✋. You ran {distance_miles}. Congrats")