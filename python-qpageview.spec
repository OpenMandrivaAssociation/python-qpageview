%define	pypi_name qpageview

# ATM the build fails... too lazy to investigate why
%bcond_with docs

Summary:	Widget to display page-based documents for Qt6/PyQt6
Name:	python-%{pypi_name}
Version:	1.0.1
Release:	1
License:	GPLv3+
Group:	Development/Python
# See also: https://qpageview.org/
Url:	https://github.com/frescobaldi/qpageview
Source0:	https://files.pythonhosted.org/packages/source/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:		noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3dist(hatchling)
BuildRequires:	python3dist(pip)
BuildRequires:	python3dist(pyproject-api)
BuildRequires:	python3dist(setuptools)
BuildRequires:	python3dist(sphinx)
BuildRequires:	python3dist(wheel)
BuildRequires:	python-cups
BuildRequires:	python-docs
BuildRequires:	python-qt6-devel >= 6.6

Provides:	%{pypi_name} = %{version}-%{release}
Requires:	python-cups
Requires:	python-qt6-core
Requires:	python-qt6-gui
Requires:	python-qt6-pdf
Requires:	python-qt6-printsupport
Requires:	python-qt6-svg
Requires:	python-qt6-widgets

%description
The qpageview module provides a page based document viewer widget for
Qt6/PyQt6. It has a flexible architecture potentionally supporting many
formats. Currently, it supports SVG documents, images, and PDF documents.

%files 
%license LICENSE docs/source/license.rst
%if %{with docs}
%doc html 
%endif
%doc README.rst
%{py_puresitedir}/%{pypi_name}*

#-----------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

%if %{with docs}
# Use local objects.inv for intersphinx
sed -e "s|\('https://docs\.python\.org/3', \)None|\1'%{_docdir}/python3-docs/html/objects.inv'|" \
  -i docs/source/conf.py
%endif

  
%build
%py_build

%if %{with docs}
# Generate html docs
PYTHONPATH=${PWD} sphinx-build docs/source html
# Remove sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}
%endif


%install
%py_install
