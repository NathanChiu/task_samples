import sys;

def main():
    value = sys.stdin.readline().rstrip('\n')
    decimalPlaces = sys.stdin.readline().rstrip('\n')
    addDecimalForSingleDigit = True if (sys.stdin.readline().rstrip('\n')=="1") else False

    output = graduatedValue(value, decimalPlaces, addDecimalForSingleDigit);
    sys.stdout.write(output)

def getGrad(value):
    thresholds = [1E15, 1E12, 1E9, 1E6, 1E3]
    threshold_chars = ['Q', 'T', 'B', 'M', 'K']
#    thresholds = {}
#    thresholds[1E15] = 'Q'
#    thresholds[1E12] = 'T'
#    thresholds[1E9] = 'B'
#    thresholds[1E6] = 'M'
#    thresholds[1E3] = 'K'
#    ts = list()
#    for t in thresholds.keys():
#        ts.append(t)
    for t in thresholds:
        if value >= t:
            return t, threshold_chars[thresholds.index(t)]

def graduatedValue(value, decimalPlaces, addDecimalForSingleDigit):
    #turn the value from string to int
    value = int(value)
    #get the graduation number and character
    grad_num, grad_char = getGrad(value)
    value = value / grad_num
    #value now is in the form wanted. Check the number of decimals.
    if bool(addDecimalForSingleDigit) and int(decimalPlaces) == 0:
        #only affects things if single digit result.
        #add 1 decimal place.
        temp_fmt = "{:.1f}".format(value)
    else:
        temp_fmt = "{:.%df}" % int(decimalPlaces)

    return temp_fmt.format(value) + grad_char

main()

Failed for Zero: Failed with [exception] rather than [0]
Failed for Decimal Zeros: Failed with [exception] rather than [0.0000]
Failed for Zero AddDec: Failed with [exception] rather than [0.0]
