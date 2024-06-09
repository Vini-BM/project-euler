import numpy as np

# Read data
grid = np.loadtxt('euler011_file.txt') # data
tgrid = np.transpose(grid) # transposed matrix

x, y = np.shape(grid) # dimensions (20x20)
maxlist = [] # list for values

# Loop on data
for i in range(x-4): # row
    for j in range(y-4): # columns 
        horiz = np.prod(grid[i][j:j+4]) # horizontal product of 4 terms
        vert = np.prod(tgrid[i][j:j+4]) # vertical product (uses transposed data)
        diag = np.prod([grid[i][j],grid[i+1][j+1],grid[i+2][j+2],grid[i+3][j+3]]) # diagonal product
        secdiag = np.prod([grid[i][-j],grid[i+1][-j-1],grid[i+2][-j-2],grid[i+3][-j-3]]) # secondary diagonal product
        maxlist.append(max(horiz,vert,diag,secdiag)) # append biggest value for this i, j
print(max(maxlist)) # print max value
