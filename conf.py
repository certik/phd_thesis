# -*- coding: utf-8 -*-
#
# phd_thesis documentation build configuration file, created by
# sphinx-quickstart on Sat Sep 22 17:02:23 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))
sys.path.append(os.path.abspath('exts'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath', "math_dollar", "numfig", "figtable",
        "sphinxcontrib.bibtex"]

initial_pages = r"""

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Title Page

\begin{center}
University of Nevada, Reno

\vfill

{\Large \bf Physics in Screening Environments}\\

\vfill

A dissertation submitted in partial fulfillment of the\\
requirements for the degree of Doctor of Philosophy in\\
Chemical Physics

\vfill

by

\vspace{0.5in}

Ond\v rej \v Cert\' ik

\vspace{0.5in}

Dr. Peter Winkler, Dissertation Advisor

\vspace{0.5in}

December 2012
\end{center}
\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Copyright Notice

\vspace*{\fill}
\begin{center}
Copyright by Ond\v rej \v Cert\' ik 2012\\
All Rights Reserved
\end{center}
\vspace*{\fill}

\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Committee Approval Page

\baselineskip=26pt
\newpage

\begin{center}
{\Large \bf THE GRADUATE SCHOOL}
\vspace*{0.5in}
\vspace*{\fill}

We recommend that the dissertation \\
prepared under our supervision by \\

\vspace*{\fill}

{\bf Ond\v rej \v Cert\' ik}

\vspace*{\fill}

entitled

\vspace*{\fill}

{\bf Physics in Screening Environments}

\vspace*{\fill}

be accepted in partial fulfillment of the \\
requirements for the degree of

\vspace*{\fill}

{\bf DOCTOR OF PHILOSOPHY}

\vspace*{\fill}
\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
Peter Winkler, Ph.D., Advisor

\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
David M. Leitner, Ph.D., Committee Member

\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
Yasuhiko Sentoku, Ph.D., Committee Member

\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
Sergey A. Varganov, Ph.D., Committee Member

\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
Karen Spears, Ph.D., Graduate School Representative

\vspace*{\fill}

\underline{\hspace{5in}} \\
\vspace{-10pt}
Marsha H. Read, Ph.D., Associate Dean, Graduate School


\vspace*{\fill}

December 2012

\vspace*{\fill}

\vspace*{\fill}
\end{center}

\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Abstract

\setcounter{page}{1}
\pagestyle{normal}

\vbox{
\addcontentsline{toc}{chapter}{Abstract}
\begin{center}
{\bf Abstract}
\end{center}

In the current study, we investigated atoms in screening environments like
plasmas.

It is common practice to extract physical data, such as temperature and
electron densities, from plasma experiments. We present results that address
inherent computational difficulties that arise when the screening approach is
extended to include the interaction between the atomic electrons. We show that
there may arise an ambiguity in the interpretation of physical properties, such
as
temperature and charge density, from experimental data due to the opposing
effects of electron-nucleus screening and electron-electron screening.

The focus of the work, however, is on the resolution of inherent computational
challenges that appear in the computation of two-particle matrix elements.
Those enter already at the Hartree-Fock level. Furthermore, as
examples of post Hartree-Fock calculations, we show second-order Green's
function results and many body perturbation theory results of second order.

A self-contained derivation of all necessary equations has been included.  The
accuracy of the implementation of the method is established by comparing
standard unscreened results for various atoms and molecules against literature
for Hartree-Fock as well as Green's function and many body perturbation
theory.

The main results of the thesis are presented in the chapter called Screened
Results, where the behavior of several atomic systems depending on
electron-electron and electron-nucleus Debye screening was studied.
The computer code that we have developed has been made available for anybody to
use.

Finally, we present and discuss results obtained for screened interactions. We
also examine thoroughly the computational details of the calculations and
particular implementations of the method.
}

\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Acknowledgments

\addcontentsline{toc}{chapter}{Acknowledgments}
\begin{center}
{\bf Acknowledgments}
\end{center}


I would like to thank my Ph.D. advisor Dr. Peter Winkler, for all the time that
he has devoted to me, teaching me atomic physics and guiding me through my
Ph.D studies.

I thank my Ph.D. committee members Dr. David M. Leitner, Dr. Yasuhiko Sentoku,
Dr. Karen Spears and Dr. Sergey A. Varganov, for their support and always being
ready to help. I
thank Dr. Sergey A. Varganov for all the discussions and explaining to me many
methods in quantum chemistry, pointing me to relevant literature and serving on
my committee.  I also wish to thank
Dr. Joseph I. Cline for initially serving on my committee and helping me with
administrative and other issues. I am indebted to Dr. Pavel \v Sol\' in for
inviting me to Reno, his time and his help getting me integrated in the USA, as
well as serving on my committee for two years. I wish to thank Dr. Bernhard
Bach for helping me with teaching labs as well as explaining many physics
topics. I would like to thank my former advisors and friends Dr. Ji\v r\'i
Vack\'a\v r, Dr. Ji\v r\'i Ple\v sek, Dr. Fernando Perez, Dr. Brian Granger and
Dr. Anton\'in Fejfar for their help and encouragement.

I thank Dr. John. E. Pask for being my advisor at the Lawrence
Livermore National Laboratory, teaching me finite element method for electronic
structure calculations as well as introducing me to modern Fortran and his
continuous help through my Ph.D. studies. John has provided many useful
suggestions for improving the thesis as well.

Most importantly I would like to thank my wife Michelle for her relentless and
patient support during all the late nights that I worked on my Ph.D., her
encouragement as well as proofreading.

\newpage

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% TOC

\cleardoublepage
\phantomsection
\renewcommand{\contentsname}{Table of Contents}
\addcontentsline{toc}{chapter}{Table of Contents}
\tableofcontents

\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{List of Tables}
\listoftables

\cleardoublepage
\phantomsection
\addcontentsline{toc}{chapter}{List of Figures}
\listoffigures

\pagebreak

\pagenumbering{arabic}
"""

_latex_preamble = r"""
\usepackage{dsfont}
\usepackage{braket}
\usepackage{slashed}
\usepackage{yfonts}
\usepackage{mathrsfs}
\def\degrees{^\circ}
\def\d{{\rm d}}

\def\sign{\mathop{\mathrm{sign}}}
\def\L{{\mathcal L}}
\def\H{{\mathcal H}}
\def\M{{\mathcal M}}
\def\matrix{}
\def\fslash#1{#1 \!\!\!/}
\def\F{{\bf F}}
\def\R{{\bf R}}
\def\J{{\bf J}}
\def\x{{\bf x}}
\def\y{{\bf y}}
\def\h{{\rm h}}
\def\a{{\rm a}}
\newcommand{\bfx}{\mbox{\boldmath $x$}}
\newcommand{\bfy}{\mbox{\boldmath $y$}}
\newcommand{\bfz}{\mbox{\boldmath $z$}}
\newcommand{\bfv}{\mbox{\boldmath $v$}}
\newcommand{\bfu}{\mbox{\boldmath $u$}}
\newcommand{\bfF}{\mbox{\boldmath $F$}}
\newcommand{\bfJ}{\mbox{\boldmath $J$}}
\newcommand{\bfU}{\mbox{\boldmath $U$}}
\newcommand{\bfY}{\mbox{\boldmath $Y$}}
\newcommand{\bfR}{\mbox{\boldmath $R$}}
\newcommand{\bfg}{\mbox{\boldmath $g$}}
\newcommand{\bfc}{\mbox{\boldmath $c$}}
\newcommand{\bfxi}{\mbox{\boldmath $\xi$}}


%\def\back{\!\!\!\!\!\!\!\!\!\!}
\def\back{}
\def\col#1#2{\left(\matrix{#1#2}\right)}
\def\row#1#2{\left(\matrix{#1#2}\right)}
\def\mat#1{\begin{pmatrix}#1\end{pmatrix}}
\def\matd#1#2{\left(\matrix{#1\back0\cr0\back#2}\right)}
\def\p#1#2{{\partial#1\over\partial#2}}
\def\cg#1#2#3#4#5#6{({#1},\,{#2},\,{#3},\,{#4}\,|\,{#5},\,{#6})}
\def\half{{\textstyle{1\over2}}}
\def\jsym#1#2#3#4#5#6{\left\{\matrix{
{#1}{#2}{#3}
{#4}{#5}{#6}
}\right\}}
\def\diag{\hbox{diag}}

\font\dsrom=dsrom10
\def\one{\hbox{\dsrom 1}}

\def\res{\mathop{\mathrm{Res}}}

\def\mathnot#1{\text{"$#1$"}}


%See Character Table for cmmib10:
%http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/cmmib10/cmmib10.html
\font\mib=cmmib10
\def\balpha{\hbox{\mib\char"0B}}
\def\bbeta{\hbox{\mib\char"0C}}
\def\bgamma{\hbox{\mib\char"0D}}
\def\bdelta{\hbox{\mib\char"0E}}
\def\bepsilon{\hbox{\mib\char"0F}}
\def\bzeta{\hbox{\mib\char"10}}
\def\boldeta{\hbox{\mib\char"11}}
\def\btheta{\hbox{\mib\char"12}}
\def\biota{\hbox{\mib\char"13}}
\def\bkappa{\hbox{\mib\char"14}}
\def\blambda{\hbox{\mib\char"15}}
\def\bmu{\hbox{\mib\char"16}}
\def\bnu{\hbox{\mib\char"17}}
\def\bxi{\hbox{\mib\char"18}}
\def\bpi{\hbox{\mib\char"19}}
\def\brho{\hbox{\mib\char"1A}}
\def\bsigma{\hbox{\mib\char"1B}}
\def\btau{\hbox{\mib\char"1C}}
\def\bupsilon{\hbox{\mib\char"1D}}
\def\bphi{\hbox{\mib\char"1E}}
\def\bchi{\hbox{\mib\char"1F}}
\def\bpsi{\hbox{\mib\char"20}}
\def\bomega{\hbox{\mib\char"21}}

\def\bvarepsilon{\hbox{\mib\char"22}}
\def\bvartheta{\hbox{\mib\char"23}}
\def\bvarpi{\hbox{\mib\char"24}}
\def\bvarrho{\hbox{\mib\char"25}}
\def\bvarphi{\hbox{\mib\char"27}}

%how to use:
%$$\alpha\balpha$$
%$$\beta\bbeta$$
%$$\gamma\bgamma$$
%$$\delta\bdelta$$
%$$\epsilon\bepsilon$$
%$$\zeta\bzeta$$
%$$\eta\boldeta$$
%$$\theta\btheta$$
%$$\iota\biota$$
%$$\kappa\bkappa$$
%$$\lambda\blambda$$
%$$\mu\bmu$$
%$$\nu\bnu$$
%$$\xi\bxi$$
%$$\pi\bpi$$
%$$\rho\brho$$
%$$\sigma\bsigma$$
%$$\tau\btau$$
%$$\upsilon\bupsilon$$
%$$\phi\bphi$$
%$$\chi\bchi$$
%$$\psi\bpsi$$
%$$\omega\bomega$$
%
%$$\varepsilon\bvarepsilon$$
%$$\vartheta\bvartheta$$
%$$\varpi\bvarpi$$
%$$\varrho\bvarrho$$
%$$\varphi\bvarphi$$

%small font
\font\mibsmall=cmmib7
\def\bsigmasmall{\hbox{\mibsmall\char"1B}}

\def\Tr{\hbox{Tr}\,}
\def\Arg{\hbox{Arg}}
\def\atan{\hbox{atan}}

% The lines below redefine the default values from sphinx.sty

% Redefine Sphinx colors
\definecolor{TitleColor}{rgb}{0.0,0.0,0.0}
\definecolor{InnerLinkColor}{rgb}{0.0,0.0,0.0}
\definecolor{OuterLinkColor}{rgb}{0.216,0.439,0.388}


% Header and Footer
\fancypagestyle{normal}{
    \fancyhf{}
    \fancyhead[R]{{\thepage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}
\fancypagestyle{plain}{
    \fancyhf{}
    \fancyhead[R]{{\thepage}}
    \renewcommand{\headrulewidth}{0pt}
    \renewcommand{\footrulewidth}{0pt}
}


\usepackage[top=1in, bottom=1.25in, left=1.5in, right=1in]{geometry}



% This redefines sphinxmanual.cls
% Table of Contents; restore previous behavior of "\tableofcontents":
\makeatletter
\renewcommand{\tableofcontents}{\py@OldTableofcontents}
\makeatother
\setcounter{tocdepth}{3}


% Other

% spacing
\usepackage{setspace}
\doublespacing

% Format Table of Figures
\usepackage{tocloft}
\renewcommand{\cftfigpresnum}{Figure~}
\renewcommand{\cfttabpresnum}{Table~}
\newlength{\mylenf}
\settowidth{\mylenf}{\cftfigpresnum}
\setlength{\cftfignumwidth}{\dimexpr\mylenf+1.5em}
\setlength{\cfttabnumwidth}{\dimexpr\mylenf+1.5em}
"""

pngmath_latex_preamble = _latex_preamble

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'phd_thesis'
copyright = u'2012, Ondřej Čertík'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = '0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'phd_thesisdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

# Additional stuff for the LaTeX preamble.
'preamble': _latex_preamble,

'fncychap': '',

# A hack to add the "oneside" option:
'classoptions': ',english,oneside,openany',

'maketitle': '',

'tableofcontents' : initial_pages,

'pointsize': '12pt',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'phd_thesis.tex', u'Ph.D. Dissertation',
   u'Ondřej Čertík', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
#latex_logo = None

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'phd_thesis', u'phd_thesis Documentation',
     [u'Ondřej Čertík'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'phd_thesis', u'phd_thesis Documentation', u'Ondřej Čertík',
   'phd_thesis', 'One line description of project.', 'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'