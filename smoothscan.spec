Summary:	A tool to convert scanned text into a vectorized output form
Name:		smoothscan
Version:	0.1.0
Release:	0
License:	GPLv3+
Group:		Office
URL:		https://natecraun.net/projects/smoothscan/
Source0:	https://github.com/ncraun/%{name}/archive/v%{version}.tar.gz

BuildRequires:	fontforge-python
BuildRequires:	potrace
BuildRequires:	python
BuildRequires:	fontforge
BuildRequires:	haru-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(libtiff-4)
BuildRequires:	pkgconfig(lept)
#BuildRequires:	pkgconfig(libfontforge)

Requires:	python
Requires:	fontforge-python

%description
smoothscan is a tool to convert scanned text into a vectorized output
form. Because printed text is assembled from fonts, each particular
letter (like 'o') will have the same shape as every other 'o' in the
document. We can take advantage of this, by building a table of such
symbols, and represent each occurrence of a symbol with a reference to
that symbol's table entry. This will save a lot of space, and a
similar idea is used in djvu's jb2 mode and JBIG2 for PDF.

%files
%{_bindir}/%{name}
%{_bindir}/%{name}-fontgen.py
%{_mandir}/man1/%{name}.1*
%doc README
%doc NEWS
%doc TODO
%doc AUTHORS
%doc COPYING

#----------------------------------------------------------------------------

%prep
%setup -q

%build
autoreconf -fiv
%configure
%make

%install
%makeinstall_std

