class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visited = [[False] * n for _ in range(m)]

        def dfs(board,i,j,index,word):
            if index==len(word):
                return True
            if (i<0 or j<0 or i>=m or j>=n or visited[i][j]==True or board[i][j]!=word[index]):
                return False
            visited[i][j]=True
            # if we found the char in any of the 4 direction we will return True that why we are using or
            if (dfs(board,i+1,j,index+1,word) or 
                    dfs(board,i-1,j,index+1,word) or
                    dfs(board,i,j+1,index+1,word) or
                    dfs(board,i,j-1,index+1,word) ):
                return True

            # back tracking and making it False again so that we can use it in any another iteration.
            visited[i][j]=False

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0] and dfs(board,i,j,0,word):
                    return True
        return False

                
        
