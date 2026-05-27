#Input: 
#matrix = [[1,1,1],[1,0,1],[1,1,1]]
matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]


#Output: 
#[[1,0,1],[0,0,0],[1,0,1]]

lun=len(matrix)
lun_righ=len(matrix[0])
righe_0=[]
colonne_0=[]

for i in range(lun):
    for j in range(lun_righ):

        if matrix[i][j]==0:
            righe_0.append(j)
            colonne_0.append(i)



for n in colonne_0:
    for x in range(lun_righ):
        matrix[n][x]=0


for m in righe_0:
    for x in range(lun):
        matrix[x][m]=0



print(matrix)
