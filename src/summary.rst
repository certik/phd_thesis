Summary and Conclusions
=======================

We chose radium as a benchmark for our Hartree-Fock (HF) code, because it
requires Slater integrals up to $k=6$ and has non zero occupation numbers up to
$l=3$.  By comparing the total energy with :cite:`Koga2000` for the same Slater
Type Orbital (STO) basis, and agreeing to 14 significant digits (all digits
given in :cite:`Koga2000`), means that our Hartree-Fock and STO code works well.
By using the finite element (FE) basis, we get the converged value which agrees
exactly with :cite:`Koga1996` (10 significant digits), and from the
$p$-convergence graph it suggests that our FE total energy is actually correct
to $10^{-8}\rm,a.u.$ (13 significant digits).  This establishes that our FE
basis works correctly as well.

The STO basis is highly efficient, for example for Ra one can get $10^{-4}$
accuracy with only 42 degrees of freedom. One has to optimize the basis for
each atom separately, one cannot reuse the basis directly, for example the
basis for radium is less accurate if used for Ne as established in the section
Unscreened Results. However, when an optimized basis is used for Ne, it
provides better accuracy with fewer basis functions.

The very same basis is less accurate for Ne. The disadvantage of the STO basis
is that it is not straightforward to improve the accuracy -- one has to add
more functions to the basis and optimize the exponents.

The efficiency of the FE basis, on the other hand, is determined by the choice
of a mesh. Once the mesh is fixed, then the systematic, robust and variational
way to improve the accuracy is just to increase the polynomial order. An
exponential mesh with the mesh parameter $a=200$ and polynomial order $p=20$
allows to get accuracy $10^{-6}$ for all atoms up to radium.

The traditional FE approach is to solve the Poisson problem by solving the
differential equation and the exchange term by calculating the integrals on the
fly. As shown above, this approach is equivalent to first calculating all two
particle integrals, and then solving the Roothaan equations.

The even-tempered STO basis for Mg shows nicely that the virial theorem cannot
always be trusted as an error indicator, because it only provides the lower
bound on the actual error of the total energy. In that example for DOF=15, the
virial theorem gives almost $10^{-8}$ accuracy, while the actual error is
$10^{-4}$. As such, the only reliable way to asses the accuracy is to do a
convergence study. Other possible error indicators that may provide information
about the quality of the wavefunctions (and ultimately the basis) include the
cusp condition and various sum rules like the Thomas-Reiche-Kuhn sum rule.

By properly updating the $\alpha$ and $\beta$ coefficients as increasing the
number ($N$) of basis functions, one can converge to the exact HF solution.
The convergence rate is exponential. The only practical disadvantage is that
the overlap matrix eventually becomes ill-conditioned for high $N$, preventing
the self-consistency cycle to converge. The FE approach does not suffer from
ill-conditioning.

We use STO basis that is optimized for unscreened (Coulomb) potential. More
thorough study would be needed to reoptimize the basis for the given Debye
screening. The virial theorem in the presence of screening takes a more
complicated form than just a simple sum of kinetic and total energy. The best
way to judge the accuracy of results is to perform a convergence with respect
to the STO basis, for example using the even-tempered basis set.

As a few examples of post-HF calculations, we show results for Green's function
and many body perturbation theory in second order. Other common post
Hartree-Fock methods include configuration interaction and coupled cluster.
The unscreened results can be directly compared to literature and the energies
are in good agreement, thus establishing that our implementation is correct.

In the screened results, we concentrate on the HF level of theory.  We ran
various calculations for He and Mg as well as $H^-$.  As an example of a
post-HF calculation, we show screened second order Green's function
calculations for He and Mg. We also compare our Hartree-Fock $H^-$ results with
a correlated wave function approach and as seen from the behavior of energies
as we decrease the Debye length, both set of energies follow the same trend.

The computational methods we have presented in this thesis are developed to the
point where one can include essentially any screening potential and are
accurate enough to distinguish between results and help resolve possible
ambiguities in the interpretation of plasma data.
