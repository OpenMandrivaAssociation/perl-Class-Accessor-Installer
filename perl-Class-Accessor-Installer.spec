%define upstream_name    Class-Accessor-Installer
%define upstream_version 1.100880

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Install an accessor subroutine
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Class/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Class::Accessor)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(Pod::Generated)
BuildRequires: perl(Sub::Name)
BuildRequires: perl(Test::Compile)
BuildRequires: perl(Test::More)
BuildRequires: perl(UNIVERSAL::require)
BuildRequires: perl(URI::Escape)
BuildRequires: perl(Vim::Tag)

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This mixin class provides a method that will install a coderef. There are
other modules that do this, but this one is a bit more specific to the
needs of the Class::Accessor::Complex manpage and friends.

It is intended as a mixin, that is, your accessor-generating class should
inherit from this class.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor --skipdeps
%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes LICENSE README
%{_mandir}/man3/*
%perl_vendorlib/*
