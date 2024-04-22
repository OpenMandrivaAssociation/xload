Name:		xload
Version:	1.2.0
Release:	1
Summary:	System load average display for X
Group:		Development/X11
Source0:	https://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.xz
License:	MIT

BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
The xload program displays a periodically updating histogram of the system
load average.

%prep
%autosetup -p1

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/xload
%{_datadir}/X11/app-defaults/XLoad
%doc %{_mandir}/man1/xload.1*
