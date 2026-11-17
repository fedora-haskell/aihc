%define debug_package %{nil}

Name:           aihc
Version:        0.1.0
Release:        0.3%{?dist}
Summary:        AI Haskell Compiler

License:        Unlicense
URL:            https://github.com/ai-haskell-compiler/aihc
Source0:        https://github.com/ai-haskell-compiler/aihc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        aihc.sh
# https://github.com/ai-haskell-compiler/aihc/pull/3321
Patch0:         https://patch-diff.githubusercontent.com/raw/ai-haskell-compiler/aihc/pull/3321.patch

BuildRequires:  cabal-install
# for check
BuildRequires:  clang
BuildRequires:  ghc9.12
BuildRequires:  zlib-devel
Requires:       clang

%description
AIHC is a Haskell compiler that AI models write.
It compiles Haskell source code to native machine code,
to LLVM IR, and to WebAssembly.


%prep
%autosetup -p1


%build
cabal update
cabal build -w %{_bindir}/ghc-9.12 exe:aihc


%install
mkdir -p %{buildroot}%{_libexecdir}
strip -s -o %{buildroot}%{_libexecdir}/aihc dist-newstyle/build/%{_arch}-linux/ghc-9.12.4/aihc-%{version}/x/aihc/build/aihc/aihc

%global aihc_datadir %{_datadir}/aihc
mkdir -p %{buildroot}%{aihc_datadir}/
cp -pr core-libs %{buildroot}%{aihc_datadir}

mkdir -p %{buildroot}%{_bindir}
install -p %{SOURCE1} %{buildroot}%{_bindir}/aihc

%check
%{buildroot}%{_libexecdir}/aihc build examples/hello-world/Main.hs -o hello-world
./hello-world


%files
%license LICENSE
%doc README.md examples
%{_bindir}/aihc
%{_libexecdir}/aihc
%{aihc_datadir}


%changelog
* Tue Nov 17 2026 Jens Petersen <petersen@redhat.com> - 0.1.0-0.3
- check needs clang
- include core-libs

* Sun Nov 15 2026 Jens Petersen <petersen@redhat.com> - 0.1.0-0.2
- initial package
