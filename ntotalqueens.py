def totalNQueens(n: int) -> int:
    visited_cols = set()
    visited_diagonals = set()
    visited_antidiagonals = set()
    ans = 0
    def backtrack(r):
        if r == n:
            nonlocal ans
            ans += 1
            return
        for c in range(n):
            if not (c in visited_cols or (r+c) in visited_diagonals or (r-c) in visited_antidiagonals):
                visited_cols.add(c)
                visited_diagonals.add(r+c)
                visited_antidiagonals.add(r-c)
                backtrack(r+1)
                # undo backtracking
                visited_cols.remove(c)
                visited_diagonals.remove(r+c)
                visited_antidiagonals.remove(r-c)
    backtrack(0)
    return ans

n = 9
print(totalNQueens(n))