Summary:	Tetum dictionary for aspell
Summary(pl):	S³ownik tetum dla aspella
Name:		aspell-tet
Version:	0.1.1
#%%define	subv	0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/tet/aspell5-tet-%{version}.tar.bz2
# Source0-md5:	6a18e0253d7d6baa49daca513b0d782b
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 0.50.0
Requires:	aspell >= 0.50.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tetum dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik tetum (lista s³ów) dla aspella.

%prep
%setup -q -n aspell5-tet-%{version}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
