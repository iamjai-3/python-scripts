# SAY -> CONVERT VALUE "kilomts" to "mtrs"

from stt_conversion import voice
t = voice()
op = t.split()
print (op)
def getConvertfrom():
    return op[2]

def getConvertto():
    return op[4]


num1 = float(op[1])

available_units = ('millimetre', 'centimetre', 'metre', 'kilometre', 'inches', 'feet', 'yards', 'miles')
conversions = (1, 10, 1000, 1e6, 25.4, 304.8, 914.4, 1.609344E6)

fromc = getConvertfrom()
toc = getConvertto()

index = 0
for i in range (0, len(available_units)):
    # print (available_units[i], '==', str(fromc))
    if available_units[i] == str(fromc):
        num_in_mm = num1 * conversions[i]

for j in range (0, len(available_units)):
    if available_units[j] == str(toc):
        num2 = num_in_mm / conversions[j]

print(num1, fromc, "is equal to", num2, toc)