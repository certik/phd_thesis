Appendices
==========


.. _legendre_polynomials:

Legendre Polynomials
--------------------

Legendre polynomials $P_l(x)$ defined by the Rodrigues formula

.. math::

       P_l(x)={1\over2^l l!}{\d^l\over\d x^l}[(x^2-1)^l]

they also obey the completeness relation

.. math::
    :label: Lorto

       \sum_{l=0}^\infty {2l+1\over2}P_l(x')P_l(x)=\delta(x-x')

and orthogonality relation:

.. math::

    \int_{-1}^1 P_k(x) P_l(x) \d x = {2\delta_{kl} \over 2k+1}

Two Legendre polynomials can be expanded in a series:

.. math::

    P_k(x) P_l(x)
        = \sum_{m=|k-l|}^{k+l}
        \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2
        (2m+1) P_m(x)

This was first proven by :cite:`Adams1878`, where he shows:

.. math::

    P_k(x) P_l(x) = \sum_{m=|k-l|}^{k+l} {A(s-k) A(s-l) A(s-m)\over A(s)}
        {2m+1\over 2s+1} P_m(x)

where $s={k+l+m\over 2}$ and

.. math::

    A(n) = {1\cdot3\cdot5 \cdot \dots \cdot (2n-1) \over
        1\cdot 2\cdot 3\cdot \dots \cdot n} =
            {(2n)!\over 2^n (n!)^2} = {1\over 2^n}\binom{2n}{n}

The coefficient in the expansion can then be written using a $3j$ symbol as:

.. math::

    {A(s-k) A(s-l) A(s-m)\over A(s)} {1\over 2s+1} =

    = {
            {1\over2^{s-k}}\binom{2s-2k}{s-k}
            {1\over2^{s-l}}\binom{2s-2l}{s-l}
            {1\over2^{s-m}}\binom{2s-2m}{s-m}
            \over
            {1\over2^{s}}\binom{2s}{s}
        } {1\over 2s+1} =

    = {2^s\over2^{s-k+s-l+s-m}} {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = {
            \binom{2s-2k}{s-k}
            \binom{2s-2l}{s-l}
            \binom{2s-2m}{s-m}
            \over
            \binom{2s}{s}
        } {1\over 2s+1} =

    = {
            {(2s-2k)! \over ((s-k)!)^2}
            {(2s-2l)! \over ((s-l)!)^2}
            {(2s-2m)! \over ((s-m)!)^2}
            {(s!)^2 \over (2s)!}
        } {1\over 2s+1} =

    = {(2s-2k)! (2s-2l)! (2s-2m)! \over (2s+1)!}
        \left[{s! \over (s-k)! (s-l)! (s-m)!}\right]^2
       =

    = \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

So we will just use the $3j$ symbol form from now on.
We can now calculate the integral of three Legendre polynomials:

.. math::
    :label: int_three_legendre_polys

    \int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x =

    = \int_{-1}^1
        \sum_{n=|k-l|}^{k+l}
        \begin{pmatrix} k & l & n \\ 0 & 0 & 0 \end{pmatrix}^2
        (2n+1) P_n(x)
    P_m(x) \d x =

    =
        \sum_{n=|k-l|}^{k+l}
        \begin{pmatrix} k & l & n \\ 0 & 0 & 0 \end{pmatrix}^2
        (2n+1) {2\delta_{nm}\over 2n+1}
    =

    = 2 \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2

This is consistent with the series expansion:

.. math::

    P_k(x) P_l(x) = \sum_{m=|k-l|}^{k+l}
        {2m+1\over 2}\int_{-1}^1 P_k(x) P_l(x) P_m(x) \d x\,\,
        P_m(x) =

    = \sum_{m=|k-l|}^{k+l}
        \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}^2
        (2m+1) P_m(x)

Any function $f(x)$ (where $-1\le x \le 1$) can be expanded as:

.. math::

    f(x) = \sum_{l=0}^\infty f_l P_l(x)

    f_l = {(2l+1)\over 2} \int_{-1}^1 f(x) P_l(x) \d x

For the following choice of $f(x)$ we get (for $|t| \le 1$):

.. math::

    f(x) = {1\over\sqrt{1-2xt+t^2}}

    f_l = {(2l+1)\over 2} \int_{-1}^1 {P_l(x)\over\sqrt{1-2xt+t^2}} \d x
        = {(2l+1)\over 2} \int_{|1+t|}^{|1-t|}
                 {P_l\left(1-R^2+t^2\over 2 t\right)\over R}
                 \left(-{R\over t}\right) \d R
        =

        = {(2l+1)\over 2 t} \int_{|1-t|}^{|1+t|}
                 P_l\left(1-R^2+t^2\over 2 t\right) \d R
        = {(2l+1)\over 2 t} \int_{1-t}^{1+t}
                 P_l\left(1-R^2+t^2\over 2 t\right) \d R
        =

        = t^l

Code:

.. raw:: latex

    {}

    \singlespacing

::

    >>> from sympy import var, legendre, integrate
    >>> var("l R t")
    (l, R, t)
    >>> f = (2*l+1) / (2*t) * integrate(legendre(l, (1-R**2+t**2) / (2*t)),
    ...         (R, 1-t, 1+t))
    >>> for _l in range(20): print _l, f.subs(l, _l).doit().simplify()
    ...
    0 1
    1 t
    2 t**2
    3 t**3
    4 t**4
    5 t**5
    6 t**6
    7 t**7
    8 t**8
    9 t**9
    10 t**10
    11 t**11
    12 t**12
    13 t**13
    14 t**14
    15 t**15
    16 t**16
    17 t**17
    18 t**18
    19 t**19

.. raw:: latex

    \doublespacing

So the Legendre polynomials are the coefficients of the following expansion
for $|t| \le 1$:

.. math::

    {1\over\sqrt{1-2xt+t^2}} = \sum_{l=0}^\infty P_l(x) t^l

Note that for $|t| > 1$ we get:

.. math::

    {1\over\sqrt{1-2xt+t^2}}
    = {1\over |t|}{1\over\sqrt{1-2x{1\over t}+\left({1\over t}\right)^2}}
    = {1\over |t|}\sum_{l=0}^\infty P_l(x) \left({1\over t}\right)^l
    = \sign t \sum_{l=0}^\infty P_l(x) t^{-l-1}


Example I
~~~~~~~~~

Very important is the following multipole expansion:

