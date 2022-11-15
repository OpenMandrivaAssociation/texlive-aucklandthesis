Name:		texlive-aucklandthesis
Version:	51323
Release:	1
Summary:	Memoir-based class for formatting University of Auckland masters' and doctors' theses
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/aucklandthesis
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aucklandthesis.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/aucklandthesis.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A memoir-based class for formatting University of Auckland
masters' and doctors' thesis dissertations in any discipline.
The title page does not handle short dissertations for
diplomas.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/aucklandthesis
%doc %{_texmfdistdir}/doc/latex/aucklandthesis

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
