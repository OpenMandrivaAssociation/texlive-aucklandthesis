%global tl_name aucklandthesis
%global tl_revision 51323

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Memoir-based class for formatting University of Auckland masters and doctors ...
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/aucklandthesis
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aucklandthesis.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/aucklandthesis.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
Requires(pre):	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A memoir-based class for formatting University of Auckland masters' and
doctors' thesis dissertations in any discipline. The title page does not
handle short dissertations for diplomas.

%prep
%setup -q -c -a1
rm -rf tlpkg
if [ -d RELOC ]; then
	cp -a RELOC/. .
	rm -rf RELOC
fi

%build

%install
mkdir -p %{buildroot}%{_datadir}/texmf-dist
# Flat tlnet layout: tex/ doc/ source/ fonts/ ... -> texmf-dist/
if [ -d texmf-dist ]; then
	cp -a texmf-dist/. %{buildroot}%{_datadir}/texmf-dist/
elif [ -d texmf ]; then
	mkdir -p %{buildroot}%{_datadir}/texmf
	cp -a texmf/. %{buildroot}%{_datadir}/texmf/
else
	for d in * .[!.]* ..?*; do
		[ -e "$d" ] || continue
		case "$d" in tlpkg|RELOC) continue ;; esac
		cp -a "$d" %{buildroot}%{_datadir}/texmf-dist/
	done
fi
rm -rf %{buildroot}%{_datadir}/texmf-dist/tlpkg

%files
%dir %{_datadir}/texmf-dist
%dir %{_datadir}/texmf-dist/doc
%dir %{_datadir}/texmf-dist/tex
%dir %{_datadir}/texmf-dist/doc/latex
%dir %{_datadir}/texmf-dist/tex/latex
%dir %{_datadir}/texmf-dist/doc/latex/aucklandthesis
%dir %{_datadir}/texmf-dist/tex/latex/aucklandthesis
%doc %{_datadir}/texmf-dist/doc/latex/aucklandthesis/README.TEXLIVE
%doc %{_datadir}/texmf-dist/doc/latex/aucklandthesis/README.txt
%doc %{_datadir}/texmf-dist/doc/latex/aucklandthesis/template.tex
%{_datadir}/texmf-dist/tex/latex/aucklandthesis/aucklandthesis.cls
