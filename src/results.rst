Unscreened Results
==================

The purpose of this section is to provide evidence that our program works and
is able to reproduce known results from the literature. We perform convergence
tests for the Hartree-Fock total energy, we check the energies for a particular
STO basis, we check second order perturbation theory as well as second order
Green function results against literature.

Historically, the standard reference for accurate STO orbitals used to be
:cite:`Clementi`. Lately, the new state of the art reference seems to be given
in the references :cite:`Koga1998` and :cite:`Koga2000`, that provides very
accurate and small STO bases for any atom from He to Lr.

Hartree-Fock
------------

Ra
~~

Radium is a closed shell atom with $Z=88$ and the configuration:

.. math::

    f_{n,0} &= [2, 2, 2, 2, 2, 2, 2] \\
    f_{n,1} &= [6, 6, 6, 6, 6] \\
    f_{n,2} &= [10, 10, 10] \\
    f_{n,3} &= [14] \\

We used the STO basis from :cite:`Koga2000`. Then the self-consistent SCF Hartree-Fock
energies are (we used ``tolE=1e-10`` and ``tolP=1e-4``):

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0      -3388.94104039     -92217.77956191
       2   0       -587.74420729     -15993.33393552
       3   0       -147.87172991      -4023.79458059
       4   0        -37.34157119      -1016.11587210
       5   0         -8.25316973       -224.58017937
       6   0         -1.37067573        -37.29798516
       7   0         -0.14876040         -4.04797645
       8   0          0.08165397          2.22191763
       9   0          0.72340804         19.68493462
      10   0          4.66147311        126.84513981
      11   0         25.24608995        686.98107455
      12   0        120.95628254       3291.38797843
      13   0        535.76303483      14578.85423631
      14   0       2517.93096422      68516.38899682
      15   0      17467.06888395     475303.13709612
       1   1       -566.94278080     -15427.29830980
       2   1       -137.79866067      -3749.69241475
       3   1        -32.72200096       -890.41096784
       4   1         -6.44987601       -175.51005952
       5   1         -0.81981163        -22.30820982
       6   1          0.30903607          8.40929961
       7   1          3.55206062         96.65648921
       8   1         18.98639327        516.64605785
       9   1         72.27839685       1966.79528758
      10   1        251.72462436       6849.77568014
      11   1        976.90370346      26582.90283152
      12   1       5274.79312909     143534.42689472
       1   2       -119.22873420      -3244.37899532
       2   2        -24.19779669       -658.45556300
       3   2         -3.29686823        -89.71235093
       4   2          0.70184142         19.09807715
       5   2          6.25455310        170.19505280
       6   2         24.88623637        677.18896040
       7   2         82.85779377       2254.67533067
       8   2        299.22996892       8142.46190290
       9   2       1466.26202858      39899.02064377
       1   3        -12.43050199       -338.25117611
       2   3          0.82042589         22.32492479
       3   3          7.01801677        190.96995658
       4   3         24.88560409        677.17175514
       5   3         78.31351681       2131.01926041
       6   3        314.75842103       8565.01259240
            EKIN+EHF (a.u.):  1.33E-04
      KINETIC ENERGY (a.u.):    23094.3036253898
    HF ATOMIC ENERGY (a.u.):   -23094.3034926210

.. raw:: latex

    \doublespacing

Which agrees with :cite:`Koga2000` to every single printed digit. There are a
total of 42 DOFs. We print 8 decimal digits after the floating point in order
to show the numerical accuracy of our results.

In the FE basis, with $p=20$ we get:

.. raw:: latex

    {}

    \singlespacing

::

     tolE:  1.00000000000000006E-009
     tolP:  1.00000000000000005E-004
     dP:  1.23226187438905178E-006
     Emax-Emin:  6.00266503170132637E-010
     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0      -3388.94108567     -92217.78079401
       2   0       -587.74424129     -15993.33486066
       3   0       -147.87175129      -4023.79516241
       4   0        -37.34161387      -1016.11703329
       5   0         -8.25320196       -224.58105652
       6   0         -1.37070249        -37.29871325
       7   0         -0.14877117         -4.04826955
       1   1       -566.94280420     -15427.29894631
       2   1       -137.79868421      -3749.69305533
       3   1        -32.72204108       -890.41205938
       4   1         -6.44990553       -175.51086305
       5   1         -0.81983794        -22.30892576
       1   2       -119.22876709      -3244.37989034
       2   2        -24.19783041       -658.45648063
       3   2         -3.29689595        -89.71310530
       1   3        -12.43052485       -338.25179817
            EKIN+EHF (a.u.):  7.46E-08
      KINETIC ENERGY (a.u.):    23094.30366649
    HF ATOMIC ENERGY (a.u.):   -23094.30366642

