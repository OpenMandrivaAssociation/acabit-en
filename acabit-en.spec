%define base_name	acabit
%define name		%{base_name}-en

Name:		acabit-en
Version:	4.3
Release:	1
Summary:	Automatic Corpus-based Acquisition of Binary Terms
License:	GPL
Group:		Sciences/Computer science
Source0:	https://web.archive.org/web/20070226194754if_/http://www.sciences.univ-nantes.fr:80/info/perso/permanents/daille/acabit_en_v%{version}.tgz
Url:		https://web.archive.org/web/20090605220804/http://www.sciences.univ-nantes.fr/info/perso/permanents/daille/acabit_en.html
BuildArch:	noarch
Obsoletes:	%{base_name}
Provides:	%{base_name}
Requires:	locales-en

%description
ACABIT is a terminological aquisition software, taking an annotated  text as
input, and returning an ordered list of candidates terms.

This is the english version.

%prep
%autosetup -p1 -n %{base_name}_en_v%{version}

%build
perl -pi -e 's|require \("lib/(.*)"\);|require ("%{_datadir}/%{name}/$1");|' */*.pl

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -m 755 *.pl %{buildroot}%{_bindir}
install -m 644 lib/* %{buildroot}%{_datadir}/%{name}

%files
%defattr(-,root,root)
%doc exemple_en.txt
%{_bindir}/*
%{_datadir}/%{name}
