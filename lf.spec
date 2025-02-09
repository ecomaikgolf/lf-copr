Name:       lf
Version:    34
Release:    1
Summary:    Terminal file manager

License:    MIT
URL:        https://github.com/gokcehan/lf
Source0:    %{url}/archive/refs/tags/r%{version}.tar.gz

BuildRequires: golang
BuildRequires: git

# https://github.com/rpm-software-management/rpm/issues/367#issuecomment-350131349
%global _missing_build_ids_terminate_build 0
%global debug_package %{nil}

%description
lf is a terminal file manager written in Go with a heavy inspiration from ranger file manager.


%prep
%setup -n %{name}-r%{version}


%build
env CGO_ENABLED=0 go build -ldflags="-s -w"


%install
install -d -m 0755 %{buildroot}%{_bindir}
install -m 0755 lf %{buildroot}%{_bindir}/%{name}


%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}


%changelog
* Sat Nov 2 2024 Ernesto Martínez <me@ecomaikgolf.com>
- Bump r32 -> r33

* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>
- Initial setup
