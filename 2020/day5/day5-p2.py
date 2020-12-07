
with open("input.txt", "r") as f:
    data = f.read().splitlines()

def rowMapToSeatId(rowStr,seatStr):

    rowStrBin = rowStr.replace("F","0").replace("B","1")
    decimalRowNumber = int(rowStrBin,2)

    seatStrBin = seatStr.replace("L","0").replace("R","1")
    decimalSeatNumber = int(seatStrBin,2)

    seatId = (decimalRowNumber*8) + decimalSeatNumber

    return(seatId)

seatIds=[]
for seatMap in data:
    rowStr = seatMap[0:7]
    buttStr = seatMap[7:10]
    seatIds.append(rowMapToSeatId(rowStr,buttStr))

seatIds.sort()
for lookFor in range(seatIds[0],seatIds[-1]):
    if (lookFor not in seatIds):
        print(f"My seat ID is {lookFor}")
