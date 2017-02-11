# Complete the function below.

def  reverseButPreserveWhitespace(reverseMe):
    s = ""
    flag = 0
    word = ""
    for i in range(len(reverseMe)):
        if(reverseMe[i] == " " and flag == 0):
            s += " "
        elif (reverseMe[i] == " " and flag == 1):
            flag = 0
            s += word[: : -1] + " "
            word = ""
        else:
            flag = 1
            word += reverseMe[i]
    s += word[: : -1]
    return s
