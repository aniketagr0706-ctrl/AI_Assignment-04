from collections import deque
import copy


rows = 'ABCDEFGHI'
cols = '123456789'


cells = [r + c for r in rows for c in cols]


row_units = [[r + c for c in cols] for r in rows]
col_units = [[r + c for r in rows] for c in cols]
box_units = [
    [r + c for r in rb for c in cb]
    for rb in ['ABC', 'DEF', 'GHI']
    for cb in ['123', '456', '789']
]

all_units = row_units + col_units + box_units


cell_units = {
    cell: [u for u in all_units if cell in u]
    for cell in cells
}


cell_peers = {
    cell: set(c for u in cell_units[cell] for c in u if c != cell)
    for cell in cells
}


fig_6_4a = [
    [0, 0, 3, 0, 2, 0, 6, 0, 0],
    [9, 0, 0, 3, 0, 5, 0, 0, 1],
    [0, 0, 1, 8, 0, 6, 4, 0, 0],

    [0, 0, 8, 1, 0, 2, 9, 0, 0],
    [7, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 0, 6, 7, 0, 8, 2, 0, 0],

    [0, 0, 2, 6, 0, 9, 5, 0, 0],
    [8, 0, 0, 2, 0, 3, 0, 0, 9],
    [0, 0, 5, 0, 1, 0, 3, 0, 0],
]


def grid_to_domains(grid):
    flat = [grid[r][c] for r in range(9) for c in range(9)]

    doms = {}
    for i, cell in enumerate(cells):
        if flat[i] != 0:
            doms[cell] = [flat[i]]
        else:
            doms[cell] = list(range(1, 10))

    return doms


def ac3(doms):
    q = deque(
        (xi, xj)
        for u in all_units
        for xi in u
        for xj in u
        if xi != xj
    )

    while q:
        xi, xj = q.popleft()
        changed = False

        for v in doms[xi][:]:
            if not any(v != v2 for v2 in doms[xj]):
                doms[xi].remove(v)
                changed = True

        if changed:
            if not doms[xi]:
                return False

            for xk in cell_peers[xi]:
                if xk != xj:
                    q.append((xk, xi))

    return True


def pick_cell(doms, assigned):
    free = [c for c in cells if c not in assigned]
    return min(free, key=lambda c: len(doms[c]))


def bt(assigned, doms):
    if len(assigned) == 81:
        return assigned

    cell = pick_cell(doms, assigned)

    for val in doms[cell][:]:
        if any(assigned.get(p) == val for p in cell_peers[cell]):
            continue

        assigned[cell] = val

        removed = {}
        ok = True

        for p in cell_peers[cell]:
            if p not in assigned and val in doms[p]:
                doms[p].remove(val)
                removed[p] = val

                if not doms[p]:
                    ok = False
                    break

        if ok:
            res = bt(assigned, doms)
            if res:
                return res

        del assigned[cell]

        for p, v in removed.items():
            doms[p].append(v)

    return None


def print_grid(source):
    print()

    for ri, r in enumerate(rows):
        line = "  "

        for ci, c in enumerate(cols):
            key = r + c

            if isinstance(source, dict):
                vals = source[key]
                if isinstance(vals, int):
                    ch = str(vals)
                elif len(vals) == 1:
                    ch = str(vals[0])
                else:
                    ch = "."
            else:
                ch = str(source[key]) if source[key] != 0 else "."

            line += ch + " "

            if ci in [2, 5]:
                line += "| "

        print(line)

        if ri in [2, 5]:
            print("  -------+-------+-------")

    print()


def run(grid):
    print("Input puzzle:")

    print_grid({
        cells[i]: grid[i // 9][i % 9]
        for i in range(81)
    })

    doms = grid_to_domains(grid)

    print("Applying AC-3...")

    if not ac3(doms):
        print("Contradiction found during AC-3, no solution exists\n")
        return

    if all(len(doms[c]) == 1 for c in cells):
        print("AC-3 fully solved the puzzle\n")

        sol = {c: doms[c][0] for c in cells}

        print("Solution:")
        print_grid(sol)
        return

    print("AC-3 reduced domains, running backtracking...\n")

    pre_assigned = {
        c: doms[c][0]
        for c in cells
        if len(doms[c]) == 1
    }

    sol = bt(pre_assigned, doms)

    if sol:
        print("Solution found:")
        print_grid(sol)
    else:
        print("No solution found for this puzzle\n")


print("=" * 40)
print("  Sudoku CSP Solver (Reference: Russel and Norvig 6.2.6)")
print("=" * 40)

print("\nSolving the textbook puzzle from Figure 6.4(a):\n")
run(fig_6_4a)


ans = input("Would you like to enter your own puzzle? (y/n): ").strip().lower()

if ans == 'y':
    print("\nEnter the puzzle row by row (9 digits, 0 for empty):")

    custom = []

    for r in rows:
        while True:
            row = input(f"Row {r}: ").strip()

            if len(row) == 9 and all(ch.isdigit() for ch in row):
                custom.append([int(x) for x in row])
                break

            print("Please enter exactly 9 digits")

    print()
    run(custom)
