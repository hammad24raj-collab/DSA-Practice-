board = [["A","B","C","E"],
         ["S","F","C","S"],
         ["A","D","E","E"]]
         
word = "SEE"

def word_search(board,word,i,j,index):
    if index == len(word):
        return True 
    if i >= len(board) or j >= len(board[0]) or i < 0 or j < 0:
        return False
    if word[index] != board[i][j]:
        return False 
    temp = board[i][j] 
    board[i][j] = "#"
    
    found = (
        word_search(board,word,i-1,j, index+1)
        or
        word_search(board,word,i+1,j, index+1)
        or
        word_search(board,word,i,j-1, index+1)
        or
        word_search(board,word,i,j+1, index+1)
    )
    board[i][j] = temp
    return found 
    
def exist(board, word):
    rows = len(board)
    cols = len(board[0])
    
    for i in range(rows):
        for j in range(cols):
            if word_search(board, word, i, j, 0):
                return True

    return False


print(exist(board, word))