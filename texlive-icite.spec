Name:		texlive-icite
Version:	54512
Release:	1
Summary:	Indices locorum citatorum
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/icite
License:	gpl3+ cc-by-sa-4
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/icite.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package is designed to produce from BibTeX or BibLaTeX
bibliographical databases the different indices of authors and
works cited which are called indices locorum citatorum. It
relies on a specific \icite command and can operate with either
BibTeX or BibLaTeX.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/icite
%{_texmfdistdir}/tex/latex/icite
%doc %{_texmfdistdir}/doc/latex/icite

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
