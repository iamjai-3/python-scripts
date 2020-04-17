
# SAY -> CONVERT VALUE "ml" to "litres"

from stt_conversion import voice
m = voice()
t = m.lower()
op = t.split()
print(op)

def getConvertfrom():
    return op[2]

def getConvertto():
    return op[4]


if "cubic" in op[2] and len(op) <= 6:
    global fromc,toc
    k = op[2] + op [3]
    fromc = k
    toc = op[5]
    print(k)
    num1 = float(op[1])

elif "cubic" in t and len(op) > 6:    
    k = op[2] + op[3]
    l= op[5] + op[6]
    fromc = k
    toc = l
    print(l)
    num1 = float(op[1])

elif "cubic" in op[4] and len(op) <= 6 :
    
    k = op[4] + op [5]
    fromc = op[2]
    toc = k
    print(k)
    num1 = float(op[1])

else:

    fromc = getConvertfrom()
    toc = getConvertto()
    num1 = float(op[1])

available_units = ('ml', 'litre', 'cubicmetre', 'cubicinch', 'cubicfoot', 'pint', 'quart', 'gallon',  'barrel')
conversions = (1, 1000, 1000000, 16.387064, 28316.846592, 473.176473, 946.352946, 3785.411784, 119240.471196)


index = 0
for i in range (0, len(available_units)):
    if available_units[i] == str(fromc):
        x = num1 * conversions[i]

for j in range (0, len(available_units)):
    if available_units[j] == str(toc):
        num2 = x / conversions[j]

print(num1, fromc, "is equal to", num2, toc)

  