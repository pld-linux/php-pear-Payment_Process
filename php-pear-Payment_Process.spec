%define		_status		beta
%define		_pearname	Payment_Process
Summary:	%{_pearname} - unified payment processor
Summary(pl.UTF-8):	%{_pearname} - zunifikowany procesor zapłat
Name:		php-pear-%{_pearname}
Version:	0.6.8
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	5a6467693eace7bc89a8ce4de4e3bff3
URL:		http://pear.php.net/package/Payment_Process/
BuildRequires:	php-pear-PEAR >= 1:1.4.11
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.6.2
Requires:	php-pear-Validate_Finance_CreditCard >= 0.5.2
Suggests:	php-pear-Net_Curl
Suggests:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(XML/Parser.*) pear(Net/Curl.*)

%description
Payment_Process is a gateway-independent framework for processing
credit cards, and eventually e-checks and other forms of payments as
well.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Payment_Process dostarcza niezależnego środowiska do przetwarzania
opłat za pomocą kart kredytowych, czeków elektronicznych lub innych
form płatności.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup

mv docs/%{_pearname}/examples .

install -d docs
mv .%{php_pear_dir}/data/Payment_Process/TODO docs/%{_pearname}

# what are those really? examples or classes?
mv .%{php_pear_dir}/docs/Payment_Process/Process examples

# package.xml for Payment_Process_Litle (wtf is it doing here?)
rm .%{php_pear_dir}/data/Payment_Process/package_Litle.xml

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/%{_pearname}/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Payment/*.php
%{php_pear_dir}/Payment/Process

%{_examplesdir}/%{name}-%{version}
