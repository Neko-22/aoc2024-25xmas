text_file = open("test.txt", "r")
doc = text_file.read().split("\n")

polarity = 0
problem = 0
safe_lines = 0
is_safe = True

def check_safe(jump, polarity):
    if jump > polarity & polarity == -1:
        raise Exception("Bad polarity")
    elif jump < polarity & polarity == 1:
        raise Exception("Bad polarity")
    elif abs(jump) <= 3 & abs(jump) >= 1:
        print(f"{jump} is ok!")
        return True
    else:
        raise ValueError("Number error!")

for i in range(len(doc)):
    print("")
    polarity = 0
    problem = 0
    line = doc[i].split()
    for i in range(len(line)):
        num1 = int(line[i])
        # this try-catch is to account for end of line out of range errors
        try:
            int(line[i + 1])
        except:
            print("end of line")
            safe_lines += 1
            break
        else:
            num2 = int(line[i + 1])
        jump = num1 - num2
        print(f"{jump}, {num1} - {num2}")
        # set the polarity
        if polarity == 0:
            if jump > 0:
                polarity = 1
                print("polarity is positive")
            else:
                polarity = -1
                print("polarity is negative")
        try:
            check_safe(jump, polarity)
        except:
            print("PROBLEM!! RUNNING CHECKS:")
            for i in range(len(line)):
                line2 = line.copy()
                del line2[i]
                num1 = int(line[i])
                # this try-catch is to account for end of line out of range errors
                try:
                    int(line[i + 1])
                except:
                    print("end of line")
                    safe_lines += 1
                    break
                else:
                    num2 = int(line[i + 1])
                jump = num1 - num2
                print(f"{jump}, {num1} - {num2}")
                # set the polarity
                if polarity == 0:
                    if jump > 0:
                        polarity = 1
                        print("polarity is positive")
                    else:
                        polarity = -1
                        print("polarity is negative")
                try:
                    check_safe(jump, polarity)
                except:
                    pass
                else:
                    break
        else:
            pass
print(safe_lines)