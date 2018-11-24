%define debug_package %{nil}

Name:     ocaml-taglib

Version:  0.3.5
Release:  0.0%{dist}
Summary:  OCaml bindings for the taglib
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-taglib
Source0:  https://github.com/savonet/ocaml-taglib/releases/download/%{version}/ocaml-taglib-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: gcc-c++
BuildRequires: taglib-devel
Requires:      taglib

%prep
%setup -q 

%build
./configure \
   --prefix=%{_prefix} \
   -disable-ldconf
make all

%install
export DESTDIR=%{buildroot}
export OCAMLFIND_DESTDIR=%{buildroot}$(ocamlfind printconf destdir)
export OCAMLFIND_LDCONF=ignore
export DLLDIR=$OCAMLFIND_DESTDIR/stublibs

install -d $OCAMLFIND_DESTDIR/%{ocamlpck}
make install

%files
%{_libdir}/ocaml/taglib/
%{_libdir}/ocaml/taglib/META
%{_libdir}/ocaml/taglib/dlltaglib_stubs.so
%{_libdir}/ocaml/taglib/libtaglib_stubs.a
%{_libdir}/ocaml/taglib/taglib.a
%{_libdir}/ocaml/taglib/taglib.cma
%{_libdir}/ocaml/taglib/taglib.cmi
%{_libdir}/ocaml/taglib/taglib.cmx
%{_libdir}/ocaml/taglib/taglib.cmxa
%{_libdir}/ocaml/taglib/taglib.mli

%description
OCaml interface for TagLib Audio Meta-Data Library, otherwise known as taglib.


%changelog
* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.5-0.0
- Bump to 0.3.5
- Start cleaning up files section

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-2
- Fix Fedora build by disabling debug package

* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch>
- Bump version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-taglib.spec
