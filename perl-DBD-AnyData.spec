#
# Conditional build:
%bcond_without	tests	# don't perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	AnyData
Summary:	DBD::AnyData - DBI access to XML, CSV and other formats
Summary(pl):	DBD::AnyData - dostêp DBI do XML-a, CSV i innych formatów
Name:		perl-DBD-AnyData
Version:	0.06
Release:	1
# same as perl
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0d1867fe1fe256a184a39be45ca0a413
%if %{with tests}
BuildRequires:	perl-AnyData
BuildRequires:	perl-CGI
BuildRequires:	perl-DBD-CSV
# HTML and XML tests currently disabled
#BuildRequires:	perl-HTML-Parser
#BuildRequires:	perl-HTML-TableExtract
#BuildRequires:	perl-XML-Parser
#BuildRequires:	perl-XML-Twig
%endif
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DBD::AnyData module provides a DBI/SQL interface to data in many
formats and from many sources.

Currently supported formats include general format flatfiles (CSV,
Fixed Length, Tab or Pipe "delimited", etc.), specific formats (passwd
files, web logs, etc.), a variety of other kinds of formats (XML, Mp3,
HTML tables), and, for some operations, any DBI accessible database.

%description -l pl
Modu³ DBD::AnyData udostêpnia interfejs DBI/SQL do danych w wielu
formatach, pobieranych z wielu ¼róde³. Aktualnie obs³ugiwane formaty
zawieraj± ogólne sformatowane pliki (CSV, z polami o sta³ej d³ugo¶ci,
oddzielonymi tabami lub znakiem |, itp.), okre¶lone formaty (pliki
passwd, logi serwera WWW itp.), wiele innych rodzajów formatów (XML,
mp3, tabele HTML) oraz, dla niektórych operacji, dowolne bazy danych
dostêpne przez DBI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
