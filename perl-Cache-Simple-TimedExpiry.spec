%define upstream_name    Cache-Simple-TimedExpiry
%define upstream_version 0.27

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    Perl module to add expiry to Cache::Simple object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildArch:      noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}-%{release}

%description
Perl module to add expiry to Cache::Simple object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
