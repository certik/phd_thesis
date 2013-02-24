A perhaps not so well known feature of STO and GTO bases is the fact that they
can be made systematically convergent towards the exact answer for the ground
state Hartree-Fock calculation. This section gives an overview of the
convergence algorithm.

GTO and STO Completeness
------------------------

The mathematical framework was given by Klahn in 1985 in papers
:cite:`Klahn1985a` and :cite:`Klahn1985b`. It is shown there (see
:cite:`Klahn1985a`, eq. (29) and (30)) that the following set of $N$ GTO basis
functions:

.. math::

    \sqrt{r} e^{-\zeta_n^N r^2}

for $n=1, 2, 3,\dots, N$ and $\zeta_n^N > 0$ is asymptotically complete in
$L^2(0, \infty)$ if and only if the following condition holds for the
exponents as we increase the number of basis functions $N\to\infty$:

.. math::
    :label: sto_gto_convergence

    \lim_{N\to\infty} \sum_{n=1}^N {\zeta_n^N\over 1 + (\zeta_n^N)^2} = \infty

It is furthermore shown that the following set of $N$ STO basis functions:

.. math::

    e^{-\zeta_n^N r}

for $n=1, 2, 3,\dots, N$ and $\zeta_n^N > 0$ is asymptotically complete in
$L^2(0, \infty)$ if and only if the condition :eq:`sto_gto_convergence` holds.

The condition :eq:`sto_gto_convergence` can also be reformulated in various
other ways, see the papers for more details. The task is now to provide a
systematic construction of GTO and STO bases to satisfy this condition and thus
provide systematic convergence. One way to do that is using a so called
even-tempered basis.

Even-tempered Bases
-------------------

An even-tempered (ET) basis is defined by making a special choice for the
exponents $\zeta_n^N$:

.. math::

    \zeta_n^N = \alpha_N (\beta_N)^n

where $\alpha_N > 0$ and $\beta_N > 0$. The whole basis for a given $N$ then
only depends on two parameters $\alpha_N$ and $\beta_N$ (as opposed to a
general basis which depends on $N$ usually distinct parameters $\zeta_n^N$).
The paper :cite:`Klahn1985a` shows that a necessary condition for this basis to
satisfy :eq:`sto_gto_convergence` (and thus being asymptotically complete) is:

.. math::

    \lim_{N\to\infty} \beta_N = 1

and also shows that this condition is sufficient
if furthermore one of the following additional conditions is fulfilled for
all $N=1, 2, 3,\dots$:

a) $\beta_N > 1$ and $\alpha_N < \alpha' < \infty$

or

b) $\beta_N < 1$ and $\alpha_N > \alpha'' > 0$

or

c) $0 < \alpha'' < \alpha_N < \alpha' < \infty$


One of the first widely cited publications on even-tempered bases is
:cite:`Schmidt1979` from 1979, which uses the choice 1. The article provides a
good motivation why that should work using Gaussian integral transforms, as
well as gives empirical evidence from numerical studies. The Klahn papers
:cite:`Klahn1985a` and :cite:`Klahn1985b` put this onto a firm mathematical
ground.

In order to systematically converge the even-tempered basis, we need to find a
formula (preferably) for updating the coefficients $\alpha_N$ and $\beta_N$ as
we increase the basis from $N$ to $N+1$ such that the necessary and sufficient
condition is asymptotically satisfied.
There are obviously many ways to do that, but one particular construction has
worked well :cite:`Cooper1982`, :cite:`Wilson1990`: by imposing even more restrictions on $\alpha_N$
and $\beta_N$ while still satisfying the convergence criterion stated above, we
can require:

.. math::

    \alpha \to 0; \beta\to1; \beta^N\to\infty

from which it follows

.. math::

    \log\alpha \to -\infty; \log\beta\to0; N \log\beta\to\infty

Which is satisfied for example by:

