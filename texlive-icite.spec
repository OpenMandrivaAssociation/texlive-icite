%global tl_name icite
%global tl_revision 67201

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.3a
Release:	%{tl_revision}.1
Summary:	Indices locorum citatorum
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/icite
License:	gpl3+ cc-by-sa-4
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package is designed to produce from BibTeX or BibLaTeX
bibliographical databases the different indices of authors and works
cited which are called indices locorum citatorum. It relies on a
specific \icite command and can operate with either BibTeX or BibLaTeX.

