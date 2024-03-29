Summary:	Guile WWW library
Summary(pl.UTF-8):	Biblioteka WWW do Guile
Name:		guile-www
Version:	1.1.1
Release:	2
License:	GPL
Group:		Development/Languages/Scheme
Source0:	ftp://ftp.gnu.org/pub/gnu/guile/%{name}-%{version}.tar.gz
# Source0-md5:	134cc208f7b6fd30aa03bae90ce2f152
URL:		http://www.gnu.org/software/guile/guile.html
BuildRequires:	guile-devel
Requires:	guile
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Guile WWW library, a set of Guile Scheme modules to
facilitate HTTP, URL and CGI programming.

%description -l pl.UTF-8
To jest biblioteka WWW dla Guile, czyli zestaw modułów Guile Scheme
mających za zadanie ułatwić programowanie HTTP, URL i CGI.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p	/sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%{_datadir}/guile/www
%{_infodir}/*.info*
