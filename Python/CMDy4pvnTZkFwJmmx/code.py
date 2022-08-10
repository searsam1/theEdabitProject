#
# tests in /tests.py 
class Sudoku:
    def __init__(self,s) -> None:
        self.s = s
        self.sqrs = []
        self.board = [list(
            map(int, self.s[i:i+9])) 
                for i in range(0,81,9)
                    ]
        self.rows = self.board
        self.cols = [
            [self.board[j][i] for j in range(9)] 
                for i in range(9)] 
        
        for j in range(0, 81, 27):
            for start in range(0+j, 9+j, 3):
                sqr = [] 
                for _ in range(3):
                    sqr.append(
                        [self.s[i] for i in range(start, 3+start)]
                                )
                    start += 9
                
                self.sqrs.append([
                    int(i) for i in sum(sqr,[])
                    ])

    def get_col(self,n): return self.cols[n]
        
    def get_row(self,n): return self.rows[n]    

    def get_sqr(self,n,m=None):
        return self.sqrs[(n // 3 * 3) + (m // 3)] if m else self.sqrs(n)
# EOF
g1 = Sudoku("417950030000000700060007000050009106800600000000003400900005000000430000200701580")

print(g1.get_sqr(1,1))


