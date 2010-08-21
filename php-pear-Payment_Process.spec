%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	Process
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}
Summary:	%{_pearname} - unified payment processor
Summary(pl.UTF-8):	%{_pearname} - zunifikowany procesor zapłat
Name:		php-pear-%{_pearname}
Version:	0.6.6
Release:	2
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	8137979f1f965ed0d94fa07755125836
URL:		http://pear.php.net/package/Payment_Process/
BuildRequires:	php-pear-PEAR >= 1:1.4.0-0.b1
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php-common >= 3:4.2.0
Requires:	php-pear
Requires:	php-pear-Validate >= 0.5.0
Requires:	php-pear-Validate_Finance_CreditCard >= 0.5.0
Suggests:	php-pear-Net_Curl
Suggests:	php-pear-XML_Parser
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(XML/Parser.*)' 'pear(Net/Curl.*)'

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

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

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
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
