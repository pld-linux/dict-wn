%define		dictname wn
Summary:	WordNet lexical reference system formatted as dictionary for dictd
Name:		dict-wn
Version:	1.5
Release:	2
License:	Free to use, but see http://www.cogsci.princeton.edu/~wn/
Group:		Applications/Dictionaries
Group(de):	Applikationen/Wörterbücher
Group(pl):	Aplikacje/S³owniki
URL:		http://www.dict.org/
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	dictzip
BuildRequires:	autoconf
Requires:	dictd 
Requires:	%{_sysconfdir}/dictd

%description 
This package contains WordNet (r) 1.6 Lexical Database formatted for
use by the dictionary server in the dictd package.

%prep 
%setup -q

%build
autoconf
%configure 
%{__make} db 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd/,%{_sysconfdir}/dictd}
%{__make} install dictdir="$RPM_BUILD_ROOT%{_datadir}/dictd/"

dictprefix=%{_datadir}/dictd/wn
echo "# WordNet 1.6 Lexical Database dictionary
database %{dictname} {
    data  \"$dictprefix.dict.dz\"
    index \"$dictprefix.index\" 
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf

%clean
rm -rf $RPM_BUILD_ROOT

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}*