.. math::

    \alpha \sim (\beta-1)^a

    \log\beta \sim N^b

where $a > 0$ and $-1 < b < 0$. By taking the log of both sides we get:

.. math::

    \log \alpha_N  = a \log (\beta_N-1) + a'

    \log\log\beta_N = b \log N + b'

The constants $a$, $b$, $a'$ and $b'$ are independent of $N$. Writing these
equations for $N-1$ we get:

.. math::

    \log \alpha_{N-1}  = a \log (\beta_{N-1}-1) + a'

    \log\log\beta_{N-1} = b \log (N-1) + b'

and subtracting from the above, we obtain:

.. math::
    :label: alphabeta_update

    \beta_N = \left(\beta_{N-1}\right)^{\left(N\over N-1 \right)^b}

    \alpha_N = \alpha_{N-1} \left(\beta_N-1\over\beta_{N-1}-1\right)^a

This construction provides a systematic choice of the exponents.
Reference :cite:`Cooper1982` recommends $a=0.5$ and $b=-0.5$ for $s$-states and
$a=0.6$ and $b=-0.45$ for $p$-states based on the numerical results of
:cite:`Schmidt1979`, but any values satisfying $a > 0$ and $-1
< b < 0$ must eventually converge, because they satisfy the convergence
condition (but they might not converge as fast). Note that due to its
construction, the equation :eq:`alphabeta_update` is not the only possible way
to update the coefficients $\alpha_N$ and $\beta_N$, indeed a more general way
has been proposed in :cite:`Kryachko2003`, but even the simplest update formula
:eq:`alphabeta_update` seems to work well in most cases as suggested by
:cite:`Schmidt1979`.

In practice, one starts from some preoptimized even-tempered basis for the
given $N$ and then one updates $\alpha$ and $\beta$ in each iteration using the
equation :eq:`alphabeta_update`. The basis must converge towards the complete
basis (exact Hartree-Fock limit). The update works for both STO and GTO.

For molecular calculations, the reference :cite:`Feller1979` shows by numerical
examples that one can reuse the even-tempered bases that were optimized for the
individual atoms.

Rate of Convergence
-------------------

Now when completeness is established, the next question is to ask about the
rate of convergence.  All empirical evidence in :cite:`Schmidt1979`,
:cite:`Feller1979`, :cite:`Cooper1982` as well as our own results in this
thesis seem to suggest that the convergence is exponential with increasing $N$.
A theoretical study :cite:`Schwartz1963` shows that Laguerre polynomials
converge exponentially (using $L^2$ projections) towards any function that has
power series expansion about the origin, and has also an exponential decay at
$\infty$  (citing:
"This is the exponential convergence which we believe is typical of all
problems wherein the trial functions are similar in kind to the function to be
fitted, but are different only in details of the shape.").
As shown in :cite:`Schwartz1963`, the situation is more complicated for the
variational approximations to solutions of Schrödinger's equation, because one
has to study the solutions of the complete Hamiltonian.
The article shows that for explicitly correlated Hylleraas-type wavefunctions
the convergence is not always exponential, neither it is for the $s$-wave
electron-hydrogen scattering at zero energy and other problems. However, all
these examples are two electron systems with a two-particle Hamiltonian and the
convergence rate is then determined by cusps and singularities of the
wavefunction (citing: "the slower power rate of convergence results when the
trial functions do not have the same analytical behavior as the function being
represented.").

On the other hand, for a ground state radial Hartree-Fock calculation, where the
exact radial wavefunction has a simple power expansion at origin and
exponential decay at infinity, the article seems to suggest that the STO basis
should converge exponentially, as indeed seems to be the case given our
numerical results.

For GTO basis, several theoretical studies have been made as well. For example
the papers :cite:`Kutzelnigg94` and :cite:`Braess1995` seem to establish that
the convergence of even-tempered GTO bases is also exponential.
A recent review article :cite:`Shavitt2004` is comparing STO and GTO.