.. raw:: latex

    \doublespacing

There is total of 316 DOFs (79 DOFs for each $l=0, 1, 2, 3$).
In order to determine the accuracy of the total energy, we did a p-study,
see Figure :num:`fig-fe-ra-pstudy`. Instead of plotting the accuracy depending
on $p$, we can also plot the corresponding DOFs on the $x$-axis, see the Figure
:num:`fig-fe-ra-pstudy-dofs` (this graph also
contains the accuracy of the STO calculation above, as a black dot).

.. _fig-fe-ra-pstudy:

.. figure:: ../figures/fe_ra_convergence.*

    The FE p-study for radium.

.. _fig-fe-ra-pstudy-dofs:

.. figure:: ../figures/fe_ra_convergence_dofs.*

    The FE and STO convergence study for radium.

The figure above shows that the total energy is converged to $10^{-8}\rm\,
a.u.$ accuracy. This total energy agrees with the converged HF energy $E_{tot}
= -23094.30367$ from :cite:`Koga1996`. Compared to our converged energy, we can
see that the STO energy is $1.74\times 10^{-4}\rm\, a.u.$ accurate.

The total energies are summarized in Table :num:`ra-energies`.

.. figtable::
    :label: ra-energies
    :caption: Ra energies summary
    :spec: c l
    :nofig:

    =====================  ================
     Method                $E_{tot}$ [a.u.]
    =====================  ================
     STO                   -23094.303492621
     :cite:`Koga2000`      -23094.303492621
     FE                    -23094.30366642
     :cite:`Koga1996`      -23094.30367
    =====================  ================


Note that using the same STO basis for Ne we get.

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0        -32.77356052       -891.81397481
       2   0         -1.93123658        -52.55162211
       1   1         -0.85098345        -23.15643837
            EKIN+EHF (a.u.):  2.21E-03
      KINETIC ENERGY (a.u.):      128.54698875
    HF ATOMIC ENERGY (a.u.):     -128.54478045

.. raw:: latex

    \doublespacing

Which seems less accurate than the results for Ra as can be seen from the
virial theorem.

Mg
~~

Using the basis from :cite:`Koga1998` we obtain the following energies:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0        -49.03173628      -1334.22145568
       2   0         -3.76772161       -102.52492359
       3   0         -0.25305242         -6.88590681
       4   0          0.19036542          5.18010663
       5   0          1.31843427         35.87642254
       6   0          6.21612265        169.14930695
       7   0         23.31152940        634.33900255
       8   0         82.63946152       2248.73420784
       9   0        354.50455399       9646.55992069
      10   0       2672.27000174      72716.16797485
       1   1         -2.28222603        -62.10253134
       2   1          0.06757963          1.83893544
       3   1          0.89720617         24.41422262
       4   1          4.69875505        127.85963292
       5   1         18.45916821        502.29953397
       6   1         72.19528066       1964.53358083
       7   1        291.83482629       7941.22982924
            EKIN+EHF (a.u.):  2.73E-08
      KINETIC ENERGY (a.u.):      199.61463630
    HF ATOMIC ENERGY (a.u.):     -199.61463627

.. raw:: latex

    \doublespacing

The total energy from this STO result is plotted (circle) with FE convergence
study in Figure :num:`fig-fe-mg-conv`. We also plotted a so called
even-tempered STO basis from :cite:`Koga1993` and plotted convergence
(triangles) as well as the virial theorem (crosses) into the same graph. The
values are in the Table :num:`mg-et-values`.  Notice that for DOF=15 the virial
theorem says $8.5\times 10^{-8}\rm\,a.u.$, but from the graph, the accuracy of
the solution is only around $10^{-4}\rm\,a.u.$. With increasing the size of the
basis (the $N_b$ column), the virial theorem error gets worse to almost
$10^{-4}\rm\,a.u.$. This is caused by the fact, that the virial theorem only
provides a lower bound of the error.

