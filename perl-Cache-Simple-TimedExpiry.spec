%define upstream_name    Cache-Simple-TimedExpiry
%define upstream_version 0.27

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Perl module to add expiry to Cache::Simple object
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Cache/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
Perl module to add expiry to Cache::Simple object.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std
rm -rf %{buildroot}/%{perl_vendorarch}/

%files
%doc Changes 
%{perl_vendorlib}/Cache
%{_mandir}/man3/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 0.270.0-2mdv2011.0
+ Revision: 680712
- mass rebuild

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.270.0-1mdv2011.0
+ Revision: 405956
- rebuild using %%perl_convert_version

* Fri Jun 13 2008 Michael Scherer <misc@mandriva.org> 0.27-2mdv2009.0
+ Revision: 218996
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Apr 29 2007 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.27-1mdv2008.0
+ Revision: 19251
-New version


* Wed Nov 01 2006 Michael Scherer <misc@mandriva.org> 0.26-2mdv2007.0
+ Revision: 74867
- Rebuild for new extension
- Import perl-Cache-Simple-TimedExpiry

