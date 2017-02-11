
def dfs(numRows,numCols,row,col,venue):
	venue[row][col] = 0
	if (row-1 >= 0):
		if venue[row-1][col] == 1:
			venue = dfs(numRows,numCols,row-1,col,venue)
	if(row-1>=0 and col-1>=0):
		if venue[row-1][col-1] == 1:
			venue = dfs(numRows,numCols,row-1,col-1,venue)
	if(row+1 < numRows):
		if venue[row+1][col] == 1:
			venue = dfs(numRows,numCols,row+1,col,venue)
	if (row+1 < numRows and col+1 < numCols):
		if venue[row+1][col+1] == 1:
			venue = dfs(numRows,numCols,row+1,col+1,venue)
	if (col-1 >= 0):
		if venue[row][col-1] == 1:
			venue = dfs(numRows,numCols,row,col-1,venue)
	if (row+1 < numRows and col-1 >= 0):
		if venue[row+1][col-1] == 1:
			venue = dfs(numRows,numCols,row+1,col-1,venue)
	if (col+1 < numCols):
		if venue[row][col+1] == 1:
			venue = dfs(numRows,numCols,row,col+1,venue)
	if (row-1 >= 0 and col+1 <numCols):
		if venue[row-1][col+1] == 1:
			venue = dfs(numRows,numCols,row-1,col+1,venue)
	return venue

def numberOfGroups(venue):
	numRows = len(venue)
	numCols = len(venue[0])
	count = 0
	for row in range(numRows):
		for col in range(numCols):
			if venue[row][col] == 1:
				venue = dfs(numRows,numCols,row,col,venue)
				count += 1
	return count