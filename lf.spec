Name:       lf
Version:    32
Release:    1
Summary:    Terminal file manager

License:    MIT
URL:        https://github.com/gokcehan/lf
Source0:    %{url}/archive/refs/tags/r%{version}.tar.gz

BuildRequires: golang


%description
lf is a terminal file manager written in Go with a heavy inspiration from ranger file manager.


%prep
%autosetup


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
* Mon Oct 21 2024 Ernesto Martínez <me@ecomaikgolf.com>

- Intiial setup