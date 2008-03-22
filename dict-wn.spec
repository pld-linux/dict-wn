%define		dictname wn
Summary:	WordNet lexical reference system for dictd
Summary(pl.UTF-8):	System referencji słownikowych WordNet dla dictd
Name:		dict-%{dictname}
Version:	3.0
Release:	1
License:	Free to use, but see http://www.cogsci.princeton.edu/~wn/
Group:		Applications/Dictionaries
Source0:	%{name}-%{version}.tar.gz
# Source0-md5:	bac633bda094b0a4f458a87a5660080c
URL:		http://www.dict.org/
BuildRequires:	rpmbuild(macros) >= 1.268
Requires:	%{_sysconfdir}/dictd
Requires:	dictd
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package contains WordNet (r) %{version} Lexical Database
formatted for use by the dictionary server in the dictd package.

%description -l pl.UTF-8
Ten pakiet zawiera leksykalną bazę danych WordNet (r) %{version}
sformatowaną do używania z serwerem słownika dictd.

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
%service -q dictd restart

%postun
if [ "$1" = 0 ]; then
	%service -q dictd restart
fi

%files
%defattr(644,root,root,755)
%doc AUTHORS README copyright
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/dictd/%{dictname}.dictconf
%{_datadir}/dictd/%{dictname}.*
