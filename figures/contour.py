from util import center_spines
from pylab import *

lam = array([float(x) for x in
"""
-4.7309197538237671      -0.30838295960915685       6.56408279474048062E-002  6.56408279474048062E-002  6.56408279474048062E-002  0.28793900640097969       0.36350961384916136       0.36350961384916136       0.36350961384916136       0.58990240339606115       0.58990240339606115       0.58990240339606115       0.58990240339606115       0.58990240339606115        1.8407555646629248        1.8407555646629248        1.8407555646629248        2.8605016873079578        8.6067195296634207        8.6067195296634207        8.6067195296634207        24.420177282004850        25.295571490597958        25.295571490597958        25.295571490597958        25.295571490597958        25.295571490597958        39.896765179527691        39.896765179527691        39.896765179527691
""".split()])
ea = []
for a in range(2):
    for r in range(2, size(lam)):
        for s in range(2, size(lam)):
            ea.append(-(lam[a]-lam[r]-lam[s]))
ip = []
for a in range(2):
    for b in range(2):
        for r in range(2, size(lam)):
            ip.append(-(lam[r]-lam[a]-lam[b]))
ea = unique(ea)
ip = unique(ip)
ea_gf = array([-4.61175302, -0.32724971])

plot(ip, [0]*size(ip), "r.", label="IP continuum")
plot(ea_gf, [0]*size(ea_gf), "go", label="IP 1s, 2s electrons")
plot(ea, [0]*size(ea), "b.", label="EA")
legend(loc="upper left")
plot([-60, 0, 0, -60, -60], [-0.1, -0.1, 0.1, 0.1, -0.1], "k-", lw=4)
center_spines()

xlim([-100, 10])
ylim([-1, 1])
xlabel("Re")
ylabel("Im")
ax = gca()
ax.xaxis.set_label_coords(1.05, 0.5)
ax.yaxis.set_label_coords(0.95, 1.0)
title("Integration contour")

savefig("sto_be_gf_contour.pdf")
