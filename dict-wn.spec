%define         dictname wn
Summary:	WordNet lexical reference system formatted as dictionary for dictd
Name:		dict-%{dictname}
Version:	1.5
Release:	1
License:	Free to use, but see http://www.cogsci.princeton.edu/~wn/
Group:		Applications/Dictionaries
Group(pl):	Aplikacje/S³owniki
URL:		http://www.dict.org/
Source0:	ftp://ftp.dict.org/pub/dict/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildRequires:	dictzip
Requires:	dictd 
BuildArch:	noarch

%description 
This package contains WordNet (r) 1.6 Lexical Database formatted for
use by the dictionary server in the dictd package.

%prep 
%setup -q

%build
%configure 
%{__make} db 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/dictd/

DICTDIR="$RPM_BUILD_ROOT%{_datadir}/dictd/"
%{__make} install dictdir="$DICTDIR" 

%clean
rm -rf $RPM_BUILD_ROOT

%post
prefix=%{_datadir}/dictd/%{dictname}

if ! grep ' %{dictname} ' /etc/dictd.conf >/dev/null; then 
   echo "Edit /etc/dictd.conf to see %{dictname} dictionary under dictd"
echo "# Uncommment this to configure WordNet Lexical Database dictionary
#database %{dictname} {
#    data  \"$prefix.dict.dz\"
#    index \"$prefix.index\" }
" >> /etc/dictd.conf
fi

%files
%defattr(644,root,root,755)
%{_datadir}/dictd/%{dictname}*
