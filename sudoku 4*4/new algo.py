def safe(nn,row,col,num):
    for i in range(0,len(nn)):
        if nn[i][col]== num:
            return False
        if nn[row][i]== num:
            return False
    sr = (row // 2) * 2  #finding row
    sc = (col // 2) * 2  #finding col
    for i in range (sr,sr+2):
        for j in range (sc,sc+2):
            if nn[i][j] == num:
                return False
    return True

def sudo(nn,row,col):
    if row == len(nn):
        return True
    nrow = 0
    ncol = 0
    if col != len(nn)-1:
        nrow = row 
        ncol = col + 1        
    else:
        nrow = row + 1
        ncol = ncol
    if nn[row][col] != 0 :
        if sudo(nn,nrow,ncol):
            return True
    else :
        for i in range(1,len(nn)+1):
            if safe(nn,row,col,i):
                nn[row][col] = i
                if sudo(nn,nrow,ncol):
                    return True
                else:
                    nn[row][col]=0
    return False

while True:
    if sudo(sud,0,0):
        print(sud)
        break
    else:
        print('no output')
        break