By properly updating the $\alpha$ and $\beta$ parameters of the even-tempered
STO basis we can converge the total energy
to $10^{-9}\rm\,a.u.$, see Figure :num:`fig-fe-mg-conv-et`.

.. figtable::
    :label: mg-et-values
    :caption: Even-tempered STO basis Etot and virial theorem values for Mg
    :spec: r r r r
    :nofig:

    ==  ==== ======================= =======================
    Nb  DOFS         Etot                virial theorem
    ==  ==== ======================= =======================
     3     9 -1.9564661093751155E+02  2.3306633268013258E+01
     4    12 -1.9961452117971305E+02  8.6578325391428734E-04
     5    15 -1.9961458931754072E+02  8.5459817000810290E-08
     6    18 -1.9961459732988519E+02  1.9453174084560487E-04
     7    21 -1.9961460026776570E+02  2.8981480468814880E-04
     8    24 -1.9961460111276716E+02  3.2856031558026189E-04
     9    27 -1.9961460141633930E+02  3.4488235490925945E-04
    10    30 -1.9961460153923431E+02  3.5201552296371119E-04
    11    33 -1.9961460159216077E+02  3.5519382603865779E-04
    12    36 -1.9961460161569153E+02  3.5646990903615006E-04
    13    39 -1.9961460162633020E+02  3.5544459390735028E-04
    14    42 -1.9961460163116988E+02  3.7544886237128594E-04
    ==  ==== ======================= =======================


.. _fig-fe-mg-conv:

.. figure:: ../figures/fe_mg_convergence.*

    The FE and STO convergence study for Mg


.. _fig-fe-mg-conv-et:

.. figure:: ../figures/fe_mg_convergence_ET.*

    The FE and even-tempered STO convergence study for Mg

Xe
~~

We did even-tempered STO convergence study for Xe,
see Figure :num:`fig-sto-xe-conv-et`.

.. _fig-sto-xe-conv-et:

.. figure:: ../figures/sto_xe_convergence_ET.*

    Even-tempered STO convergence study for Mg

And we get the total energy $-7232.138362$ with accuracy
$2\times 10^{-6}\rm\,a.u.$.

Green's Function
----------------

Be
~~

We use the basis from :cite:`Doll1972`:

.. raw:: latex

    {}

    \singlespacing

::

    nbfl(0) = 5
    nl(:5, 0) = [1, 1, 3, 2, 2]
    zl(:5, 0) = [5.4297_dp, 2.9954_dp, 3.5810_dp, 1.1977_dp, 0.8923_dp]
    nbfl(1) = 5
    nl(:5, 1) = [2, 2, 4, 3, 3]
    zl(:5, 1) = [5.6998_dp, 2.7850_dp, 4.1500_dp, 1.4387_dp, 0.9819_dp]
    nbfl(2) = 2
    nl(:2, 2) = [3, 3]
    zl(:2, 2) = [1.2662_dp, 7.8314_dp]

.. raw:: latex

    \doublespacing

and obtain for Hartree-Fock:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -4.73091975       -128.73487906
       2   0         -0.30838296         -8.39152746
       3   0          0.28793901          7.83521917
       4   0          2.86050169         77.83821285
       5   0         24.42017728        664.50684701
       1   1          0.06564083          1.78617784
       2   1          0.36350961          9.89160007
       3   1          1.84075556         50.08950845
       4   1          8.60671953        234.20075914
       5   1         39.89676518       1085.64623955
       1   2          0.58990240         16.05206144
       2   2         25.29557149        688.32753589
            EKIN+EHF (a.u.):  9.87E-04
      KINETIC ENERGY (a.u.):       14.57377528
    HF ATOMIC ENERGY (a.u.):      -14.57278856

.. raw:: latex

    \doublespacing

The MBPT2 gives:

.. raw:: latex

    {}

    \singlespacing

::

     MBPT results:
     E0+E1 (HF)    =    -14.57278856

.. raw:: latex

    \doublespacing

The Green's function calculation gives:

.. raw:: latex

    {}

    \singlespacing

::

     Green's function calculation:
       E =     -4.61175302   dE =   7.65E-11
       E =     -0.32724971   dE =   6.27E-12
     Ntot =    4.0052366660634702
     Etot =  -14.666238504287731

.. raw:: latex

    \doublespacing

