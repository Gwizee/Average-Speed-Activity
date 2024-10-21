s1 = int(input("Enter your frist speed : "))
s2 = int(input("Enter your second speed : "))
s3 = int(input("Enter your third speed : "))

average = (s1 + s2 + s3) / 3
print("The Average speed is ",average)

if s1 < average :
    print("Frist speed is slower than average with the difference of ",average-s1)
if s2 < average :
    print("Second speed is slower than average with the difference of ",average-s2)
if s3 < average :
    print("Third speed is slower than average with the difference of ",average-s3)