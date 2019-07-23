Name:	javatest
Summary:	java test
Version:	1.0
Release:	0.0
License:	Apache-2.0
Source0:	javatest-%{version}.tar.gz

BuildRequires:	openjdk
BuildRequires:	openjdk-jre
BuildRequires:	openjdk-jre-essentials

%description
NOTHING TO SAY

%prep
%setup -q

%build
javac HelloWorld.java

%files
