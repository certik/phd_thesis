In solving the atomic Kohn-Sham equations, one possible numerical method is a
shooting method, which needs to start with a proper asymptotic at the origin.
Below we describe the correct asymptotic for both Schrödinger and Dirac
equations. The present approach is directly applicable to the Dirac equation,
so we also show the asymptotic for the radial Dirac equation.

Schrödinger
~~~~~~~~~~~

The radial Schrödinger equation is:

.. math::

    P''(r) + 2\left(E-V(r)-{l(l+1)\over 2r^2}\right) P(r) = 0

    Q(r) = P'(r)

For $r\to\infty$, assuming $V(r)\to0$ we get:

.. math::

    P''(r) + 2E P(r) = 0

And the asymptotic is:

.. math::

    P(r) = e^{-\sqrt{-2E} r}

    Q(r) = P'(r) = -\sqrt{-2E} e^{-\sqrt{-2E} r}

For $r\to0$ and assuming that $V(r)$ can be neglected compared to the
${l(l+1)\over 2r^2}$ term (for example $V(r) = -Z/r + O(1)$ is acceptable) we
get:

.. math::

    P''(r) -{l(l+1)\over r^2} P(r) = 0

And the asymptotic is:

.. math::

    P(r) = r^{l+1}

    Q(r) = (l+1) r^l

Dirac
~~~~~

The Dirac equation is:

.. math::

    H = \left(\begin{array}{cc}
        V(r) + c^2 & c\left(-{\d\over\d r}+{\kappa\over r}\right) \\
        c \left({\d\over\d r}+{\kappa\over r}\right) & V(r) - c^2 \\
        \end{array}\right)

    H\left(\begin{array}{c}
        P(r) \\
        Q(r) \\
        \end{array}\right) =
    W\left(\begin{array}{c}
        P(r) \\
        Q(r) \\
        \end{array}\right)

Where the relativistic energy $W = E + c^2$. In terms of the nonrelativistic
energy it becomes:

.. math::

    H_{nonrel} = \left(\begin{array}{cc}
        V(r) & c\left(-{\d\over\d r}+{\kappa\over r}\right) \\
        c \left({\d\over\d r}+{\kappa\over r}\right) & V(r) - 2c^2 \\
        \end{array}\right)

    H_{nonrel}\left(\begin{array}{c}
        P(r) \\
        Q(r) \\
        \end{array}\right) =
    E\left(\begin{array}{c}
        P(r) \\
        Q(r) \\
        \end{array}\right)

For $r\to\infty$, assuming $V(r)\to 0$ we get:

.. math::

    H = \left(\begin{array}{cc}
        c^2 & -c{\d\over\d r} \\
        c {\d\over\d r} & - c^2 \\
        \end{array}\right)

and in terms of $P(r)$ and $Q(r)$:

.. math::

    c^2 P - c Q' = W P

    c P' - c^2 Q = W Q

let's put the derivatives on the left hand side:

.. math::

    c P' =  (W + c^2) Q

    c Q' = -(W - c^2) P

write a second order equation:

.. math::

    c^2 P'' =  (W + c^2) c Q' = - (W + c^2)(W - c^2) P
        = - (W^2 - c^4) P

and finally we get:

.. math::

    P'' + {W^2 - c^4 \over c^2} P = 0

    Q = {c\over W + c^2} P'

The asymptotic is:

.. math::

    P(r) = e^{-\sqrt{c^4-W^2\over c^2} r}

    Q(r) = {c\over W + c^2} \left(-\sqrt{c^4-W^2\over c^2}\right)
        e^{-\sqrt{c^4-W^2\over c^2} r}
      = -\sqrt{c^2-W\over c^2+W} e^{-\sqrt{c^4-W^2\over c^2} r}

We can also write it in terms of $E$:

.. math::

    P(r) = e^{-\sqrt{-2E-\left(E\over c\right)^2} r}

    Q(r) = -\sqrt{-{E\over E + 2c^2}} P(r)

For $r\to 0$ we write the full equations:

.. math::

    (V+c^2) P - c Q' + c{\kappa\over r} Q = W P

    c P' + c{\kappa\over r} P + (V-c^2) Q = W Q

The we assume $P(r) = r^\beta$ and use the second equation to express $Q(r)$:

.. math::

    Q(r) = {c P' + c{\kappa\over r} P \over W - V + c^2}
        ={c \beta r^{\beta-1} + c{\kappa\over r} r^\beta \over W - V + c^2}
        =r^{\beta-1} {c(\beta + \kappa)\over W - V + c^2}

We can always write any potential as $V(r) = -{Z(r)\over r}$ and we get:

.. math::

    Q(r)
        =r^{\beta-1} {c(\beta + \kappa)\over W + {Z(r)\over r} + c^2}
        =r^\beta {c(\beta + \kappa)\over Z(r) + (W + c^2)r}

If $Z(r)\to Z$ as $r\to 0$ then the term $(W + c^2)r$ goes to zero and we get:

.. math::

    Q(r) =r^\beta {c(\beta + \kappa)\over Z}

If $Z(r) \to Z_1 r$, then we get:

.. math::

    Q(r)
        =r^\beta {c(\beta + \kappa)\over Z_1 r + (W + c^2)r}
        =r^{\beta-1} {c(\beta + \kappa)\over Z_1 + W + c^2}

If $Z(r) \sim r^3$ (harmonic oscillator) or $Z(r) \sim r^2$, then the $Z(r)$
term goes to zero and we get:

.. math::

    Q(r) =r^{\beta-1} {c(\beta + \kappa)\over W + c^2}
