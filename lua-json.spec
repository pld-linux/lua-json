# TODO
# - noarch pkg?
Summary:	A lightweight JSON library for Lua
Name:		lua-json
Version:	0.1.2
Release:	1
License:	BSD-like
Group:		Development/Languages
Source0:	https://github.com/rxi/json.lua/archive/refs/tags/v%{version}.tar.gz
# Source0-md5:	098b01952297cb33832fae428b65f23f
URL:		https://github.com/rxi/json.lua
BuildRequires:	lua53-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A lightweight JSON library for Lua.

Features:
- Implemented in pure Lua
- Fast: generally outperforms other pure Lua JSON implementations
  (benchmark scripts)
- Tiny: around 280sloc, 9kb
- Proper error messages, eg: expected '}' or ',' at line 203 col 30

%prep
%setup -q -n json.lua-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_datadir}/lua/5.3

cp -a json.lua $RPM_BUILD_ROOT%{_datadir}/lua/5.3

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md
%{_datadir}/lua/5.3/json.lua
