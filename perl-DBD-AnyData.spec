#
# Conditional build:
# _with_tests - perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	DBD
%define	pnam	AnyData
Summary:	DBD::AnyData - DBI access to XML, CSV and other formats
Summary(pl):	DBD::AnyData - dostêp DBI do XML, CSV i innych formatów
Name:		perl-DBD-AnyData
Version:	0.05
Release:	3
License:	?
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
%if %{?_with_tests:1}%{!?_with_tests:0}
BuildRequires:	perl-AnyData
BuildRequires:	perl-XML-Parser
BuildRequires:	perl-XML-Twig
BuildRequires:	perl-HTML-Parser
BuildRequires:	perl-HTML-TableExtract
BuildRequires:	perl-CGI
%endif
BuildRequires:	rpm-perlprov >= 3.0.3-26
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
perl Makefile.PL
%{__make}

# test seem to hang ... 
%{?_with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_sitelib}/%{pdir}/*.pm
%{_mandir}/man3/*