The total energy was calculated using a rectangular contour from $0$ to
$-60\rm\, a.u.$.
Extending the integration contour further than $-60\rm\, a.u.$ does not change
the total energy.
We partition the domain into $0.1 \times 0.1$ rectangles and
integrate using Gaussian integration of order $N_q = 20$ over the top and
bottom parts of each rectangle (as well as the left resp. right side of the
very left resp. very right rectangle), see the Figure :num:`sto-be-gf-contour`.
Following the approach from :cite:`Doll1972`, we have corrected the Green's
function total energy for lack of trace conservation by dividing it by the
ratio of the true trace to that actually produced. In the case of Be
we did ``Etot / Ntot * 4``.
The total energies are summarized in Table :num:`sto-be-gf`. The ionization
potentials are summarized in the Table :num:`sto-be-gf-ip`.

.. _sto-be-gf-contour:

.. figure:: ../figures/sto_be_gf_contour.*

    The contour for total energy integration of Be.

.. figtable::
    :label: sto-be-gf
    :caption: Green's function total energies for Be
    :spec: c l
    :nofig:

    =====================  ================
     Method                $E_{tot}$ [a.u.]
    =====================  ================
     HF                     -14.57278856
     HF :cite:`Doll1972`    -14.572789
     GF                     -14.647063
     GF :cite:`Doll1972`    -14.641639
    =====================  ================

.. figtable::
    :label: sto-be-gf-ip
    :caption: Green's function IP energies for Be
    :spec: c l l
    :nofig:

    =====================  ======================= ============
     Method                $E_1$ [a.u.]            $E_2$ [a.u.]
    =====================  ======================= ============
     HF                     -4.73091975            -0.30838296
     HF :cite:`Doll1972`    -4.731                 -0.308
     GF                     -4.61175302            -0.32724971
     GF :cite:`Doll1972`    -4.612                 -0.327
    =====================  ======================= ============

He
~~

For He we use again the basis from :cite:`Doll1972`:

.. raw:: latex

    {}

    \singlespacing

::

    nbfl(0) = 5
    nl(:5, 0) = [1, 1, 2, 3, 3]
    zl(:5, 0) = [1.4191_dp, 2.5722_dp, 4.2625_dp, 3.9979_dp, 5.4864_dp]
    nbfl(1) = 4
    nl(:4, 1) = [2, 2, 3, 4]
    zl(:4, 1) = [2.5834_dp, 3.6413_dp, 5.5308_dp, 5.7217_dp]
    nbfl(2) = 3
    nl(:3, 2) = [3, 3, 4]
    zl(:3, 2) = [3.6365_dp, 4.8353_dp, 6.9694_dp]

.. raw:: latex

    \doublespacing

and we get for HF:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -0.91804537        -24.98128597
       2   0          0.88239287         24.01113203
       3   0          5.07439794        138.08139625
       4   0         19.66534934        535.12139290
       5   0        119.00491186       3238.28847938
       1   1          1.16674233         31.74867471
       2   1          5.07923156        138.21292570
       3   1         17.00970593        462.85765772
       4   1         55.12789316       1500.10632781
       1   2          3.79051952        103.14528608
       2   2         16.77713044        456.52895653
       3   2         60.33563243       1641.81612641
            EKIN+EHF (a.u.): -4.08E-04
      KINETIC ENERGY (a.u.):        2.86127076
    HF ATOMIC ENERGY (a.u.):       -2.86167868

.. raw:: latex

    \doublespacing

for MBPT2:

.. raw:: latex

    {}

    \singlespacing

::

     MBPT results:
     E0+E1 (HF)    =     -2.86167868

.. raw:: latex

    \doublespacing

and Green's function:


.. raw:: latex

    {}

    \singlespacing

::

     Green's function calculation:
       E =     -0.90587321   dE =   9.02E-12
     Ntot =   2.0001613956929334
     Etot =  -2.9012448886081441

.. raw:: latex

    \doublespacing

We correct the total energy for lack of trace conservation. We used the same
contour as for Be (Figure :num:`sto-be-gf-contour`) and the same integration
order $N_q=20$..  The total energies are
summarized in Table :num:`sto-he-gf`. The ionization potentials are summarized
in the Table :num:`sto-he-gf-ip`.

