Name: xload
Version: 1.1.1
Release: 1
Summary: System load average display for X
Group: Development/X11
Source0: http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License: MIT

BuildRequires: libxt-devel >= 1.0.0
BuildRequires: libxaw-devel >= 1.0.1
BuildRequires: x11-util-macros >= 1.0.1

%description
The xload program displays a periodically updating histogram of the system
load average.

%prep
%setup -q -n %{name}-%{version}

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xload
%{_datadir}/X11/app-defaults/XLoad
%{_mandir}/man1/xload.1*
