%define debug_package %{nil}

Name:           aihc
Version:        0.1.0
Release:        0.2%{?dist}
Summary:        AI Haskell Compiler

License:        Unlicense
URL:            https://github.com/ai-haskell-compiler/aihc
Source0:        https://github.com/ai-haskell-compiler/aihc/archive/refs/tags/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
# https://github.com/ai-haskell-compiler/aihc/pull/3321
Patch0:         https://patch-diff.githubusercontent.com/raw/ai-haskell-compiler/aihc/pull/3321.patch

BuildRequires:  cabal-install
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
mkdir -p %{buildroot}%{_bindir}
strip -s -o %{buildroot}%{_bindir}/aihc dist-newstyle/build/%{_arch}-linux/ghc-9.12.4/aihc-%{version}/x/aihc/build/aihc/aihc

%check
%{buildroot}%{_bindir}/aihc build examples/hello-world/Main.hs -o hello-world
./hello-world


%files
%license LICENSE
%doc README.md
%{_bindir}/aihc


%changelog
* Sun Nov 15 2026 Jens Petersen <petersen@redhat.com>
- initial package
