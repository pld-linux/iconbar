Summary:	EFL-enabled iconbar
Name:		iconbar
Version:	0.9.1
%define _snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	0de760614558418831ba42ed0dcdbc79
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
%doc AUTHORS COPYING INSTALL README TODO ChangeLog
%attr(755,root,root) %{_bindir}/iconbar
%{_datadir}/%{name}
