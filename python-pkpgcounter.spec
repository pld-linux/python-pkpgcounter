%define		module	pkpgcounter

Summary:	Page Description Language parser
Summary(pl.UTF-8):	Analizator języka opisu strony
Name:		python-%{module}
Version:	3.50
Release:	4
License:	LGPL
Group:		Development/Languages/Python
Source0:	http://www.pykota.com/software/pkpgcounter/download/tarballs/%{module}-%{version}.tar.gz
# Source0-md5:	564dd96e8a5433564c2e39319e65217e
Patch0:		pkpgcounter-postscript-multiple-copies.patch
Patch1:		pkpgcounter-stdin-noargs.patch
URL:		http://www.pykota.com/software/pkpgcounter/
BuildRequires:	python >= 1:2.5
BuildRequires:	python-devel >= 1:2.5
BuildRequires:	python-PIL
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
pkpgcounter is a generic Page Description Language parser which
can either count the number of pages or compute the percent of
ink coverage needed to print various types of documents.

%description -l pl.UTF-8
pkpgcounter jest ogólnym analizatorem języka opisu strony, który
potrafi policzyć liczbę stron albo procentowe pokrycie atramentem
potrzebne do wydrukowania różnych typów dokumentów.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p1
%patch1 -p1

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

%{__python} setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_postclean

# we already have these files in %doc
rm -fr $RPM_BUILD_ROOT%{_docdir}/%{module}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc BUGS CREDITS NEWS README
%attr(755,root,root) %{_bindir}/pkpgcounter
%dir %{py_sitescriptdir}/pkpgpdls
%{py_sitescriptdir}/pkpgpdls/*.py[co]
%{py_sitescriptdir}/*.egg-info
%{_mandir}/man1/pkpgcounter.1*
