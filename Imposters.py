from pyfiglet import figlet_format

f = open("Following.txt", encoding="utf8")
l = []
for ln in f:
    lnstrip = ln.strip()
    lnsplit = lnstrip.split()
    l.append(lnsplit)

res = [ele for ele in l if ele != []]
f.close()

f2 = open("Followers.txt", encoding="utf8")
l2 = []
for ln2 in f2:
    ln2strip = ln2.strip()
    ln2split = ln2strip.split()
    l2.append(ln2split)
f2.close()

res2 = [ele for ele in l2 if ele != []]
nres = [i for i in res if i not in res2]

f = figlet_format("Imposters")
print(f)


for i in nres:
    print(i)
