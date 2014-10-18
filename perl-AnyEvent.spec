%include	/usr/lib/rpm/macros.perl

%define		pdir	AnyEvent
%define		pnam	I3

Summary:	Simple API for I/O, timer, signal, child process and completion events
Name:		perl-AnyEvent
Version:	7.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://search.cpan.org/CPAN/authors/id/M/ML/MLEHMANN/%{pdir}-%{version}.tar.gz
# Source0-md5:	e5ef99081b2acc3df80851838f9acfc4
URL:		http://search.cpan.org/dist/common-sense/
BuildRequires:	perl-devel
BuildRequires:	rpm-perlprov
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module offers a simple API for I/O, timer, signal, child process
and completion events, independent of a specific event loop.

%prep
%setup -qn %{pdir}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%check
#%{__make} test

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{perl_vendorarch}/AnyEvent
%dir %{perl_vendorarch}/AnyEvent/IO
%dir %{perl_vendorarch}/AnyEvent/Impl
%dir %{perl_vendorarch}/AnyEvent/Util
%{perl_vendorarch}/AnyEvent/*.p[lm]
%{perl_vendorarch}/AnyEvent/IO/*.pm
%{perl_vendorarch}/AnyEvent/Impl/*.pm
%{perl_vendorarch}/AnyEvent/Util/*.pl
%{perl_vendorarch}/*.p[lm]
%{_mandir}/man3/AnyEvent*.3*

%if 0
%doc Changes LICENSE README
%dir %{perl_vendorlib}/AnyEvent
%{perl_vendorlib}/common/*.pm
%{_mandir}/man3/common::sense.3pm*
%endif