.. figtable::
    :label: sto-he-gf
    :caption: Green's function total energies for He
    :spec: c l
    :nofig:

    =====================  ================
     Method                $E_{tot}$ [a.u.]
    =====================  ================
     HF                     -2.86167868
     HF :cite:`Doll1972`    -2.86168
     GF                     -2.9010108
     GF :cite:`Doll1972`    -2.90090
    =====================  ================

.. figtable::
    :label: sto-he-gf-ip
    :caption: Green's function IP energies for He
    :spec: c l
    :nofig:

    =====================  ============
     Method                $E_1$ [a.u.]
    =====================  ============
     HF                     -0.91804537
     HF :cite:`Doll1972`    -0.918
     GF                     -0.90587321
     GF :cite:`Doll1972`    -0.906
    =====================  ============

Hydrogen Molecule
~~~~~~~~~~~~~~~~~

For the $H_2$ we use the interatomic distance $1.4\rm\,a.u.$
and the 6-31G** Gaussian basis, the same configuration as in :cite:`szabo`
(see also this reference for a detailed description of the basis).
Total energy comparison is in the Table :num:`gauss-h2`.
The ionization potentials are in the Table :num:`gauss-h2-ip`.

.. figtable::
    :label: gauss-h2
    :caption: HF and MBPT2 total energies for the hydrogen molecule
    :spec: c l
    :nofig:

    =========================  ================
     Method                    $E_{tot}$ [a.u.]
    =========================  ================
     HF                        -1.13128434
     HF :cite:`szabo`          -1.131
     MBPT2                     -0.026341791
     MBPT2 :cite:`szabo`       -0.0263
     MBPT2 :cite:`gamess-uk`   -0.02634179
     MBPT3                     -0.005515979
     MBPT3 :cite:`gamess-uk`   -0.00551598
    =========================  ================

.. figtable::
    :label: gauss-h2-ip
    :caption: Green's function IP energies for the hydrogen molecule
    :spec: c l
    :nofig:

    =====================  ============
     Method                $E_1$ [a.u.]
    =====================  ============
     HF                     -0.59465997
     HF :cite:`szabo`       -0.595
     GF                     -0.59832340
     GF :cite:`szabo`       -0.598
    =====================  ============

Ammonia
~~~~~~~

For $NH_3$ we use the atomic configuration from :cite:`szabo`
and the 6-31G** Gaussian basis.
Total energy comparison is in the Table :num:`gauss-nh3`.
The ionization potentials are in the Table :num:`gauss-nh3-ip`.
Note: the HF energy $-0.421$ from :cite:`szabo` is probably wrong, because the
total energy as well as the Green's function ionization potential agrees.

.. figtable::
    :label: gauss-nh3
    :caption: HF total energies for ammonia
    :spec: c l
    :nofig:

    =====================  ================
     Method                $E_{tot}$ [a.u.]
    =====================  ================
     HF                    -56.19457246
     HF :cite:`szabo`      -56.195
    =====================  ================

.. figtable::
    :label: gauss-nh3-ip
    :caption: Green's function IP energies for ammonia
    :spec: c l
    :nofig:

    =====================  ============
     Method                $E_1$ [a.u.]
    =====================  ============
     HF                     -0.41491598
     HF :cite:`szabo`       -0.421
     GF                     -0.35357570
     GF :cite:`szabo`       -0.353
    =====================  ============

Methane
~~~~~~~

For the $CH_4$ molecule we use the $CH$ bond length of $2.05\rm\,a.u.$
and the 6-31G** Gaussian basis, the same configuration as in :cite:`szabo`.
Total energy comparison is in the Table :num:`gauss-ch4`.
The ionization potentials are in the Table :num:`gauss-ch4-ip`.

.. figtable::
    :label: gauss-ch4
    :caption: HF and MBPT2 total energies for the methane molecule
    :spec: c l
    :nofig:

    =========================  ================
     Method                    $E_{tot}$ [a.u.]
    =========================  ================
     HF                        -40.20170036
     HF :cite:`szabo`          -40.202
     MBPT2                     -0.16815509
     MBPT2 :cite:`gamess-uk`   -0.16815509
     MBPT3                     -0.01819243
     MBPT3 :cite:`gamess-uk`   -0.01819243
    =========================  ================

