%include	/usr/lib/rpm/macros.php
%define		_class		Payment
%define		_subclass	Process
%define		_status		beta
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - unified payment processor
Summary(pl):	%{_pearname} - zunifikowany procesor zap³at
Name:		php-pear-%{_pearname}
Version:	0.5.6
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f0ea3ba9ba2160164a72fbe32fface0b
URL:		http://pear.php.net/package/Payment_Process/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Payment_Process is a gateway-independent framework for processing
credit cards, and eventually e-checks and other forms of payments as
well.

This class has in PEAR status: %{_status}.

%description -l pl
Payment_Process dostarcza niezale¿nego ¶rodowiska do przetwarzania
op³at za pomoc± kart kredytowych, czeków elektronicznych lub innych
form p³atno¶ci.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Type

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}
install %{_pearname}-%{version}/%{_subclass}/Type/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}/Type

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/examples
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
