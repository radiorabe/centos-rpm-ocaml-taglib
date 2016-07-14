Name:     ocaml-taglib

Version:  0.3.2
Release:  1
Summary:  OCaml bindings for the taglib
License:  GPLv2+
URL:      https://github.com/savonet/ocaml-taglib
Source0:  https://github.com/savonet/ocaml-taglib/releases/download/0.3.2/ocaml-taglib-0.3.2.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
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
/usr/lib64/ocaml/taglib/META
/usr/lib64/ocaml/taglib/dlltaglib_stubs.so
/usr/lib64/ocaml/taglib/libtaglib_stubs.a
/usr/lib64/ocaml/taglib/taglib.a
/usr/lib64/ocaml/taglib/taglib.cma
/usr/lib64/ocaml/taglib/taglib.cmi
/usr/lib64/ocaml/taglib/taglib.cmx
/usr/lib64/ocaml/taglib/taglib.cmxa
/usr/lib64/ocaml/taglib/taglib.mli

%description
OCaml interface for TagLib Audio Meta-Data Library, otherwise known as taglib.


%changelog
* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch>
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-taglib.spec
