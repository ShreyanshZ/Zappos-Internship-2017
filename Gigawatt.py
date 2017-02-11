# Complete the function below.
def  GigawattPower(batteryOne, batteryTwo, gigawattTarget):
    dictbatteryOne={}
    for i in batteryOne:
        dictbatteryOne[i]=1
    print dictbatteryOne
    for i in batteryTwo:
        if gigawattTarget-i in dictbatteryOne:
            return True
    return False