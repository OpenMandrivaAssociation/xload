Name:		xload
Version:	1.1.2
Release:	5
Summary:	System load average display for X
Group:		Development/X11
Source0:	http://xorg.freedesktop.org/releases/individual/app/%{name}-%{version}.tar.bz2
License:	MIT

BuildRequires:	pkgconfig(xt)
BuildRequires:	pkgconfig(xaw7)
BuildRequires:	pkgconfig(xorg-macros)

%description
The xload program displays a periodically updating histogram of the system
load average.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/xload
%{_datadir}/X11/app-defaults/XLoad
%{_mandir}/man1/xload.1*


%changelog
* Mon Mar 26 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.1.1-1
+ Revision: 786811
- version update 1.1.1

* Sat May 07 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 671334
- mass rebuild

* Sun Sep 26 2010 Thierry Vignaud <tv@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 581151
- new release

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.2-6mdv2010.1
+ Revision: 524450
- rebuilt for 2010.1

* Mon Apr 13 2009 Funda Wang <fwang@mandriva.org> 1.0.2-5mdv2009.1
+ Revision: 366690
- no autoreconf needed

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.0.2-4mdv2009.0
+ Revision: 226052
- rebuild

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Revert to use upstream tarball, build requires and remove non mandatory local patches.

* Thu Jan 17 2008 Paulo Andrade <pcpa@mandriva.com.br> 1.0.2-3mdv2008.1
+ Revision: 154447
- Updated BuildRequires and resubmit package.

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 1.0.2-2mdv2008.1
+ Revision: 130255
- kill re-definition of %%buildroot on Pixel's request
- do not hardcode lzma extension!!!

  + Paulo Andrade <pcpa@mandriva.com.br>
    - Choose default Xaw from xaw.m4 unless configure explicitly told otherwise.

