#Input: 
columnNumber = 701

#Output: "ZY"

output=''

lettere = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


test=columnNumber//26
resto=columnNumber-test*26

output+= lettere[test-1]+ lettere[resto-1]


print(output)