%define name whichman
%define version 2.4
%define release 6

Summary: Fault tolerant search utilities
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: File tools
Url: https://main.linuxfocus.org/~guido/
Source: %{name}-%{version}.tar.bz2
Patch: whichman-makefile.patch.bz2
#Patch: whichman-2.0-makefile_manpage.patch.bz2
#Patch1: whichman-2.0-lfs_mancompliant.patch.bz2
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot

%description
ftff, ftwhich and whichman are fault tolerant search utilities.
whichman allows to search for man pages that match approximately the specified
search key. ftff is a fault tolerant file find utility and ftwhich
is a fault tolerant version for the 'which' command.
The error tolerant approximate string match is based on the Levenshtein
Distance between two strings. This is a measure for the number of
replacements, insertions and deletions that are necessary to transform
string A into string B.

%prep

%setup -q
%patch 
#%patch1 -p1

%build
%make 

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
make DESTDIR=$RPM_BUILD_ROOT PREFIX=$RPM_BUILD_ROOT%{_prefix} MANDIR=$RPM_BUILD_ROOT%{_mandir} install

%clean
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi

%files
%defattr(-,root,root)
%doc README 
%{_bindir}/*
%{_mandir}/man1/*



%changelog
* Wed Sep 09 2009 Thierry Vignaud <tvignaud@mandriva.com> 2.4-5mdv2010.0
+ Revision: 434745
- rebuild

* Sun Aug 03 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4-4mdv2009.0
+ Revision: 261949
- rebuild

* Wed Jul 30 2008 Thierry Vignaud <tvignaud@mandriva.com> 2.4-3mdv2009.0
+ Revision: 255951
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tvignaud@mandriva.com> 2.4-1mdv2008.1
+ Revision: 129336
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import whichman


* Sat Aug 28 2004 Franck Villaume <fvill@freesurf.fr> 2.4-1mdk
- 2.4

* Thu Jun 12 2003 Marcel Pol <mpol@gmx.net> 2.1-1mdk
- 2.1

* Thu Oct 18 2001 Daouda LO <daouda@mandrakesoft.com> 2.0-2mdk
- rpmlint compliant

* Thu May 31 2001  Daouda Lo <daouda@mandrakesoft.com> 2.0-1mdk
- first mdk package.
- mdkisation (lfs compliant: s|/usr/man|/usr/share/man)



