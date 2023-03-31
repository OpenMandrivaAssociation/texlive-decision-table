Name:		texlive-decision-table
Version:	60673
Release:	2
Summary:	An easy way to create Decision Model and Notation decision tables
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/decision-table
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decision-table.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decision-table.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decision-table.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The decision-table package allows for an easy way to generate
decision tables in the Decision Model and Notation (DMN)
format. This package ensures consistency in the tables (i.e.
fontsize), and is thus a better alternative to inserting tables
via images. The decision-table package adds the \dmntable
command, with which tables can be created. This command expands
into a tabular, so it can be used within a table or figure
environment. Furthermore, this allows labels and captions to be
added seamlessly. It is also possible to place multiple DMN
tables in one table/figure environment. The package relies on
nicematrix and l3keys2e.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/decision-table
%{_texmfdistdir}/tex/latex/decision-table
%doc %{_texmfdistdir}/doc/latex/decision-table

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
