%define module  Cache-Simple-TimedExpiry
%define name    perl-%{module}
%define version 0.26
%define release %mkrel 2

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:        Perl module to add expiry to Cache::Simple object
License:	    GPL or Artistic
Group:		    Development/Perl
Url:		    http://search.cpan.org/dist/%{module}
Source:		    http://www.cpan.org/modules/by-module/Cache/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

%description
Perl module to add expiry to Cache::Simple object.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes 
%{perl_vendorlib}/Cache
%{_mandir}/man3/*


