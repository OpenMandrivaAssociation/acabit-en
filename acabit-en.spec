%define base_name	acabit
%define name		%{base_name}-en
%define version		26112003
%define release		10

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Automatic Corpus-based Acquisition of Binary Terms
License:	GPL
Group:		Sciences/Computer science
Source0:	http://www.sciences.univ-nantes.fr/info/perso/permanents/daille/%{base_name}_en_%{version}.tar.bz2
Url:		http://www.sciences.univ-nantes.fr/info/perso/permanents/daille/acabit.html
Buildroot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch
Obsoletes:	%{base_name}
Provides:	%{base_name}
Requires:	locales-en

%description
ACABIT is a terminological aquisition software, taking an annotated  text as
input, and returning an ordered list of candidates terms.

This is the english version.

%prep
%setup -q -n %{base_name}_en 

%build
perl -pi -e 's|require \("lib/(.*)"\);|require ("%{_datadir}/%{name}/$1");|' */*.pl

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 *.pl %{buildroot}%{_bindir}
install -m 644 lib/* %{buildroot}%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc exemple_en.txt
%{_bindir}/*
%{_datadir}/%{name}



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 26112003-9mdv2011.0
+ Revision: 616498
- the mass rebuild of 2010.0 packages

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Tue Sep 01 2009 Thierry Vignaud <tv@mandriva.org> 26112003-7mdv2010.0
+ Revision: 423860
- rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 26112003-6mdv2009.0
+ Revision: 226107
- rebuild

* Thu Dec 20 2007 Olivier Blin <oblin@mandriva.com> 26112003-5mdv2008.1
+ Revision: 135813
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Aug 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 26112003-5mdv2008.0
+ Revision: 67052
- rebuild
- import acabit-en


* Tue Jul 11 2006 Lenny Cartier <lenny@mandriva.com> 26112003-4mdv2007.0
- rebuild

* Thu Jul 28 2005 Guillaume Rousse <guillomovitch@mandriva.org> 26112003-3mdk 
- split package in two distinct ones, as english and french version have different versions

* Fri Jul 09 2004 Guillaume Rousse <guillomovitch@mandrake.org> 26112003-2mdk 
- fixed spec perms

* Tue Jun 15 2004 Guillaume Rousse <guillomovitch@mandrake.org> 26112003-1mdk 
- first mdk release
