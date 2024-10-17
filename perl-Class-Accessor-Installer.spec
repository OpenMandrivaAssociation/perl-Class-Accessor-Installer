%define upstream_name    Class-Accessor-Installer
%define upstream_version 1.100880

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Install an accessor subroutine
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Class::Accessor)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Pod::Generated)
BuildRequires:	perl(Sub::Name)
BuildRequires:	perl(Test::Compile)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(UNIVERSAL::require)
BuildRequires:	perl(URI::Escape)
#BuildRequires:	perl(Vim::Tag)

BuildArch:	noarch

%description
This mixin class provides a method that will install a coderef. There are
other modules that do this, but this one is a bit more specific to the
needs of the Class::Accessor::Complex manpage and friends.

It is intended as a mixin, that is, your accessor-generating class should
inherit from this class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 16 2011 Funda Wang <fwang@mandriva.org> 1.100.880-2mdv2011.0
+ Revision: 653396
- rebuild for updated spec-helper

* Tue Mar 30 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.880-1mdv2011.0
+ Revision: 529776
- update to 1.100880

* Wed Mar 24 2010 Jérôme Quelin <jquelin@mandriva.org> 1.100.820-1mdv2010.1
+ Revision: 527094
- update to 1.100820

* Thu Feb 11 2010 Jérôme Quelin <jquelin@mandriva.org> 0.90.0-1mdv2010.1
+ Revision: 504070
- update to 0.09

* Mon Feb 08 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2010.1
+ Revision: 502179
- update to 0.08

* Tue Dec 08 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 474687
- adding missing buildrequires:
- update to 0.06

* Fri Sep 18 2009 Jérôme Quelin <jquelin@mandriva.org> 0.50.0-1mdv2010.0
+ Revision: 444411
- adding missing buildrequires
- import perl-Class-Accessor-Installer


* Thu Sep 17 2009 cpan2dist 0.05-1mdv
- initial mdv release, generated with cpan2dist
