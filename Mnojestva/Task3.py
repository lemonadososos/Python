trebuemie_naviki = {'Python', 'SQL', 'Git', 'Docker'}

kandidat1 = {'Python', 'SQL', 'Git', 'Docker', 'Kubernetes'}
kandidat2 = {'Python', 'SQL', 'JavaScript'}
kandidat3 = {'Python', 'SQL', 'Git', 'HTML/CSS'}

treb_kad1 = kandidat1.union(trebuemie_naviki)
if treb_kad1 >= trebuemie_naviki:
    print("Кандидат 1 имеет все навыки")
else:
    print("Кандидат 1 имеет не все навыки")

otsut_treb1 = trebuemie_naviki.difference(treb_kad1)
if len(otsut_treb1) > 0:
    print("У кандидата 1 отсутвуют навыки", end=" ")
    print(*otsut_treb1, sep=", ")
else:
    print("У кандидата 1 все навыки есть")

dop_nav1 = kandidat1.difference(trebuemie_naviki)
if len(dop_nav1) > 0:
    print("У кандидата 1 есть такие дополнительные наваыки навыки:", end=" ")
    print(*dop_nav1, sep=", ")
else:
    print("У кандита 1 нет дополнительных навыков")


treb_kad2 = kandidat2.union(trebuemie_naviki)
if treb_kad2 >= trebuemie_naviki:
    print("Кандидат 2 имеет все навыки")
else:
    print("Кандидат 2 имеет не все навыки")

otsut_treb2 = trebuemie_naviki.difference(treb_kad2)
if len(otsut_treb2) > 0:
    print("У кандидата 2 отсутвуют навыки", end=" ")
    print(*otsut_treb1, sep=", ")
else:
    print("У кандидата 2 все навыки есть")

dop_nav2 = kandidat2.difference(trebuemie_naviki)
if len(dop_nav2) > 0:
    print("У кандидата 2 есть такие дополнительные наваыки навыки:", end=" ")
    print(*dop_nav2, sep=", ")
else:
    print("У кандита 2 нет дополнительных навыков")


treb_kad3 = kandidat3.union(trebuemie_naviki)
if treb_kad3 >= trebuemie_naviki:
    print("Кандидат 3 имеет все навыки")
else:
    print("Кандидат 3 имеет не все навыки")

otsut_treb3 = trebuemie_naviki.difference(treb_kad3)
if len(otsut_treb3) > 0:
    print("У кандидата 3 отсутвуют навыки", end=" ")
    print(*otsut_treb3, sep=", ")
else:
    print("У кандидата 3 все навыки есть")

dop_nav3 = kandidat3.difference(trebuemie_naviki)
if len(dop_nav3) > 0:
    print("У кандидата 3 есть такие дополнительные наваыки навыки:", end=" ")
    print(*dop_nav3, sep=", ")
else:
    print("У кандита 3 нет дополнительных навыков")