.. figtable::
    :label: gauss-ch4-ip
    :caption: Green's function IP energies for the methane molecule
    :spec: c l
    :nofig:

    ======================  ============
     Method                 $E_1$ [a.u.]
    ======================  ============
     HF                     -0.54451008
     HF :cite:`szabo`       -0.543
     HF :cite:`gamess-uk`   -0.54451009
     GF                     -0.51384473
     GF :cite:`szabo`       -0.510
    ======================  ============

Screened Results
================

After having presented plenty of evidence for the trustworthiness of our
computational tools, we present in this section the results for screened
electron-nucleus as well as electron-electron interaction.

In particular, we show that if we only screen electron-nucleus as opposed to
both electron-nucleus and electron-electron screening, we can produce the same
total energy. This means that the experimental results can be interpreted in
different ways.

Be
--

In Figure :num:`sto-be-screen-gf` we plot the Hartree-Fock eigenvalues together
with second order Green's function results for Be. Both exhibit similar trend.

.. _sto-be-screen-gf:

.. figure:: ../figures/sto_be_screen_gf.*

    HF and GF eigenvalues for beryllium.

We have also performed a calculation with $D_{en}=100$ and $D_{ee}=\infty$
(i.e. without $e-e$ screening):

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -4.69136904       -127.65864930
       2   0         -0.26897735         -7.31924625
       3   0          0.32713617          8.90182828
       4   0          2.89995575         78.91181265
       5   0         24.45968140        665.58180867
       1   1          0.10485005          2.85311497
       2   1          0.40275502         10.95952181
       3   1          1.88017673         51.16221303
       4   1          8.64622701        235.27581235
       5   1         39.93628578       1086.72164972
       1   2          0.62923171         17.12226644
       2   2         25.33510034        689.40317060
            EKIN+EHF (a.u.):  1.59E-01
      KINETIC ENERGY (a.u.):       14.57263329
    HF ATOMIC ENERGY (a.u.):      -14.41399656

.. raw:: latex

    \doublespacing

The total energy $-14.41399656\rm\,a.u.$ can be reproduced
alternatively
with
$D_{en}=80$ and $D_{ee}=151.32235$ to accuracy $10^{-8}\rm\,a.u.$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -4.70120880       -127.92640299
       2   0         -0.27891615         -7.58969477
       3   0          0.31064466          8.45307135
       4   0          2.88349893         78.46399957
       5   0         24.44323726        665.13434093
       1   1          0.08836110          2.40442782
       2   1          0.38626422         10.51078439
       3   1          1.86371042         50.71414173
       4   1          8.62977885        234.82823507
       5   1         39.91984324       1086.27422554
       1   2          0.61274761         16.67371109
       2   2         25.31865776        688.95574533
            EKIN+EHF (a.u.):  1.58E-01
      KINETIC ENERGY (a.u.):       14.57230512
    HF ATOMIC ENERGY (a.u.):      -14.41399656

.. raw:: latex

    \doublespacing

as well as with $D_{en}=50$ and $D_{ee}=37.102069$ to accuracy
$10^{-8}\rm\,a.u.$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -4.72975509       -128.70318697
       2   0         -0.30806010         -8.38274204
       3   0          0.26320819          7.16225946
       4   0          2.83506986         77.14617762
       5   0         24.39469170        663.81334896
       1   1          0.04090382          1.11304972
       2   1          0.33855496          9.21254935
       3   1          1.81533650         49.39782038
       4   1          8.58115980        233.50524356
       5   1         39.87122358       1084.95121734
       1   2          0.56467167         15.36549832
       2   2         25.26998935        687.63141044
            EKIN+EHF (a.u.):  1.60E-01
      KINETIC ENERGY (a.u.):       14.57416124
    HF ATOMIC ENERGY (a.u.):      -14.41399656

.. raw:: latex

    \doublespacing

or with $D_{en}=D_{ee}=62.50862$ to accuracy
$10^{-8}\rm\,a.u.$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -4.71470166       -128.29356232
       2   0         -0.29263351         -7.96296299
       3   0          0.28814455          7.84081227
       4   0          2.86073937         77.84468044
       5   0         24.42045295        664.51434834
       1   1          0.06585616          1.79203731
       2   1          0.36368780          9.89644875
       3   1          1.84096083         50.09509399
       4   1          8.60697118        234.20760691
       5   1         39.89703911       1085.65369363
       1   2          0.59006984         16.05661757
       2   2         25.29583992        688.33484027
            EKIN+EHF (a.u.):  1.59E-01
      KINETIC ENERGY (a.u.):       14.57264209
    HF ATOMIC ENERGY (a.u.):      -14.41399656

