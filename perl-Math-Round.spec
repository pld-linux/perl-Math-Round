#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Math
%define	pnam	Round
Summary:	Math::Round - Perl extension for rounding numbers
Summary(pl.UTF-8):	Math::Round - perlowe rozszerzenie do zaokrąglania liczb
Name:		perl-Math-Round
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	b74c5d2a3f891c19dafd7ce638732fd1
URL:		http://search.cpan.org/dist/Math-Round/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Math::Round supplies functions that will round numbers in different
ways. The functions round and nearest are exported by default; others
are available as described in the manual. "use ... qw(:all)" exports
all functions.

%description -l pl.UTF-8
Math::Round udostępnia funkcje zaokrąglające liczby w różny sposób.
Funkcje round i nearest są eksportowane domyślnie; inne są dostępne w
sposób opisany w manualu. "use ... qw(:all)" eksportuje wszystkie
funkcje.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Math/Round.pm
%dir %{perl_vendorlib}/auto/Math/Round
%{perl_vendorlib}/auto/Math/Round/autosplit.ix
%{_mandir}/man3/Math::Round.3pm*
