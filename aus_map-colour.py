from collections import deque

neighbors = {
    "WA":  ["NT", "SA"],
    "NT":  ["WA", "Q", "SA"],
    "Q":   ["NT", "NSW", "SA"],
    "NSW": ["Q", "V", "SA"],
    "V":   ["NSW", "SA"],
    "SA":  ["WA", "NT", "Q", "NSW", "V"],
    "T":   []
}

color_options = ["Red", "Green", "Blue"]


def get_domain():
    return {region: color_options[:] for region in neighbors}


def ac_3(domain_map):
    arcs = deque()

    for x in neighbors:
        for y in neighbors[x]:
            arcs.append((x, y))

    while arcs:
        x, y = arcs.popleft()
        removed = False

        for c in domain_map[x][:]:
            if all(c == c2 for c2 in domain_map[y]):
                domain_map[x].remove(c)
                removed = True

        if removed:
            if len(domain_map[x]) == 0:
                return False

            for z in neighbors[x]:
                if z != y:
                    arcs.append((z, x))

    return True


def is_valid(region, color, coloring):
    for nb in neighbors[region]:
        if coloring.get(nb) == color:
            return False
    return True


def solve_csp(domain_map, coloring={}):
    coloring = dict(coloring)

    uncoloRed = [r for r in neighbors if r not in coloring]

    if not uncoloRed:
        return coloring

    next_r = min(uncoloRed, key=lambda r: len(domain_map[r]))

    for c in domain_map[next_r]:
        if is_valid(next_r, c, coloring):
            coloring[next_r] = c

            removed = {}
            ok = True

            for nb in neighbors[next_r]:
                if nb not in coloring and c in domain_map[nb]:
                    domain_map[nb].remove(c)
                    removed[nb] = c

                    if len(domain_map[nb]) == 0:
                        ok = False
                        break

            if ok:
                result = solve_csp(domain_map, coloring)
                if result:
                    return result

            for nb, col in removed.items():
                domain_map[nb].append(col)

            coloring.pop(next_r)

    return None


print("=" * 45)
print("  CSP Map Coloring - Australia")
print("=" * 45)

print(f"\nRegions: {', '.join(neighbors.keys())}")
print(f"Colors available: {', '.join(color_options)}\n")

dm = get_domain()

print("Step 1: Enforcing arc consistency (AC-3)...")
feasible = ac_3(dm)

if not feasible:
    print("AC-3: Problem is unsatisfiable with 3 colors")
else:
    print("AC-3: Domains Reduced successfully")

    print("\nStep 2: Backtracking search with MRV + forward checking...")
    answer = solve_csp(dm)

    if not answer:
        print("No valid coloring found!")
    else:
        print("\nValid coloring found!\n")
        print("-" * 25)

        for region, color in answer.items():
            print(f"  {region:5} --> {color}")

        print("-" * 25)

        print("\nVerification (checking no adjacent regions share a color):")

        all_ok = True

        for r in neighbors:
            for nb in neighbors[r]:
                if answer[r] == answer[nb]:
                    print(f"  CONFLICT: {r} and {nb} both have {answer[r]}")
                    all_ok = False

        if all_ok:
            print("All constraints satisfied!")

        print()
