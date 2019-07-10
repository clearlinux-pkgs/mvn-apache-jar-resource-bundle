#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-apache-jar-resource-bundle
Version  : 1.4
Release  : 2
URL      : https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar
Source0  : https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar
Source1  : https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar
Source2  : https://repo1.maven.org/maven2/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: mvn-apache-jar-resource-bundle-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-apache-jar-resource-bundle package.
Group: Data

%description data
data components for the mvn-apache-jar-resource-bundle package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.jar
/usr/share/java/.m2/repository/org/apache/apache-jar-resource-bundle/1.4/apache-jar-resource-bundle-1.4.pom
