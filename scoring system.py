score = int(input("Enter your test score out of 100 "))
if score >= 0 and score <= 39:
    print("FAIL")
if score >= 40 and score < 60:
    print("PASS")
if score >= 60 and score < 80 :
    print("MERIT")
if score >= 80 and score < 100:
    print("DISTINCTION")
else:
    print("You are stupid")