.. math::
    :label: legendre_expansion

    {1\over |{\bf r}-{\bf r'}|}
        ={1\over \sqrt{({\bf r}-{\bf r'})^2}}
        ={1\over \sqrt{r^2-2{\bf r}\cdot {\bf r'} + r'^2}}
        ={1\over r_>\sqrt{1-2\left(r_<\over r_>\right){\bf\hat r}\cdot {\bf\hat
            r'} + \left(r<\over r_>\right)^2}} =

    ={1\over r_>}\sum_{l=0}^\infty\left(r_<\over r_>\right)^l P_l({\bf\hat r}\cdot {\bf\hat r'})
    =\sum_{l=0}^\infty {r_<^l\over r_>^{l+1}} P_l({\bf\hat r}\cdot {\bf\hat r'})

Where $r_{>} = \max(r, r')$ and
$r_{<} = \min(r, r')$.
Assuming $r > r'$, we get for the first few terms:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
    ={1\over r}\left( P_0({\bf\hat r}\cdot {\bf\hat r'}) + P_1({\bf\hat r}\cdot {\bf\hat r'}){r'\over r} + P_2({\bf\hat r}\cdot {\bf\hat r'})\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r}\left( 1 + {\bf\hat r}\cdot {\bf\hat r'} {r'\over r} + \half\left(3({\bf\hat r}\cdot {\bf\hat r'})^2-1\right)\left(r'\over r\right)^2 + O\left(r'^3\over r^3\right) \right) =

    ={1\over r} +{{\bf r}\cdot {\bf r'}\over r^3} +{3({\bf r}\cdot {\bf r'})^2-r^2r'^2\over 2r^5} + O\left(r'^3\over r^4\right)

Example II
~~~~~~~~~~

Let's find the expansion of

.. math::

    f(x) = {e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}}

for $|t| \le 1$. We get:

.. math::

    f_l = {(2l+1)\over 2} \int_{-1}^1
        {P_l(x)e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}} \d x =

        = {(2l+1)\over 2} \int_{|1+t|}^{|1-t|}
                 {P_l\left(1-R^2+t^2\over 2 t\right)e^{-\alpha R}\over R}
                 \left(-{R\over t}\right) \d R
        =

        = {(2l+1)\over 2 t} \int_{|1-t|}^{|1+t|}
                 P_l\left(1-R^2+t^2\over 2 t\right) e^{-\alpha R} \d R =

        = {(2l+1)\over 2 t} \int_{1-t}^{1+t}
                 P_l\left(1-R^2+t^2\over 2 t\right) e^{-\alpha R} \d R

Here is the result for the first few $l$:

.. math::

    f_0 & = \frac{\left(e^{2 \alpha t} -1\right) e^{- \alpha t - \alpha}}{2 \alpha t} \\
    f_1 & = \frac{3}{2} \frac{\left(\alpha^{2} t e^{2 \alpha t} + \alpha^{2} t + \alpha t e^{2 \alpha t} + \alpha t - \alpha e^{2 \alpha t} + \alpha - e^{2 \alpha t} + 1\right) e^{- \alpha t - \alpha}}{\alpha^{3} t^{2}} \\
    f_2 & = \frac{5}{2} \frac{\left(\alpha^{4} t^{2} e^{2 \alpha t} - \alpha^{4} t^{2} + 3 \alpha^{3} t^{2} e^{2 \alpha t} - 3 \alpha^{3} t^{2} - 3 \alpha^{3} t e^{2 \alpha t} - 3 \alpha^{3} t + 3 \alpha^{2} t^{2} e^{2 \alpha t}   + X\right) e^{- \alpha t - \alpha}}{\alpha^{5} t^{3}}

    X = - 3 \alpha^{2} t^{2} - 9 \alpha^{2} t e^{2 \alpha t} - 9 \alpha^{2} t
    3 \alpha^{2} e^{2 \alpha t} - 3 \alpha^{2} - 9 \alpha t e^{2 \alpha t} - 9 \alpha t + 9 \alpha e^{2 \alpha t} - 9 \alpha + 9 e^{2 \alpha t} -9


Expanding in $t$ up to
$\operatorname{\mathcal{O}}\left(t^{7}\right)$ we get:

.. math::

    f_l & = e^{-\alpha} g_l \\
    g_0 & = 1 + \frac{1}{6} \alpha^{2} t^{2} + \frac{1}{120} \alpha^{4} t^{4} + \frac{1}{5040} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_1 & = t + \alpha t + \frac{1}{10} \alpha^{2} t^{3} + \frac{1}{10} \alpha^{3} t^{3} + \frac{1}{280} \alpha^{4} t^{5} + \frac{1}{280} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_2 & = t^{2} + \alpha t^{2} + \frac{1}{3} \alpha^{2} t^{2} + \frac{1}{14} \alpha^{2} t^{4} + \frac{1}{14} \alpha^{3} t^{4} + \frac{1}{42} \alpha^{4} t^{4} + \frac{1}{504} \alpha^{4} t^{6} + \frac{1}{504} \alpha^{5} t^{6} + \\
    &\quad\quad + \frac{1}{1512} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_3 & = t^{3} + \alpha t^{3} + \frac{2}{5} \alpha^{2} t^{3} + \frac{1}{18} \alpha^{2} t^{5} + \frac{1}{15} \alpha^{3} t^{3} + \frac{1}{18} \alpha^{3} t^{5} + \frac{1}{45} \alpha^{4} t^{5} + \frac{1}{270} \alpha^{5} t^{5} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\
    g_4 & = t^{4} + \alpha t^{4} + \frac{3}{7} \alpha^{2} t^{4} + \frac{1}{22} \alpha^{2} t^{6} + \frac{2}{21} \alpha^{3} t^{4} + \frac{1}{22} \alpha^{3} t^{6} + \frac{1}{105} \alpha^{4} t^{4} + \frac{3}{154} \alpha^{4} t^{6} + \frac{1}{231} \alpha^{5} t^{6} + \\
        &\quad\quad +\frac{1}{2310} \alpha^{6} t^{6} + \operatorname{\mathcal{O}}\left(t^{7}\right) \\



Code:

.. raw:: latex

    {}

    \singlespacing

::

    >>> from sympy import var, legendre, integrate, exp, latex, cse
    >>> var("l R t alpha")
    (l, R, t, alpha)
    >>>
    >>> f = (2*l+1) / (2*t) * integrate(legendre(l, (1-R**2+t**2) \
    ...         / (2*t)) * exp(-alpha*R), (R, 1-t, 1+t))
    >>>
    >>> for _l in range(3):
    ...     print "f_%d & =" %_l, latex(f.subs(l, _l).doit() \
    ...     .simplify()), "\\\\"
    ...
    f_0 & = \frac{\left(e^{2 \alpha t} -1\right) e^{- ... \\
    f_1 & = \frac{3}{2} \frac{\left(\alpha^{2} t e^{2 ... \\
    f_2 & = \frac{5}{2} \frac{\left(\alpha^{4} t^{2} ...  \\
    >>> for _l in range(5):
    ...     result = f.subs(l, _l).doit().simplify() / exp(-alpha)
    ...     print "g_%d & =" %_l, latex(result.series(t, 0, 7)), "\\\\"
    ...
    g_0 & = 1 + \frac{1}{6} \alpha^{2} t^{2} + \frac{1}{120} ... \\
    g_1 & = t + \alpha t + \frac{1}{10} \alpha^{2} t^{3} +   ... \\
    g_2 & = t^{2} + \alpha t^{2} + \frac{1}{3} \alpha^{2}    ... \\
    g_3 & = t^{3} + \alpha t^{3} + \frac{2}{5} \alpha^{2}    ... \\
    g_4 & = t^{4} + \alpha t^{4} + \frac{3}{7} \alpha^{2}    ... \\

.. raw:: latex

    \doublespacing

The long output of the script has been truncated by the dots "...".

Example III
~~~~~~~~~~~

.. math::

    {e^{-{|{\bf r}-{\bf r'}|\over D}}\over |{\bf r}-{\bf r'}|}
        = {e^{-r_>\sqrt{1-2\left(r_<\over r_>\right)
                {\bf\hat r}\cdot {\bf\hat r'}
            +\left(r_<\over r_>\right)^2}\over D}\over
                r_>\sqrt{1-2\left(r_<\over r_>\right)
                        {\bf\hat r}\cdot {\bf\hat r'}
                +\left(r_<\over r_>\right)^2}}
        = {1\over r_>}
            {e^{-\alpha \sqrt{1-2xt+t^2}}\over\sqrt{1-2xt+t^2}}

where:

.. math::

    \alpha & = {r_>\over D} \\
    x & = {\bf\hat r}\cdot {\bf\hat r'} \\
    t & = {r_<\over r_>}

Example IV
~~~~~~~~~~

.. math::

    V(|{\bf r}_1-{\bf r}_2|)
        = {e^{-{|{\bf r}_1-{\bf r}_2|\over D}}\over |{\bf r}_1-{\bf r}_2|}

The potential $V$ is a function of $r_1$, $r_2$ and $\cos\theta$ only:

.. math::

    V(|{\bf r}_1-{\bf r}_2|)
        = V\left(\sqrt{r_1^2 - 2 {\bf r_1} \cdot {\bf r_2} + r_2^2}\right)
        = V\left(\sqrt{r_1^2 - 2 r_1 r_2\cos\theta + r_2^2}\right) =

        = V(r_1, r_2, \cos\theta)

So we expand in the $\cos\theta$ variable using the Legendre expansion:

.. math::

    V(|{\bf r}_1-{\bf r}_2|)
        = V(r_1, r_2, \cos\theta)
        = \sum_{l=0}^\infty V_l(r_1, r_2) P_l(\cos\theta)

where $V_l(r_1, r_2)$ only depends on $r_1$ and $r_2$:

.. math::

    V_l(r_1, r_2) = {2l+1\over 2}\int_{-1}^1 V(|{\bf r}_1-{\bf r}_2|)
        P_l(\cos\theta) \d(\cos\theta) =

        = {2l+1\over 2}\int_{-1}^1
            {e^{-{|{\bf r}_1-{\bf r}_2|\over D}}\over |{\bf r}_1-{\bf r}_2|}
            P_l(\cos\theta) \d(\cos\theta) =

        = {2l+1\over 2 r_1 r_2}\int_{|r_1 - r_2|}^{r_1+r_2}
            e^{-{r\over D}}
            P_l\left(r_1^2 - r^2 + r_2^2 \over 2 r_1 r_2 \right) \d r

In the limit $D\to\infty$ we get:

.. math::

    V_l(r_1, r_2) \to {r_<^l\over r_>^{l+1}}

In general, the $V_l(r_1, r_2)$ expressions are complicated. For the first two
lowest $l$ we get:

.. math::

    V_0(r_1, r_2) = {D\over 2 r_1 r_2}\left(e^{-{|r_1 - r_2|\over D}} -
        e^{-{r_1 + r_2\over D}}\right)

    V_1(r_1, r_2) =
        \frac{3}{2} \frac{D \left(- D^{2} e^{2 \frac{r_{2}}{D}} + D^{2} - D
        r_{1} e^{2 \frac{r_{2}}{D}} + D r_{1} + D r_{2} e^{2 \frac{r_{2}}{D}} +
        X\right) e^{-
        \frac{r_{1}}{D} - \frac{r_{2}}{D}}}{r_{1}^{2} r_{2}^{2}}

    X = D r_{2} + r_{1} r_{2} e^{2 \frac{r_{2}}{D}} + r_{1} r_{2}

In $V_1(r_1, r_2)$ we assume $r_1 \ge r_2$.

Another option is to use the Gegenbauer's addition theorem, which gives
directly:

.. math::

    V_k(r_1, r_2) = (2k+1)
        {K_{k+\half}\left(r_>\over D\right) \over \sqrt{r_>}}
        {I_{k+\half}\left(r_<\over D\right) \over \sqrt{r_<}}

Using:

.. math::

    I_\nu(z) = {1\over \Gamma(\nu+1)} \left(z\over 2\right)^\nu
        {}_0F_1\left(\nu+1; {z^2\over 4}\right)

    K_\nu(z) = {\Gamma(\nu)\over 2} \left(2\over z\right)^\nu
        {}_0F_1\left(1-\nu; {z^2\over 4}\right)
            + {\Gamma(-\nu)\over 2} \left(z\over 2\right)^\nu
        {}_0F_1\left(\nu+1; {z^2\over 4}\right)

and

.. math::

    I_\nu(x) K_\nu(y) = {1\over 2\nu} \left(x\over y\right)^\nu
        {}_0F_1\left(\nu+1; {x^2\over 4}\right)
        {}_0F_1\left(1-\nu; {y^2\over 4}\right)
        +

        +
        {\Gamma(-\nu)\over 2\Gamma(\nu+1)} \left( xy\over 4\right)^\nu
        {}_0F_1\left(\nu+1; {x^2\over 4}\right)
        {}_0F_1\left(\nu+1; {y^2\over 4}\right)

we get

.. math::

    V_k(r_1, r_2) = {2k+1\over (r_> r_<)^\half}\left(
        {1\over 2k+1} \left(r_< \over r_>\right)^{k+\half}
            {}_0F_1\left(k+{3\over 2}; {r_<^2\over 4D^2}\right)
            {}_0F_1\left(\half - k; {r_>^2\over 4D^2}\right)
            +\right.

            \left. +
            {\pi\over2} {1\over\Gamma^2(k+{3\over2})\sin(\pi(k+{3\over2}))}
            \left(r_< r_>\over 4D^2\right)^{k+\half}
            {}_0F_1\left(k+{3\over 2}; {r_<^2\over 4D^2}\right)
            {}_0F_1\left(k+{3\over 2}; {r_>^2\over 4D^2}\right)
        \right) =

    = {r_<^k \over r_>^{k+1}}
            \ {}_0F_1\left(k+{3\over 2}; {r_<^2\over 4D^2}\right)
            {}_0F_1\left(\half - k; {r_>^2\over 4D^2}\right)
            +

            +
            {\pi\over (2D)^{2k+1}}
                (r_< r_>)^k {(-1)^{k+1}\over\Gamma(k+\half)\Gamma(k+{3\over2})}
            \ {}_0F_1\left(k+{3\over 2}; {r_<^2\over 4D^2}\right)
            {}_0F_1\left(k+{3\over 2}; {r_>^2\over 4D^2}\right)

where we used:

.. math::

    \Gamma(-\nu) = {\pi\over \sin(\pi(\nu+1))}
        {1\over \Gamma(\nu+1)}

Since ${}_0F_1\left(a; 0\right) = 1$, we get for $D\to\infty$:

.. math::

    V_k(r_1, r_2) \to {r_<^k \over r_>^{k+1}}

as we should.

Spherical Harmonics
-------------------


Are defined for $m \ge 0$ by

.. math::

       Y_{lm}(\theta,\phi)=\sqrt{{2l+1\over4\pi}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta)\,e^{im\phi}

where $P_l^m$ are associated Legendre polynomials defined by

.. math::

       P_l^m(x)=(-1)^m (1-x^2)^{m/2}{\d^m\over\d x^m} P_l(x)

and $P_l$ are Legendre polynomials. For $m < 0$ they are defined by:

.. math::

    Y_{lm}(\Omega) = (-1)^m Y_{l,-m}^*(\Omega)

Sometimes the spherical harmonics are
written as:

.. math::

    Y_{lm}(\theta,\phi) = \Theta_{lm}(\theta) \Phi_m(\phi)

where:

.. math::

    \Phi_m(\phi) &= {1\over\sqrt{2\pi}} e^{im\phi} \\
    \Theta_{lm}(\theta) &= \begin{cases}
        \sqrt{{2l+1\over2}{(l-m)!\over(l+m)!}}\,P_l^m(\cos\theta) &
            \mbox{for } m \ge 0 \\
        (-1)^m \Theta_{l,-m}(\theta) & \mbox{for } m < 0 \\
        \end{cases}

The spherical harmonics are orthonormal:

.. math::
    :label: Yorto

       \int Y_{lm}\,Y^*_{l'm'}\,\d\Omega = \int_0^{2\pi}\int_0^{\pi} Y_{lm}(\theta,\phi)\,Y^*_{l'm'}(\theta,\phi)\sin\theta\,\d\theta\,\d\phi = \delta_{mm'}\delta_{ll'}

and complete (both in the $l$-subspace and the whole space):

.. math::
    :label: lcomplete

       \sum_{m=-l}^l|Y_{lm}(\theta,\phi)|^2={2l+1\over4\pi}


.. math::
    :label: Ycomplete

       \sum_{l=0}^\infty\sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi') ={1\over\sin\theta}\delta(\theta-\theta')\delta(\phi-\phi')= \delta({\bf\hat r}-{\bf\hat r'})

The relation :eq:`lcomplete` is a special case of an addition theorem for spherical harmonics

.. math::
    :label: lsum

       \sum_{m=-l}^lY_{lm}(\theta,\phi)Y_{lm}^*(\theta',\phi')= {2l+1\over 4\pi}P_l(\cos\gamma)

where $\gamma$ is the angle between the unit vectors given by ${\bf\hat r}=(\theta,\phi)$ and ${\bf\hat r'}=(\theta',\phi')$:

.. math::

       \cos\gamma=\cos\theta\cos\theta'+\sin\theta\sin\theta'\cos(\phi-\phi') ={\bf\hat r}\cdot{\bf\hat r'}

Relations between complex conjugates is:

.. math::

    Y_{l m}^*(\Omega) = (-1)^m Y_{l,-m}(\Omega)

    (-1)^m Y_{l,-m}^*(\Omega) = Y_{lm}(\Omega)

Examples
~~~~~~~~

.. math::

    \int_{-1}^1 P_k(x) \d x
        = \int_{-1}^1 P_k(x) P_0(x) \d x
        = 2\delta_{k0}

    \int Y_{k0}(\Omega) \d \Omega
        = \int Y_{k0}(\Omega) \sqrt{4\pi} Y_{00}(\Omega) \d \Omega
        = \sqrt{4\pi} \delta_{k0}


Gaunt Coefficients
------------------

We use the Wigner-Eckart theorem:

.. math::

    \braket{j m | T^k_q | j' m'} = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (j || T^k || j')

Where:

.. math::

    T^k_q = Y_{k q}

In order to calculate the reduced matrix element $(j || T^k || j')$, we
evaluate the W-E theorem for $m=q=m'=0$:

.. math::

    \braket{j 0 | T^k_0 | j' 0} = (-1)^{j}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}
        (j || T^k || j')

and also evaluate the left hand side explicitly:

.. math::

    \braket{j 0 | T^k_0 | j' 0}
        = \braket{j 0 | Y_{k 0} | j' 0}
        = \int Y_{j0}^*(\Omega) Y_{k0}(\Omega) Y_{j'0}(\Omega) \d \Omega =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi} {1\over 4\pi}
        \int P_j(\cos\theta) P_k(\cos\theta) P_{j'}(\cos\theta) \sin\theta
            \d \theta \d \phi =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi} {1\over 2}
        \int_{-1}^1 P_j(x) P_k(x) P_{j'}(x) \d x =

    = \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}^2

where we used :eq:`int_three_legendre_polys`.
Comparing these two results, we get:

.. math::

    (j || T^k || j') = (-1)^{-j}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}

and finally:

.. math::

    \int Y_{jm}^*(\Omega) Y_{kq}(\Omega) Y_{j'm'}(\Omega) \d \Omega =

    =\braket{j m | T^k_q | j' m'} = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (j || T^k || j') =

    = (-1)^{j-m}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}
        (-1)^{-j}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2j+1)(2k+1)(2j'+1)\over 4\pi}
        \begin{pmatrix} j & k & j' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} j & k & j' \\ -m & q & m' \end{pmatrix}

In order to evaluate other integrals of spherical harmonics, we just use the
above result, for example:

.. math::

    \int Y_{l_1 m_1}(\Omega) Y_{l_2 m_2}(\Omega) Y_{l_3 m_3}(\Omega) \d\Omega =

    =(-1)^{m_1}\int Y_{l_1 -m_1}^*(\Omega) Y_{l_2 m_2}(\Omega)
        Y_{l_3 m_3}(\Omega) \d\Omega=

    =(-1)^{m_1}
    (-1)^{-(-m_1)}
        \sqrt{(2l_1+1)(2l_2+1)(2l_3+1)\over 4\pi}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ -(-m_1) & m_2 & m_3 \end{pmatrix}=

    = \sqrt{(2l_1+1)(2l_2+1)(2l_3+1)\over 4\pi}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l_1 & l_2 & l_3 \\ m_1 & m_2 & m_3 \end{pmatrix}

This is the most symmetric relation. It was first obtained by
:cite:`Gaunt1929`
(equation (9), p. 194, where the author expanded the $3j$ symbols, so his
formula is more complex but equivalent to the above).

It is useful to incorporate
the selection rule $m_1 + m_2 + m_3 = 0$ of the $3j$ symbols into the formula
and we get:

.. math::

    c^k(l, m, l', m') =
        \sqrt{4\pi \over 4k+1}
    \int Y_{lm}^*(\Omega) Y_{k, m-m'}(\Omega) Y_{l'm'}(\Omega) \d\Omega =

    = (-1)^{-m}
        \sqrt{4\pi \over 4k+1}
        \sqrt{(2l+1)(2k+1)(2l'+1)\over 4\pi}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}

In this form the $c^k$ symbols are the same as in :cite:`CondonShortley`.
From the other selection rules of the $3j$ symbols it follows, that
the $c^k(l, m, l', m')$ coefficients are nonzero only when:

.. math::

    |l-l'| \le k \le l + l'

    l+l'+k = \mbox{even integer}

Example I
~~~~~~~~~

.. math::

    c^0(l, m, l', m')
        =\sqrt{4\pi}
    \int Y_{lm}^*(\Omega) Y_{00}(\Omega) Y_{l'm'}(\Omega) \d\Omega
        =\delta_{l l'}\delta_{m m'}

Example II
~~~~~~~~~~

.. math::

    \sum_{m=-l}^l c^k(l, m, l, m)
        = \sum_m
        \sqrt{4\pi \over 4k+1}
        \int Y_{lm}^*(\Omega) Y_{k0}(\Omega) Y_{lm}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        \int \sum_m |Y_{lm}(\Omega)|^2 Y_{k0}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        {2l+1\over 4\pi} \int Y_{k0}(\Omega) \d\Omega =

        =
        \sqrt{4\pi \over 4k+1}
        {2l+1\over 4\pi}
        \sqrt{4\pi} \delta_{k0} =

        =
        (2l+1) \delta_{k0}

Example III
~~~~~~~~~~~

.. math::

    c^k(l, m, l', m') =
        \sqrt{4\pi \over 4k+1}
    \int Y_{lm}^*(\Omega) Y_{k, m-m'}(\Omega) Y_{l'm'}(\Omega) \d\Omega =

    = \sqrt{4\pi \over 4k+1}
    \int \Theta_{lm}\Phi_m^* \Theta_{k, m-m'}\Phi_{m-m'} \Theta_{l'm'}\Phi_{m'}
        \sin\theta \d\theta \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \int_0^{2\pi} \Phi_m^* \Phi_{m-m'} \Phi_{m'} \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \left(1\over\sqrt{2\pi}\right)^3
    \int_0^{2\pi} e^{-im\phi} e^{i(m-m')\phi} e^{im'\phi} \d\phi =

    = \sqrt{4\pi \over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta
    \left(1\over\sqrt{2\pi}\right)^3
    \int_0^{2\pi} \!\!\!\d\phi =

    = \sqrt{2\over 4k+1}
    \int_0^\pi \Theta_{lm} \Theta_{k, m-m'} \Theta_{l'm'} \sin\theta \d\theta

Example IV
~~~~~~~~~~

.. math::

    c^k(l, -m, l', -m') =

    = (-1)^{m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ m & -m+m' & -m' \end{pmatrix} =

    = (-1)^{m}(-1)^{l+k+l'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    c^k(l, m, l', m')

Where we used the fact, that $l+k+l'$ is an even integer and
$(-1)^m=(-1)^{-m}$. $c^k$ is not symmetric in $l m$ and $l' m'$:

.. math::

    c^k(l', m', l, m)

    = (-1)^{-m'}
        \sqrt{(2l'+1)(2l+1)}
        \begin{pmatrix} l' & k & l \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l' & k & l \\ -m' & m'-m & m \end{pmatrix} =

    = (-1)^{-m'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ m & m'-m & -m' \end{pmatrix} =

    = (-1)^{-m'}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{m-m'} (-1)^{-m}
        \sqrt{(2l+1)(2l'+1)}
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix} =

    = (-1)^{m-m'} c^k(l, m, l', m')

Few other identities:

.. math::

    c^k(l, 0, l', 0)
        = \sqrt{(2l+1)(2l'+1)}
            \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2

    \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        = {c^k(l, 0, l', 0) \over \sqrt{(2l+1)(2l'+1)}}
        = {c^{l'}(l, 0, k, 0) \over \sqrt{(2l+1)(2k+1)}}
        = {c^{l}(l', 0, k, 0) \over \sqrt{(2l'+1)(2k+1)}}

    c^k(l, 0, l', 0) = c^k(l', 0, l, 0)

Example V
~~~~~~~~~

.. math::

    \sum_{m'} \left(c^k(l, m, l', m')\right)^2 =

        = \sum_{m'}
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2 =

        =
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        \sum_{m'}
        \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2 =

        =
        (2l+1)(2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        {1\over 2l+1} =

        =
        (2l'+1)
        \begin{pmatrix} l & k & l' \\ 0 & 0 & 0 \end{pmatrix}^2
        =

        =\sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)


.. _five_spherical_harmonics:

Example VI
~~~~~~~~~~

.. math::
    :label: five_spherical_harmonics

    \sum_{m'}\sum_{q}\int
            Y_{l'm'}(\Omega)
            Y_{l'm'}^*(\Omega')
            Y_{kq}(\Omega)
            Y_{kq}^*(\Omega')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\int
            {2l'+1\over 4\pi} P_{l'}({\bf \hat x}\cdot{\bf \hat x}')
            {2k+1\over 4\pi} P_k({\bf \hat x}\cdot{\bf \hat x}')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\int
            {2l'+1\over 4\pi}
            {2k+1\over 4\pi}
            \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
                \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
                {4\pi \over 2\lambda+1}
                \sum_{\mu=-\lambda}^\lambda
                Y_{\lambda\mu}^*(\Omega')
                Y_{\lambda\mu}(\Omega)
            Y_{lm}(\Omega')
            \d \Omega' =

    =
            {2l'+1\over 4\pi}
            {2k+1\over 4\pi}
            \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
                \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
                {4\pi \over 2\lambda+1}
                \sum_{\mu=-\lambda}^\lambda
                Y_{\lambda\mu}(\Omega)
            \delta_{\lambda l}
            \delta_{\mu m}
            =

    =
            {2k+1\over 4\pi}
                \sqrt{2l'+1\over 2l+1} c^k(l', 0, l, 0)
                Y_{lm}(\Omega)


Where we used the following identities:

.. math::

    \sum_{m'}
        Y_{l'm'}(\Omega)
        Y_{l'm'}^*(\Omega')
    = {2l'+1\over 4\pi} P_{l'}({\bf \hat x}\cdot{\bf \hat x}')

    \sum_{q}
        Y_{kq}(\Omega)
        Y_{kq}^*(\Omega')
    = {2k+1\over 4\pi} P_k({\bf \hat x}\cdot{\bf \hat x}')

    P_k({\bf \hat x}\cdot{\bf \hat x}')P_{l'}({\bf \hat x}\cdot{\bf \hat x}')
    = \sum_{\lambda=|l'-k|}^{l'+k}
        \begin{pmatrix} k & l' & \lambda \\ 0 & 0 & 0 \end{pmatrix}^2
        (2\lambda+1) P_\lambda({\bf \hat x}\cdot{\bf \hat x}') =

        = \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
            \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
            P_\lambda({\bf \hat x}\cdot{\bf \hat x}') =

    = \sum_{\lambda=|l'-k|}^{\lambda=l'+k}
        \sqrt{2\lambda+1\over 2l'+1} c^k(l', 0, \lambda, 0)
        {4\pi \over 2\lambda+1}
        \sum_{\mu=-\lambda}^\lambda
        Y_{\lambda\mu}^*(\Omega')
        Y_{\lambda\mu}(\Omega)

Note: using the integral of 3 spherical harmonics directly in
:eq:`five_spherical_harmonics`:

.. math::

    \sum_{m'}\sum_{q}\int
            Y_{l'm'}(\Omega)
            Y_{l'm'}^*(\Omega')
            Y_{kq}(\Omega)
            Y_{kq}^*(\Omega')
            Y_{lm}(\Omega')
            \d \Omega' =

    =\sum_{m'}
            Y_{l'm'}(\Omega)
            Y_{k, m-m'}(\Omega)
            \sqrt{4\pi\over 2k+1}
            c^k(l, m, l', m')

doesn't straightforwardly lead to the final result, as it is not obvious how to
simplify things further.


Wigner 3j Symbols
-----------------

Relation between the Wigner $3j$ symbols and Clebsch-Gordan coefficients:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix}
        = {(-1)^{j_1-j_2-m_3}\over \sqrt{2j_3+1}}
            (j_1 m_1 j_2 m_2 | j_3 -m_3)

    (j_1 m_1 j_2 m_2 | j_3 m_3)
        = (-1)^{j_1-j_2+m_3}\sqrt{2j_3+1}
        \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & -m_3 \end{pmatrix}

They are nonzero only when:

.. math::

    m_1 + m_2 + m_3 = 0

    j_1+j_2+j_3 = \mbox{integer (or even integer if $m_1=m_2=m_3=0$)}

    |m_i| \le j_i

    |j_1-j_2| \le j_3 \le j_1+j_2

They have lots of symmetries. The $3j$ symbol is invariant for an even
permutation of columns:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = \begin{pmatrix} j_2 & j_3 & j_1 \\ m_2 & m_3 & m_1 \end{pmatrix} =

        = \begin{pmatrix} j_3 & j_1 & j_2 \\ m_3 & m_1 & m_2 \end{pmatrix}

For an odd permutation of columns it changes sign if $j_1+j_2+j+3$ is an odd
integer:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_2 & j_1 & j_3 \\ m_2 & m_1 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_1 & j_3 & j_2 \\ m_1 & m_3 & m_2 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_3 & j_2 & j_1 \\ m_3 & m_2 & m_1 \end{pmatrix}

and the same if you change the sign of the second row:

.. math::

    \begin{pmatrix} j_1 & j_2 & j_3 \\ m_1 & m_2 & m_3 \end{pmatrix} =

        = (-1)^{j_1+j_2+j_3}
        \begin{pmatrix} j_1 & j_2 & j_3 \\ -m_1 & -m_2 & -m_3 \end{pmatrix}

Orthogonality relations:

.. math::

    \sum_{m_1 m_2}
    \begin{pmatrix} j_1 & j_2 & j \\ m_1 & m_2 & m \end{pmatrix}
    \begin{pmatrix} j_1 & j_2 & j' \\ m_1 & m_2 & m' \end{pmatrix} =
        {\delta_{jj'}\delta_{mm'}
            \over
        2j+1}

As a special case, we get:

.. math::
    :label: 3j-square-sum

    \sum_{m'}
    \begin{pmatrix} l & k & l' \\ -m & m-m' & m' \end{pmatrix}^2
    =
        {1 \over 2l+1}

Here is a script to check that the equation :eq:`3j-square-sum` works:

.. raw:: latex

    {}

    \singlespacing

::

    from sympy import S
    from sympy.physics.wigner import wigner_3j

    def doit(l, k, lp, m):
        s = 0
        for mp in range(-lp, lp+1):
            s += wigner_3j(l, k, lp, -m, m-mp, mp)**2
        print "%2d %2d %2d %2d  " % (l, k, lp, m), s, " ", S(1)/(2*l+1)

    k = 4
    lp = 3
    print " l  k  lp m:  lhs   rhs"
    for l in range(1, 6):
        for m in range(-l, l+1):
            doit(l, k, lp, m)

.. raw:: latex

    \doublespacing

it prints:

.. raw:: latex

    {}

    \singlespacing

::

     l  k  lp m:  lhs   rhs
     1  4  3 -1   1/3   1/3
     1  4  3  0   1/3   1/3
     1  4  3  1   1/3   1/3
     2  4  3 -2   1/5   1/5
     2  4  3 -1   1/5   1/5
     2  4  3  0   1/5   1/5
     2  4  3  1   1/5   1/5
     2  4  3  2   1/5   1/5
     3  4  3 -3   1/7   1/7
     3  4  3 -2   1/7   1/7
     3  4  3 -1   1/7   1/7
     3  4  3  0   1/7   1/7
     3  4  3  1   1/7   1/7
     3  4  3  2   1/7   1/7
     3  4  3  3   1/7   1/7
     4  4  3 -4   1/9   1/9
     4  4  3 -3   1/9   1/9
     4  4  3 -2   1/9   1/9
     4  4  3 -1   1/9   1/9
     4  4  3  0   1/9   1/9
     4  4  3  1   1/9   1/9
     4  4  3  2   1/9   1/9
     4  4  3  3   1/9   1/9
     4  4  3  4   1/9   1/9
     5  4  3 -5   1/11   1/11
     5  4  3 -4   1/11   1/11
     5  4  3 -3   1/11   1/11
     5  4  3 -2   1/11   1/11
     5  4  3 -1   1/11   1/11
     5  4  3  0   1/11   1/11
     5  4  3  1   1/11   1/11
     5  4  3  2   1/11   1/11
     5  4  3  3   1/11   1/11
     5  4  3  4   1/11   1/11
     5  4  3  5   1/11   1/11

.. raw:: latex

    \doublespacing

Values of the $3j$ coefficients for a few special cases (use the symmetries
above to obtain values for permuted symbols):

.. math::

    \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}
        &= (-1)^s \sqrt{(2s-2k)! (2s-2l)! (2s-2m)! \over (2s+1)!} \times \\
        &\quad\quad\times
            {s! \over (s-k)! (s-l)! (s-m)!}
            \quad\quad\mbox{for $2s=k+l+m$ even} \\
    \begin{pmatrix} k & l & m \\ 0 & 0 & 0 \end{pmatrix}
        &= 0
            \quad\quad\mbox{for $2s=k+l+m$ odd} \\
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
        &= (-1)^{j-m-\half} \sqrt{j-m+\half
            \over (2j+1)(2j+2)} \\
    \begin{pmatrix} j+1 & j & 1 \\ m & -m-1 & 1 \end{pmatrix}
        &= (-1)^{j-m-1} \sqrt{(j-m)(j-m+1)
            \over (2j+1)(2j+2)(2j+3)} \\
    \begin{pmatrix} j+1 & j & 1 \\ m & -m & 0 \end{pmatrix}
        &= (-1)^{j-m-1} \sqrt{2(j+m+1)(j-m+1)
            \over (2j+1)(2j+2)(2j+3)}

Examples
~~~~~~~~

.. math::

    \begin{pmatrix} j_3-\half & \half & j_3 \\
        m_3-\half & \half & -m_3 \end{pmatrix} =
    \begin{pmatrix} j_3 & j_3-\half & \half \\
        -m_3 & m_3-\half & \half \end{pmatrix} =

    =
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3-\half;m=-m_3}
    =

    = (-1)^{j_3-\half+m_3-\half}\sqrt{j_3-\half+m_3+\half\over
        (2 j_3-1+1) (2j_3-1+2)}
    = (-1)^{j_3+m_3-1}\sqrt{j_3+m_3\over 2 j_3 (2j_3+1)}


.. math::


    \begin{pmatrix} j_3-\half & \half & j_3 \\
        m_3+\half & -\half & -m_3 \end{pmatrix} =
        (-1)^{j_3-\half + \half + j_3}
    \begin{pmatrix} j_3 & j_3-\half & \half \\
        m_3 & -m_3-\half & \half \end{pmatrix} =

    =
        (-1)^{2j_3}
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3-\half;m=m_3}
    =

    = (-1)^{2j_3}
    (-1)^{j_3-\half-m_3-\half}\sqrt{j_3-\half-m_3+\half\over
        (2 j_3-1+1) (2j_3-1+2)} =

    = (-1)^{2j_3} (-1)^{j_3-m_3-1}\sqrt{j_3-m_3\over 2 j_3 (2j_3+1)}


.. math::


    \begin{pmatrix} j_3+\half & \half & j_3 \\
        m_3-\half & \half & -m_3 \end{pmatrix} =
        (-1)^{j_3+\half+\half+j_3}
    \begin{pmatrix} j_3+\half & j_3 & \half \\
        m_3-\half & -m_3 & \half \end{pmatrix} =

    =
        (-1)^{2j_3+1}
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3;m=m_3-\half}
    =

    =(-1)^{2j_3+1}(-1)^{j_3-m_3+\half-\half}\sqrt{j_3-m_3+\half+\half \over
        (2j_3+1)(2j_3+2)} =

    =(-1)^{2j_3+1}(-1)^{j_3-m_3}\sqrt{j_3-m_3+1 \over (2j_3+1)(2j_3+2)}



.. math::


    \begin{pmatrix} j_3+\half & \half & j_3 \\
        m_3+\half & -\half & -m_3 \end{pmatrix} =
    \begin{pmatrix} j_3+\half & j_3 & \half \\
        -m_3-\half & m_3 & \half \end{pmatrix} =

    =
        \left.
    \begin{pmatrix} j+\half & j & \half \\ m & -m-\half & \half \end{pmatrix}
    \right|_{j=j_3;m=-m_3-\half}
    =

    =(-1)^{j_3+m_3+\half-\half}\sqrt{j_3+m_3+\half+\half \over
        (2j_3+1)(2j_3+2)}
    =(-1)^{j_3+m_3}\sqrt{j_3+m_3+1 \over (2j_3+1)(2j_3+2)}


Multipole Expansion
-------------------

Using :eq:`legendre_expansion` we get:

.. math::

    {1\over |{\bf r}-{\bf r'}|}
        =\sum_{l=0}^\infty{r_{<}^l\over r_{>}^{l+1}} P_l({\bf\hat r}\cdot {\bf\hat r'})
        = \sum_{l,m}{r_{<}^l\over r_{>}^{l+1}}
            {4\pi\over 2l+1}Y_{lm}({\bf\hat r})Y_{lm}^*({\bf\hat r}')

where we used the formula:

.. math::

    \sum_m \braket{{\bf\hat r}|lm}\braket{lm|{\bf\hat r}'}
        ={2l+1 \over 4\pi} \braket{{\bf\hat r}\cdot{\bf\hat r'}|P_l}

Robust, Accurate and Fast Evaluation of Modified Bessel Functions
-----------------------------------------------------------------

For the screened Hartree-Fock calculations we need Fortran routines for a fast
and robust evaluation of the modified Bessel functions. The following
implementation using rational approximation has proven to work well:

.. raw:: latex

    {}

    \singlespacing

::

    real(dp) function Inu(k, x) result(r)
    integer, intent(in) :: k
    real(dp), intent(in) :: x
    select case (k)
        case (0)
            ! r = sinh(x) / exp(x)
            if (x < 20) then
                r = sinh(x) / exp(x)
            else
                r = 1._dp / 2
            end if
        case (1)
            ! r = -sinh(x)/x + cosh(x)
            ! r = r * sqrt(2/(pi*x)) / exp(x)
            if (x < 0.55_dp) then
                r = x**2/3 + x**4/30 + x**6/840 + x**8/45360 + &
                    x**10/3991680 + &
                    x**12/518918400 + x**14/93405312e3_dp
                r = r / exp(x)
            else if (x < 2) then
                r = (-1.0118340437504393201742626606e-13_dp + &
                        x*(1.816670640113517482116741309e-12_dp + &
                        x*(0.333333333318047257036705475493_dp + &
                        x*(0.0283477684328350973136495456416_dp + &
                        x*(0.0236972901524850660936691284628_dp + &
                        x*(0.0018095002919993302530473889535_dp + &
                        x*(0.000376379638016770111327098946609_dp + &
                        (0.0000200246480593843172713997406232_dp + &
                    1.01338637272678665804111511983e-6_dp*x)*x)))))))/ &
                    (1 + x*(1.08504330505794283765963608202_dp + &
                        x*(0.556135176398351735247605123725_dp + &
                        x*(0.177204358493610809522295217793_dp + &
                        x*(0.0387591827785532218461461492913_dp + &
                        x*(0.00603331772767809320892209353842_dp + &
                        x*(0.000663930390602843320578606798458_dp + &
                        (0.0000484437498700383824299885362686_dp + &
                    1.88315077527785406856560709781e-6_dp*x)*x)))))))
            else if (x < 20) then
                r = (-sinh(x)/x + cosh(x)) / exp(x)
            else
                r = (-1/x + 1) / 2
            end if
        case (2)
            ! r = (3/x**2 + 1)*sinh(x) - 3/x*cosh(x)
            ! r = r * sqrt(2/(pi*x)) / exp(x)
            if (x < 0.4_dp) then
                r = x**3/15 + x**5/210 + x**7/7560 + x**9/498960 + &
                    x**11/51891840 + x**13/7783776e3_dp
                r = r / exp(x)
            else if (x < 3.5_dp) then
                r = (2.53492679940778614368716713944e-12_dp + &
                        x*(-4.54239143359406142775391525584e-11_dp + &
                        x*(3.74155600551604503226833667911e-10_dp + &
                        x*(0.0666666647818812413079530441494_dp + &
                        x*(0.00828258168209346350068333077357_dp + &
                        x*(0.00316314651226673854191486006661_dp + &
                        x*(0.000312916425508586674670599989463_dp + &
                        (0.0000347881775004914918533122949261_dp + &
                    1.78379773794153349607916665442e-6_dp*x)*x)))))))/ &
                    (1. + x*(1.12423862743404991052489502731_dp + &
                        x*(0.600257501089318988530867089925_dp + &
                        x*(0.20062393658095786500607161529_dp + &
                        x*(0.0464529738128345227818430451247_dp + &
                        x*(0.00775200781581904134897323422714_dp + &
                        x*(0.000932283869002308809130049094732_dp + &
                        (0.0000765450448110628850893821308195_dp + &
                    3.64978189893775492541031628736e-6_dp*x)*x)))))))
            else if (x < 8) then
                r = (-0.0500329770733375148059871692299_dp + &
                        x*(0.225443974816227263854027844348_dp + &
                        x*(-0.490706738714676572173733908052_dp + &
                        x*(0.754739228306267786750520915722_dp + &
                        x*(-0.0229222956512753039643375612586_dp + &
                        x*(0.0417199171935382735527783646423_dp + &
                        x*(0.00129242688582393560040014185308_dp + &
                        (0.000436655909016956929989211236885_dp + &
                  0.0000544588062620298286123134699247_dp*x)*x)))))))/ &
                    (1 + x*(11.1481461018360358000411784178_dp + &
                        x*(2.95111664564331863128521306942_dp + &
                        x*(2.07069035717497213861002964422_dp + &
                        x*(0.212130624675779325122087859297_dp + &
                        x*(0.0985267048591193186479900210954_dp + &
                        x*(0.00581026870781213052737501655128_dp + &
                        (0.00120128946303470807826705767304_dp + &
                    0.000108903528444754760503502120599_dp*x)*x)))))))
            else if (x < 20) then
                r = ((3/x**2 + 1)*sinh(x) - 3/x*cosh(x)) / exp(x)
            else
                r = (3/x**2 - 3/x + 1) / 2
            end if
        case (3)
            ! r = -(15/x**3 + 6/x)*sinh(x) + (15/x**2 + 1)*cosh(x)
            ! r = r / exp(x)
            if (x < 0.4_dp) then
                r = x**4/105 + x**6/1890 + x**8/83160 + x**10/6486480 +&
                    x**12/778377600 + x**14/132324192e3_dp
                r = r / exp(x)
            else if (x < 3) then
                r = (-3.70655078828583097759525479916e-13_dp + &
                        x*(7.15112302218910770115285755762e-12_dp + &
                        x*(-6.36681926888695741582309642988e-11_dp + &
                        x*(3.47928680854080370346525732791e-10_dp + &
                        x*(0.00952380821395522376879618243177_dp + &
                        x*(0.00113757240229334056047517957181_dp + &
                        x*(0.000297467643525496580117283299361_dp + &
                        (0.0000243340659637433371695954961197_dp + &
                    1.81721245776908511864649367981e-6_dp*x)*x)))))))/ &
                    (1 + x*(1.11944472257087316750869453522_dp + &
                        x*(0.595124068593635706143579962619_dp + &
                        x*(0.197986316667328417652509149837_dp + &
                        x*(0.0456127952595471262482188760838_dp + &
                        x*(0.00757090880409778905789353557549_dp + &
                        x*(0.000905726554901565254770825575224_dp + &
                        (0.0000739095656995355486962496918923_dp + &
                    3.54519707102049776194411547746e-6_dp*x)*x)))))))
            else if (x < 8.5_dp) then
                r = (0.00117649571172537032041386386937_dp + &
                        x*(-0.00530534669296740084953876529485_dp + &
                        x*(0.0113989437968364216304855248904_dp + &
                        x*(-0.0155143209720413375494757271933_dp + &
                        x*(0.0245092943569822333734792982989_dp + &
                        x*(-0.00194266321525633715561142461716_dp + &
                        x*(0.00125839658564675731614612557048_dp + &
                        (-0.0000560593512807954817946224257333_dp + &
                  0.0000154307073445195296381347198964_dp*x)*x)))))))/ &
                    (1 + x*(1.93920721196223643040357762209_dp + &
                        x*(0.871960706430017695531414950855_dp + &
                        x*(0.294335907964445235622348955601_dp + &
                        x*(0.076510324944994462960832902772_dp + &
                        x*(0.0103358291871056058873144950985_dp + &
                        x*(0.00249717323564249173430366673788_dp + &
                        (0.0000729070672630135675918235119142_dp + &
                    0.0000308632011694791287440146822781_dp*x)*x)))))))
            else if (x < 20) then
                r = (-(15/x**3 + 6/x)*sinh(x) + &
                    (15/x**2 + 1)*cosh(x)) / exp(x)
            else
                r = (-15/x**3 + 15/x**2 - 6/x  + 1)/2
            end if
        case (4)
            ! r = (105/x**4 + 45/x**2 + 1)*sinh(x) &
                    - (105/x**3 + 10/x)*cosh(x)
            ! r = r / exp(x)
            if (x < 0.2_dp) then
                r = x**5/945 + x**7/20790 + x**9/1081080 + &
                        x**11/97297200 + x**13/132324192e2_dp
                r = r / exp(x)
            else if (x < 1.7_dp) then
                r = (8.24833340467311342180121686171e-18_dp + &
                    x*(-2.9977388208095462038421382427e-16_dp + &
                    x*(4.98591599598783667120520966419e-15_dp + &
                    x*(-5.04172127797261339201651796769e-14_dp + &
                    x*(3.47424275623446932695212209666e-13_dp + &
                    x*(0.00105820105646713443251629043736_dp + &
                    x*(0.0000979757728258499019673125884795_dp + &
                    (0.0000182024072642408317859820498652_dp + &
                    1.0631472458547091790087783848e-6_dp*x)*x))))))) / &
                (1 + x*(1.09258709917337245791086210753_dp + &
                    x*(0.564333846348740813775052159905_dp + &
                    x*(0.181503092836557003863165983269_dp + &
                    x*(0.040177538019272720474585552471_dp + &
                    x*(0.00635509731709913059075978583153_dp + &
                    x*(0.000715397138065847382814527384553_dp + &
                    (0.0000540407967369787069953788458276_dp + &
                    2.26320060646140077482435126776e-6_dp*x)*x)))))))
            else if (x < 4) then
                r = (-1.79380868029518008655845945341e-7_dp + &
                    x*(1.42021959889593932447404701528e-6_dp + &
                    x*(-5.3621673060507414018999203431e-6_dp + &
                    x*(0.0000128612071905009120973461141937_dp + &
                    x*(-0.0000220283666472339963720124703845_dp + &
                    x*(0.00108692026226442881323459546524_dp + &
                    x*(-0.000108914780493366312610770062505_dp + &
                    (0.0000213026860907556990203197490202_dp - &
                    2.40044294668610963152692356425e-6_dp*x)*x))))))) /&
                (1 + x*(0.92511576565864173804826819565_dp + &
                    x*(0.376185570863101848786874779376_dp + &
                    x*(0.0979599622990753625780606726782_dp + &
                    x*(0.0139543384283183184757129378369_dp + &
                    x*(0.00167710554949622675142353677903_dp + &
                    x*(-0.0000841270733243543647065400772874_dp + &
                    (-4.04735930419963375054951672688e-6_dp - &
                    4.82907242383463140296057166244e-6_dp*x)*x)))))))
            else if (x < 10) then
                r = (0.000395502959013236968661582656143_dp + &
                    x*(-0.001434648369704841686633794071_dp + &
                    x*(0.00248783474583503473135143644434_dp + &
                    x*(-0.00274477921388295929464613063609_dp + &
                    x*(0.00216275018107657273725589740499_dp + &
                    x*(-0.000236779926184242197820134964535_dp + &
                    x*(0.0000882030507076791807159699814428_dp + &
                    (-4.62078105288798755556136693122e-6_dp + &
                    8.23671374777791529292655504214e-7_dp*x)*x))))))) /&
                (1 + x*(0.504839286873735708062045336271_dp + &
                    x*(0.176683950009401712892997268723_dp + &
                    x*(0.0438594911840609324095487447279_dp + &
                    x*(0.00829753062428409331123592322788_dp + &
                    x*(0.00111693697900468156881720995034_dp + &
                    x*(0.000174719963536517752971223459247_dp + &
                    (7.22885338737473776714257581233e-6_dp + &
                    1.64737453771748367647332279826e-6_dp*x)*x)))))))
            else if (x < 20) then
                r = (1.49435717183021678294278540018_dp + &
                    x*(-1.9954827594990599398954087063_dp + &
                    x*(1.19185825369343226912112655137_dp + &
                    x*(-0.40866680980235804096143699423_dp + &
                    x*(0.0852839860059780325406440673318_dp + &
                    (-0.00980617919194154929317057489645_dp + &
                    0.000550291361244287676343295379476_dp*x)*x)))))/&
                (1 + x*(0.420439518058743727857466136746_dp + &
                    x*(0.144024726914933127664739439568_dp + &
                    x*(0.035261250406130055921113600336_dp + &
                    x*(0.0349770458351085078647522073879_dp + &
                    (-0.00860653991097136433951965579037_dp + &
                    0.00110058277850687516223459976889_dp*x)*x)))))
            else
                r = (105/x**4 - 105/x**3 + 45/x**2 - 10/x + 1)/2
            end if
        case default
            r = -1 ! For compiler warning "fix"
            call stop_error("k = " // str(k) // " not implemented.")
    end select
    r = r * sqrt(2/(pi*x))
    end function

    real(dp) function Knu(k, x) result(r)
    integer, intent(in) :: k
    real(dp), intent(in) :: x
    select case (k)
        case (0)
            r = 1
        case (1)
            r = 1/x + 1
        case (2)
            r = 3/x**2 + 3/x + 1
        case (3)
            r = 15/x**3 + 15/x**2 + 6/x + 1
        case (4)
            r = 105/x**4 + 105/x**3 + 45/x**2 + 10/x + 1
        case default
            call stop_error("k = " // str(k) // " not implemented.")
    end select
    r = r * sqrt(pi/(2*x))
    end function

.. raw:: latex

    \doublespacing


These routines were tested against arbitrary precision implementation in SymPy
:cite:`SymPy`, the results are in Figures
:num:`bessel0`,
:num:`bessel1`,
:num:`bessel2`,
:num:`bessel3`,
:num:`bessel4`.

.. _bessel0:

.. figure:: ../figures/error0.*

    The convergence of modified Bessel function for k=0

.. _bessel1:

.. figure:: ../figures/error1.*

    The convergence of modified Bessel function for k=1

.. _bessel2:

.. figure:: ../figures/error2.*

    The convergence of modified Bessel function for k=2

.. _bessel3:

.. figure:: ../figures/error3.*

    The convergence of modified Bessel function for k=3

.. _bessel4:

.. figure:: ../figures/error4.*

    The convergence of modified Bessel function for k=4
