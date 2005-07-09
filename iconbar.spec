Summary:	EFL-enabled iconbar
Summary(pl):	Pasek ikon oparty na EFL
Name:		iconbar
Version:	0.9.1
%define _snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	2228eff12f92d39785fdc89efb27975a
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a standalone iconbar based on the e17 iconbar by raster and
rephorm. As of v0.5 the iconbar now uses Edje for both its theme and
its icons. This allows for all sorts of animation and other effects.
As of now, the included themes mimic the old iconbar behavior. Expect
to see themes taking advantage of Edje's capabilities in the future.

%description -l pl
Jest to samodzielny pasek ikon oparty na pasku ikon e17 zrobionym
przez raster i rephorm. W wersji 0.5 pasek ikon u�ywa Edje zar�wno dla
motywu, jak i ikon. Pozwala to na wszelkie rodzaje animacji i innych
efekt�w. Jak na razie za��czone motywy na�laduj� stare zachowanie
paska ikon, ale w przysz�o�ci nale�y si� spodziewa� motyw�w
wykorzystuj�cych przewag� mo�liwo�ci Edje.

%prep
%setup -q -n %{name}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%attr(755,root,root) %{_bindir}/iconbar
%{_datadir}/%{name}
