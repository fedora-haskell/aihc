%define debug_package %{nil}

%global forgeurl https://github.com/ai-haskell-compiler/aihc
%global version0 0.2.0
%global commit ddbee0c4077391713e38750ad12999c1f65a41a6
%forgemeta

Name:           aihc
Version:        %{forgeversion -p}
Release:        0.1%{?dist}
Summary:        AI Haskell Compiler

License:        Unlicense
URL:            https://docs.aihc.app/
Source0:        %{forgesource}
Source1:        aihc.sh

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
%forgesetup
# %%autopatch -p1


%build
cabal update
cabal build -w %{_bindir}/ghc-9.12 exe:aihc


%install
mkdir -p %{buildroot}%{_libexecdir}
strip -s -o %{buildroot}%{_libexecdir}/aihc dist-newstyle/build/%{_arch}-linux/ghc-9.12.4/aihc-%{version0}/x/aihc/build/aihc/aihc

%global aihc_datadir %{_datadir}/aihc
mkdir -p %{buildroot}%{aihc_datadir}/
cp -pr core-libs %{buildroot}%{aihc_datadir}

mkdir -p %{buildroot}%{_bindir}
install -p %{SOURCE1} %{buildroot}%{_bindir}/aihc

%check
%ifnarch x86_64
%define target --target llvm
%endif
%{buildroot}%{_libexecdir}/aihc build %{?target} examples/hello-world/Main.hs -o hello-world
./hello-world


%files
%license LICENSE
%doc README.md examples
%{_bindir}/aihc
%{_libexecdir}/aihc
%{aihc_datadir}


%changelog
* Tue Nov 17 2026 Jens Petersen <petersen@redhat.com> - 0.2.0~20261117gitddbee0c-0.1
- update to 0.2-pre snapshot using forge macros

* Tue Nov 17 2026 Jens Petersen <petersen@redhat.com> - 0.1.0-0.3
- check needs clang
- include core-libs

* Sun Nov 15 2026 Jens Petersen <petersen@redhat.com> - 0.1.0-0.2
- initial package
