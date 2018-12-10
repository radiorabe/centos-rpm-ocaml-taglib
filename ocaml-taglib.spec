%define debug_package %{nil}

Name:     ocaml-taglib
Version:  0.3.5
Release:  0.1%{dist}
Summary:  OCaml bindings for the taglib

%global libname %(echo %{name} | sed -e 's/^ocaml-//')

License:  GPLv2+
URL:      https://github.com/savonet/ocaml-taglib
Source0:  https://github.com/savonet/ocaml-taglib/releases/download/%{version}/ocaml-taglib-%{version}.tar.gz

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: gcc-c++
BuildRequires: taglib-devel
Requires:      taglib


%description
OCaml interface for TagLib Audio Meta-Data Library, otherwise known as taglib.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature
files for developing applications that use %{name}.


%prep
%autosetup -n %{name}-%{version}

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
%license COPYING
%{_libdir}/ocaml/%{libname}
%ifarch %{ocaml_native_compiler}
%exclude %{_libdir}/ocaml/%{libname}/*.a
%exclude %{_libdir}/ocaml/%{libname}/*.cmxa
%exclude %{_libdir}/ocaml/%{libname}/*.cmx
%exclude %{_libdir}/ocaml/%{libname}/*.mli
%endif

%files devel
%license COPYING
%ifarch %{ocaml_native_compiler}
%{_libdir}/ocaml/%{libname}/*.a
%{_libdir}/ocaml/%{libname}/*.cmxa
%{_libdir}/ocaml/%{libname}/*.cmx
%{_libdir}/ocaml/%{libname}/*.mli
%endif

%changelog
* Mon Dec 10 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.5-0.1
- Cleanup and add separate -devel subpackage

* Fri Nov 23 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.5-0.0
- Bump to 0.3.5
- Start cleaning up files section

* Sun Nov 11 2018 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-2
- Fix Fedora build by disabling debug package

* Sat Apr 15 2017 Lucas Bickel <hairmare@rabe.ch> - 0.3.3-1
- Bump version

* Sun Jul  3 2016 Lucas Bickel <hairmare@rabe.ch> - 0.3.2-1
- initial version, mostly stolen from https://www.openmamba.org/showfile.html?file=/pub/openmamba/devel/specs/ocaml-taglib.spec
