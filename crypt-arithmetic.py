letter_vars = ['F', 'T', 'U', 'W', 'R', 'O']
carry_vars  = ['C1', 'C2', 'C3']

digit_domain = list(range(10))
carry_domain = [0, 1]


def all_diff(vals):
    return len(vals) == len(set(vals))


def cols_ok(a):
    if all(k in a for k in ['O', 'R', 'C1']):
        if a['O'] + a['O'] != a['R'] + 10 * a['C1']:
            return False

    if all(k in a for k in ['W', 'U', 'C1', 'C2']):
        if a['W'] + a['W'] + a['C1'] != a['U'] + 10 * a['C2']:
            return False

    if all(k in a for k in ['T', 'O', 'C2', 'C3']):
        if a['T'] + a['T'] + a['C2'] != a['O'] + 10 * a['C3']:
            return False

    if 'C3' in a and 'F' in a:
        if a['C3'] != a['F']:
            return False

    if a.get('T') == 0 or a.get('F') == 0:
        return False

    assigned_letters = [a[l] for l in letter_vars if l in a]
    if len(assigned_letters) != len(set(assigned_letters)):
        return False

    return True


search_order = ['O', 'C1', 'R', 'W', 'C2', 'U', 'T', 'C3', 'F']

found = []


def search(idx, assignment):
    if idx == len(search_order):
        if cols_ok(assignment):
            found.append(dict(assignment))
        return

    var = search_order[idx]
    dom = carry_domain if var in carry_vars else digit_domain

    for val in dom:
        assignment[var] = val

        if cols_ok(assignment):
            search(idx + 1, assignment)

        del assignment[var]


print("\n" + "+" + "-" * 27 + "+")
print("|  TWO + TWO = FOUR  (CSP)  |")
print("+" + "-" * 27 + "+\n")

print("Variables : F T U W R O  (digits 0-9)")
print("Carry vars: C1 C2 C3     (digits 0-1)\n")

print("Constraints:")
print("  O + O       = R + 10*C1")
print("  W + W + C1  = U + 10*C2")
print("  T + T + C2  = O + 10*C3")
print("  C3          = F")
print("  Alldiff(F, T, U, W, R, O)")
print("  T != 0, F != 0\n")

print("Searching...\n")

search(0, {})

if not found:
    print("No solutions found")

else:
    print(f"Found {len(found)} solution(s):\n")

    for i, sol in enumerate(found, 1):
        t = sol['T'] * 100 + sol['W'] * 10 + sol['O']
        f = sol['F'] * 1000 + sol['O'] * 100 + sol['U'] * 10 + sol['R']

        print(f"  Solution {i}:  {t} + {t} = {f}  |  ", end="")
        print("  ".join(f"{l}={sol[l]}" for l in ['F', 'T', 'U', 'W', 'R', 'O']), end="")
        print(f"  |  C1={sol['C1']} C2={sol['C2']} C3={sol['C3']}")

    print()

    s = found[0]
    t = s['T'] * 100 + s['W'] * 10 + s['O']
    f = s['F'] * 1000 + s['O'] * 100 + s['U'] * 10 + s['R']

    print("Breakdown for solution 1:\n")

    print(f"    T={s['T']} W={s['W']} O={s['O']}  =>  TWO  = {t}")
    print(f"  + T={s['T']} W={s['W']} O={s['O']}  =>  TWO  = {t}")
    print(f"  {'=' * 18}")
    print(f"  F={s['F']} O={s['O']} U={s['U']} R={s['R']}  => FOUR = {f}")

    print(f"\n  {t} + {t} = {t + t} ({'correct' if t + t == f else 'wrong'})\n")
