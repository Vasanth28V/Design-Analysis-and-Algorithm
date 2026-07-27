def can_place(positions, current_row, current_col):
    for r in range(current_row):
        c = positions[r]

        # Check same column
        if c == current_col:
            return False

        # Check diagonals
        if abs(current_row - r) == abs(current_col - c):
            return False

    return True


def n_queens(n):
    positions = [-1] * n
    solutions = []
    backtrack_count = 0

    def solve(row):
        nonlocal backtrack_count

        if row == n:
            solutions.append(positions[:])
            return

        for col in range(n):
            if can_place(positions, row, col):
                positions[row] = col
                solve(row + 1)

                # Backtrack
                positions[row] = -1
                backtrack_count += 1

    solve(0)
    return solutions, backtrack_count


def print_board(solution, n):
    border = " +" + "---+" * n

    print(border)
    for row in range(n):
        print(" |", end="")
        for col in range(n):
            if solution[row] == col:
                print(" Q |", end="")
            else:
                print(" . |", end="")
        print()
        print(border)


# Main Program
for size in [4, 6, 8]:
    solutions, backtracks = n_queens(size)

    print(f"N={size}: {len(solutions)} solutions, {backtracks} backtracks")

    if size == 4:
        print(f"\nAll solutions for {size}-Queens:")
        for i, solution in enumerate(solutions, start=1):
            print(f"\nSolution {i}: {solution}")
            print_board(solution, size)