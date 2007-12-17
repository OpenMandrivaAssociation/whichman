%define name whichman
%define version 2.4
%define release %mkrel 1

Summary: Fault tolerant search utilities
Name: %{name}
Version: %{version}
Release: %{release}
License: GPL
Group: File tools
Url: http://main.linuxfocus.org/~guido/
Source: %{name}-%{version}.tar.bz2
Patch: whichman-makefile.patch.bz2
#Patch: whichman-2.0-makefile_manpage.patch.bz2
#Patch1: whichman-2.0-lfs_mancompliant.patch.bz2

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

