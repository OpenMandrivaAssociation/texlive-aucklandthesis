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
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A memoir-based class for formatting University of Auckland masters' and
doctors' thesis dissertations in any discipline. The title page does not
handle short dissertations for diplomas.

