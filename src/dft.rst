Since we give results obtained with DFT in the Unscreened Results section,
we present here the standard formulas for atomic (radial) DFT.
A general overview of DFT is given for example in
:cite:`pickett` and :cite:`DFT`. In this section we only state the radial
Kohn-Sham equations, that are needed to solve atomic problems using DFT.

Kohn-Sham Equations
~~~~~~~~~~~~~~~~~~~

For spherically symmetric potentials, we write all eigenfunctions as:

.. math::

    \psi_{nlm} = R_{nl} Y_{lm}


and we need to solve the following Kohn-Sham equations:

.. math::

    -{1\over2}R_{nl}'' - {1\over r}R_{nl}' +
        \left(V + {l(l+1)R\over2 r^2}\right)R_{nl} = \epsilon_{nl} R_{nl}

With normalization:

.. math::

    \int R_{nl}^2 \,r^2 \,\d r = 1

For Schroedinger equation, the charge density is calculated by adding all "(n,
l, m)" states together, counting each one twice (for spin up and spin
down):

.. math::

    n({\bf r}) = \sum_{nlm}2|\psi_{nlm}|^2
        = \sum_{nlm}R_{nl}^2 2|Y_{lm}|^2
        = \sum_{nl}R_{nl}^2 2\sum_m|Y_{lm}|^2
        = {1\over 4\pi}\sum_{nl}f_{nl} R_{nl}^2

where we have introduced the occupation numbers $f_{nl}$ by

.. math::

    f_{nl} = 4\pi\,2\sum_m |Y_{lm}|^2

Normalization of the charge density is:

.. math::

    Z = \int n({\bf r}) \d^3 x
        = \int n(r) \, r^2\d\Omega \d r
        = 4\pi\int n(r) \, r^2 \d r
        =

        = 4\pi\int {1\over 4\pi} \sum_{nl} f_{nl} R_{nl}^2\, r^2\d\Omega \d r
        =

        = \sum_{nl} f_{nl}\int R_{nl}^2\, r^2 \d r
        =

        = \sum_{nl} f_{nl}

So we can see, that it must hold:

.. math::

    \sum_{nl} f_{nl} = Z

where $Z$ is the atomic number (number of electrons), and as such, $f_{nl}$ are
indeed the occupation numbers (integers). The factor $4\pi$ is
explicitly factored out, as it cancels with the spherical harmonics:
assuming all $m$ states are occupied, this can be simplified to:

.. math::

    f_{nl} = 4\pi\,2\sum_m |Y_{lm}|^2
        = 4\pi\,2{2l+1\over 4\pi}
        = 2(2l+1)

We can also use this machinery to prescribe "chemical occupation numbers", that
don't necessarily correspond to the DFT ground state. For example for the
uranium atom we get:

.. math::

    f_{1l} = 2 (2l+1)

    f_{2l} = 2 (2l+1)

    f_{3l} = 2 (2l+1)

    f_{4l} = 2 (2l+1)

    f_{5l} = 2 (2l+1)\quad\quad l\le2

    f_{53} = 3

    f_{60} = 2

    f_{61} = 6

    f_{62} = 1

    f_{70} = 2

By summing all these $f_{nl}$, we get 92 as expected:

.. math::

    \sum_{nl} f_{nl} = 2 + (2+6) + (2+6+10) + (2+6+10+14) + (2+6+10) +

        + 3 + 2 + 6 + 1 + 2 = 92

But this isn't the DFT ground state, because some KS energies are skipped, for
example there is only one state for $n=6$, $l=2$, but there are nine more
states with the same energy --- instead two more states are occupied in $n=7$,
$l=0$, but those have higher energy. So this corresponds to an excited DFT
state, which is strictly speaking not physically valid in the DFT formalism.
But in practice this approach is often used. One can also prescribe fractional
occupation numbers (in the Dirac case).

Poisson Equation
~~~~~~~~~~~~~~~~

Poisson equation becomes:

.. math::

    V_H''(r) + {2\over r} V_H'(r) = -4\pi n(r)

Total Energy
~~~~~~~~~~~~

The total energy is given by:

.. math::

    E[n]= T_s[n]+E_H[n]+E_{xc}[n]+V[n]

where

.. math::

    T_s[n] = \sum_{nl} f_{nl}\epsilon_{nl}
        -\int (V_H(r) + V_{xc}(r) + v(r))_{in} n(r) \d^3 r
        =

        = \sum_{nl} f_{nl}\epsilon_{nl}
            -\int \left(V_H(r) + V_{xc}(r) -{Z\over r}\right)_{in} n(r) \d^3 r

    E_H[n] = \half\int V_H(r) n(r) \d^3r

    E_{xc}[n]=\int \epsilon_{xc}(r;n) n(r) \d^3r

    V[n]=\int v(r) n(r) \d^3r = -\int {Z\over r} n(r) \d^3r

performing the angular integrations we obtain:

.. math::

    T_s[n] = \sum_{nl} f_{nl}\epsilon_{nl}
            -4\pi\int \left(V_H(r) + V_{xc}(r) -{Z\over r}\right)_{in} n(r)
                r^2\,\d r

    E_H[n] = 2\pi\int V_H(r) n(r)r^2\, \d r

    E_{xc}[n]=4\pi\int \epsilon_{xc}(r;n) n(r)r^2\, \d r

    V[n]=-4\pi \int {Z\over r} n(r)r^2\, \d r
        =-4\pi Z \int n(r)r\, \d r

We can also express everything using the charge density $\rho(r) = -n(r)$:

.. math::

    T_s[n] = \sum_{nl} f_{nl}\epsilon_{nl}
            +4\pi\int \left(V_H(r) + V_{xc}(r) -{Z\over r}\right)_{in} \rho(r)
                r^2\,\d r

    E_H[n] = -2\pi\int V_H(r) \rho(r)r^2\, \d r

    E_{xc}[n]=-4\pi\int \epsilon_{xc}(r;n) \rho(r)r^2\, \d r

    V[n]=4\pi \int {Z\over r} \rho(r)r^2\, \d r
        =4\pi Z \int \rho(r)r\, \d r
