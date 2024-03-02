# Created by pyp2rpm-3.3.8
%define pypi_name qpageview

Name:           python-%{pypi_name}
Version:        0.6.2
Release:        1
Summary:        Widget to display page-based documents for Qt5/PyQt5
Group:          Development/Python
License:        GPLv3+ AND GPLv2+
# https://github.com/frescobaldi/qpageview
URL:            https://qpageview.org/
Source0:        https://files.pythonhosted.org/packages/source/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
BuildRequires:  python-qt5-devel
BuildRequires:  python-docs

Provides:       %{pypi_name} = %{version}-%{release}
Requires:       python-qt5-core
Requires:       python-qt5-gui
Requires:       python-qt5-printsupport
Requires:       python-qt5-svg
Requires:       python-qt5-widgets
Requires:       python-poppler-qt5

%description
The qpageview module provides a page based document viewer widget
for Qt5/PyQt5.
It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and,
using the Poppler-Qt5 binding, PDF documents.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
  -i docs/source/conf.py

%build
%py_build

# generate html docs
PYTHONPATH=${PWD} sphinx-build-3 docs/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}

%install
%py_install

%files 
%doc html README.rst
%license LICENSE docs/source/license.rst
%{python_sitelib}/%{pypi_name}*
