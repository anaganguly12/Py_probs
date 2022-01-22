import powerset as ps
s1 = {1, 2, 3, 4}
s2 = {2, 3, 4, 6}

o1 = ps.PowerSet(s1)
o2 = ps.PowerSet(s2)

o1 + o2
o1 * o2
o1 - o2
