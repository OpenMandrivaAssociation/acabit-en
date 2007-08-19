%define base_name	acabit
%define name		%{base_name}-en
%define version		26112003
%define release		%mkrel 4

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

