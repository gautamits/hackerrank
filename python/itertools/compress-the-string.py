from itertools import groupby
arr=[list(g) for k,g in groupby(raw_input())]
arr2=[(len(a),int(a[0])) for a in arr]
print " ".join(map(str,arr2))