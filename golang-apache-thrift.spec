# Run tests in check section
%bcond_with check

%global goipath         git.apache.org/thrift.git
%global forgeurl        https://github.com/apache/thrift
%global commit          129f332d72facda5d06f87e2b4e5e08bea0b6b44

%global common_description %{expand:
Thrift is a lightweight, language-independent software stack with an 
associated code generation mechanism for RPC. Thrift provides clean 
abstractions for data transport, data serialization, and application level 
processing. The code generation system takes a simple definition language as 
its input and generates code across programming languages that uses the 
abstracted stack to build interoperable RPC clients and servers.}

%gometa

Name:           %{goname}
Version:        0.11.0
Release:        0.3%{?dist}
Summary:        Thrift Go Software Library
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}

BuildRequires: golang(github.com/golang/mock/gomock)

%description
%{common_description}


%package devel
Summary:       %{summary}
BuildArch:     noarch

%description devel
%{common_description}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%forgeautosetup
# Remove files unrelated to the Go Library
find ./* -maxdepth 0 -type d -not -name "lib" -exec rm -rf "{}" \;
find ./* -mindepth 1 -maxdepth 1 -type d -not -name "go" -exec rm -rf "{}" \;
rm -rf lib/go/test


%install
%goinstall


%if %{with check}
%check
%gochecks
%endif


%files devel -f devel.file-list
%license LICENSE
%doc README.md LANGUAGES.md CONTRIBUTING.md


%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.11.0-0.3.git129f332
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Jun 28 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.0-0.2.20180628git129f332
- Bump to commit 129f332d72facda5d06f87e2b4e5e08bea0b6b44

* Thu Mar 22 2018 Robert-André Mauchin <zebob.m@gmail.com> - 0.11.0-0.1.20180417git50bfc56
- First package for Fedora