.. raw:: latex

    \doublespacing

For $D_{en}=100$, $D_{ee}=\infty$ we calculate DFT results using the LDA exchange and
correlation potential:

.. raw:: latex

    {}

    \singlespacing

::

     Z=           4 N=        5500
    E_tot=        -14.288416
     state    E            occupancy
    1s          -3.816913    2.000
    2s          -0.166421    2.000

.. raw:: latex

    \doublespacing


and with $D_{en}=D_{ee}=\infty$:

.. raw:: latex

    {}

    \singlespacing

::

     Z=           4 N=        5500
    E_tot=        -14.447209
     state    E            occupancy
    1s          -3.856411    2.000
    2s          -0.205744    2.000

.. raw:: latex

    \doublespacing


Mg
--

In the Figure :num:`sto-mg-screen-gf` we plot Hartree-Fock eigenvalues together
with second order Green's function results for Mg.

.. _sto-mg-screen-gf:

.. figure:: ../figures/sto_mg_screen_gf.*

    HF and GF eigenvalues for magnesium.

For $D_{en}=100$, $D_{ee}=\infty$  we calculate DFT results using the LDA
exchange and correlation potential:

.. raw:: latex

    {}

    \singlespacing

::

     Z=          12 N=        5500
    E_tot=       -197.706607
     state    E            occupancy
    1s         -45.854891    2.000
    2s          -2.785497    2.000
    2p          -1.600722    6.000
    3s          -0.057813    2.000

.. raw:: latex

    \doublespacing

and with $D_{en}=D_{ee}=\infty$:

.. raw:: latex

    {}

    \singlespacing

::

     Z=          12 N=        5500
    E_tot=       -199.139406
     state    E            occupancy
    1s         -45.973167    2.000
    2s          -2.903746    2.000
    2p          -1.718970    6.000
    3s          -0.175427    2.000

.. raw:: latex

    \doublespacing

H Minus Ion
-----------

For $H^{-}$ we did a Coulomb calculation:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -0.04622233         -1.25777362
            EKIN+EHF (a.u.):  1.05E-07
      KINETIC ENERGY (a.u.):        0.48792984
    HF ATOMIC ENERGY (a.u.):       -0.48792973

.. raw:: latex

    \doublespacing

then $D_{ee}=D_{en}=20$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -0.04533145         -1.23353158
            EKIN+EHF (a.u.):  4.68E-02
      KINETIC ENERGY (a.u.):        0.48635786
    HF ATOMIC ENERGY (a.u.):       -0.43951187

.. raw:: latex

    \doublespacing

The accuracy of this calculation is roughly $10^{-5}\rm\,a.u.$ in total energy,
from a convergence study.
We also did $D_{ee}=40$, $D_{en}=20$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -0.02467076         -0.67132558
            EKIN+EHF (a.u.):  6.58E-02
      KINETIC ENERGY (a.u.):        0.48350408
    HF ATOMIC ENERGY (a.u.):       -0.41771724

.. raw:: latex

    \doublespacing

The accuracy of this calculation is roughly $10^{-5}\rm\,a.u.$ in total energy.

Finally we did $D_{ee}=10$, $D_{en}=20$:

.. raw:: latex

    {}

    \singlespacing

::

     Orbital energies:
       n   l          E [a.u.]            E [eV]
       1   0         -0.08019560         -2.18223338
            EKIN+EHF (a.u.):  1.79E-02
      KINETIC ENERGY (a.u.):        0.49583783
    HF ATOMIC ENERGY (a.u.):       -0.47793727

.. raw:: latex

    \doublespacing


The accuracy of this calculation is roughly $10^{-6}\rm\,a.u.$ in total energy.

This can be compared with correlated wave function results :cite:`Zhang1996`,
see the Table :num:`hminus`.

.. figtable::
    :label: hminus
    :caption: H minus screened total energies summary
    :spec: c c c c
    :nofig:

    ===== === =============== ==============
     Den  Dee HF total energy Correlated wf.
    ===== === =============== ==============
     oo   oo    -0.48793       -0.5277
     20   20    -0.43951       -0.47904
     20   10    -0.47794       -0.51590
    ===== === =============== ==============
