def is_safe(board, row, col, N):
    # Check if it is safe to place a queen at board[row][col]

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True


def solve_n_queens_util(board, col, N, solutions):
    # Base case: If all queens are placed, add the solution to the list
    if col == N:
        solution = []
        for i in range(N):
            row_solution = ''.join('Q' if board[i][j] == 1 else '.' for j in range(N))
            solution.append(row_solution)
        solutions.append(solution)
        return

    # Consider this column and try placing the queen in all rows one by one
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            solve_n_queens_util(board, col + 1, N, solutions)
            board[i][col] = 0


def solve_n_queens(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions


# Example usage for N = 4
N = 4
solutions = solve_n_queens(N)

for idx, solution in enumerate(solutions):
    print(f"Solution {idx + 1}:")
    for row in solution:
        print(row)
    print()
