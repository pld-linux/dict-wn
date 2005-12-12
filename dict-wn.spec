%define		dictname wn
Summary:	WordNet lexical reference system for dictd
Summary(pl):	System referencji s³ownikowych WordNet dla dictd
Name:		dict-%{dictname}
Version:	2.0
Release:	2
License:	Free to use, but see http://www.cogsci.princeton.edu/~wn/
Group:		Applications/Dictionaries
# note: pre means preformatted
Source0:	ftp://ftp.dict.org/pub/dict/pre/%{name}-%{version}-pre.tar.gz
# Source0-md5:	fcfedcc13815cde1e28103b61c05c168
URL:		http://www.dict.org/
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains WordNet (r) %{version} Lexical Database
formatted for use by the dictionary server in the dictd package.

%description -l pl
Ten pakiet zawiera leksykaln± bazê danych WordNet (r) %{version}
sformatowan± do u¿ywania z serwerem s³ownika dictd.

%prep
%setup -c -q

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_datadir}/dictd,%{_sysconfdir}/dictd}

dictprefix=%{_datadir}/dictd/%{dictname}
echo "# WordNet %{version} Lexical Database dictionary
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
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
