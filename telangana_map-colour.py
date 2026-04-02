from collections import deque
import sys


district_map = [
    ("Adilabad", ["Kumurambheem Asifabad", "Nirmal", "Mancherial"]),
    ("Kumurambheem Asifabad", ["Adilabad", "Mancherial"]),
    ("Mancherial", ["Adilabad", "Kumurambheem Asifabad", "Nirmal", "Jagtial", "Peddapalli"]),
    ("Nirmal", ["Adilabad", "Mancherial", "Nizamabad", "Kamareddy"]),
    ("Nizamabad", ["Nirmal", "Kamareddy", "Sangareddy", "Jagtial", "Rajanna Sircilla"]),
    ("Kamareddy", ["Nirmal", "Nizamabad", "Medak", "Sangareddy"]),
    ("Jagtial", ["Mancherial", "Nizamabad", "Rajanna Sircilla", "Karimnagar", "Peddapalli"]),
    ("Rajanna Sircilla", ["Jagtial", "Nizamabad", "Karimnagar", "Siddipet"]),
    ("Karimnagar", ["Jagtial", "Peddapalli", "Rajanna Sircilla", "Siddipet",
                    "Jayashankar Bhupalapalli", "Jangaon", "Hanamkonda"]),
    ("Peddapalli", ["Mancherial", "Jagtial", "Karimnagar", "Jayashankar Bhupalapalli"]),
    ("Jayashankar Bhupalapalli", ["Peddapalli", "Karimnagar", "Mulugu", "Jangaon", "Mahabubabad"]),
    ("Mulugu", ["Jayashankar Bhupalapalli", "Bhadradri Kothagudem", "Warangal", "Mahabubabad"]),
    ("Sangareddy", ["Kamareddy", "Nizamabad", "Medak", "Siddipet", "Rangareddy"]),
    ("Medak", ["Kamareddy", "Sangareddy", "Siddipet", "Medchal Malkajgiri"]),
    ("Siddipet", ["Rajanna Sircilla", "Karimnagar", "Medak", "Sangareddy",
                  "Medchal Malkajgiri", "Yadadri Bhuvanagiri", "Jangaon"]),
    ("Jangaon", ["Karimnagar", "Jayashankar Bhupalapalli", "Siddipet",
                 "Hanamkonda", "Warangal", "Yadadri Bhuvanagiri", "Mahabubabad"]),
    ("Hanamkonda", ["Karimnagar", "Jangaon", "Warangal"]),
    ("Warangal", ["Hanamkonda", "Jangaon", "Mulugu", "Mahabubabad"]),
    ("Mahabubabad", ["Jayashankar Bhupalapalli", "Mulugu", "Warangal", "Jangaon",
                     "Bhadradri Kothagudem", "Khammam", "Suryapet",
                     "Nalgonda", "Yadadri Bhuvanagiri"]),
    ("Bhadradri Kothagudem", ["Mulugu", "Mahabubabad", "Khammam"]),
    ("Khammam", ["Bhadradri Kothagudem", "Mahabubabad", "Suryapet"]),
    ("Suryapet", ["Mahabubabad", "Khammam", "Nalgonda"]),
    ("Nalgonda", ["Mahabubabad", "Suryapet", "Yadadri Bhuvanagiri",
                  "Medchal Malkajgiri", "Rangareddy", "Mahabubnagar"]),
    ("Yadadri Bhuvanagiri", ["Siddipet", "Jangaon", "Mahabubabad",
                             "Nalgonda", "Medchal Malkajgiri"]),
    ("Medchal Malkajgiri", ["Medak", "Siddipet", "Yadadri Bhuvanagiri",
                            "Nalgonda", "Hyderabad", "Rangareddy"]),
    ("Hyderabad", ["Medchal Malkajgiri", "Rangareddy"]),
    ("Rangareddy", ["Medchal Malkajgiri", "Hyderabad", "Nalgonda",
                    "Vikarabad", "Mahabubnagar", "Sangareddy"]),
    ("Vikarabad", ["Rangareddy", "Mahabubnagar", "Narayanpet"]),
    ("Mahabubnagar", ["Nalgonda", "Rangareddy", "Vikarabad",
                      "Nagarkurnool", "Wanaparthy", "Narayanpet"]),
    ("Nagarkurnool", ["Mahabubnagar", "Wanaparthy", "Jogulamba Gadwal"]),
    ("Wanaparthy", ["Mahabubnagar", "Nagarkurnool",
                    "Jogulamba Gadwal", "Narayanpet"]),
    ("Jogulamba Gadwal", ["Nagarkurnool", "Wanaparthy", "Narayanpet"]),
    ("Narayanpet", ["Vikarabad", "Mahabubnagar",
                    "Wanaparthy", "Jogulamba Gadwal"]),
]


nb = {d: n for d, n in district_map}
districts = [d for d, _ in district_map]

colors = ["Red", "Green", "Blue", "Yellow"]


def build_domains():
    return {d: colors[:] for d in districts}


def arc_reduce(doms, a, b):
    pruned = False

    for c in doms[a][:]:
        if not any(c != c2 for c2 in doms[b]):
            doms[a].remove(c)
            pruned = True

    return pruned


def run_ac3(doms):
    agenda = deque((a, b) for a in nb for b in nb[a])

    while agenda:
        a, b = agenda.popleft()

        if arc_reduce(doms, a, b):
            if not doms[a]:
                return False

            for c in nb[a]:
                if c != b:
                    agenda.append((c, a))

    return True


def no_conflict(d, c, assigned):
    return all(assigned.get(x) != c for x in nb[d])


def mrv(assigned, doms):
    return min(
        [d for d in districts if d not in assigned],
        key=lambda d: len(doms[d])
    )


def search(assigned, doms):
    if len(assigned) == len(districts):
        return assigned

    d = mrv(assigned, doms)

    for c in doms[d]:
        if no_conflict(d, c, assigned):
            assigned[d] = c

            saved = {}
            dead_end = False

            for x in nb[d]:
                if x not in assigned and c in doms[x]:
                    doms[x].remove(c)
                    saved[x] = c

                    if not doms[x]:
                        dead_end = True
                        break

            if not dead_end:
                out = search(assigned, doms)
                if out:
                    return out

            for x, col in saved.items():
                doms[x].append(col)

            del assigned[d]

    return None


print("\n" + "#" * 55)
print("   Telangana District Map Coloring (CSP)")
print("#" * 55)

print(f"\nTotal districts : {len(districts)}")
print(f"Colors available: {', '.join(colors)}\n")

doms = build_domains()

print("Step 1: Running AC-3 for arc consistency...\n")

if not run_ac3(doms):
    print("AC-3 failed: Map cannot be colored with given colors")
    sys.exit()

print("AC-3 successful. Proceeding to backtracking...\n")

coloring = search({}, doms)

if not coloring:
    print("No valid coloring found. Try adding more colors.\n")

else:
    colors_used = set(coloring.values())

    print("Coloring complete!\n")
    print(f"Colors used: {len(colors_used)} / {len(colors)}\n")

    print("-" * 55)
    print(f"{'District':<35} {'Color'}")
    print("-" * 55)

    for d in districts:
        print(f"{d:<35} {coloring[d]}")

    print("-" * 55)

    print("\nColor Groups:")

    for col in colors_used:
        group = [d for d in districts if coloring[d] == col]

        print(f"\n  {col}  ({len(group)} districts):")

        for d in group:
            print(f"    - {d}")

    print()
