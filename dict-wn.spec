%define		dictname wn
Summary:	WordNet lexical reference system for dictd
Summary(pl):	System referencji s�ownikowych WordNet dla dictd
Name:		dict-%{dictname}
Version:	1.7a
Release:	1
License:	Free to use, but see http://www.cogsci.princeton.edu/~wn/
Group:		Applications/Dictionaries
Source0:	ftp://ftp.dict.org/pub/dict/pre/%{name}_%{version}.tar.gz
# Source0-md5:	e58001b93c59a607bc9d5903a80df71e
URL:		http://www.dict.org/
Requires:	dictd
Requires:	%{_sysconfdir}/dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains WordNet (r) %version Lexical Database formatted for
use by the dictionary server in the dictd package.

%description -l pl
Ten pakiet zawiera leksykaln� baz� danych WordNet (r) %version sformatowan�
do u�ywania z serwerem s�ownika dictd.

%prep
%setup -c -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# WordNet %version Lexical Database dictionary
database %{dictname} {
	data  \"$dictprefix.dict.dz\"
	index \"$dictprefix.index\"
}" > $RPM_BUILD_ROOT%{_sysconfdir}/dictd/%{dictname}.dictconf
mv %{dictname}.* $RPM_BUILD_ROOT%{_datadir}/dictd

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2
fi

%postun
if [ -f /var/lock/subsys/dictd ]; then
	/etc/rc.d/init.d/dictd restart 1>&2 || true
fi

%files
%defattr(644,root,root,755)
%attr(640,root,root) %config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
