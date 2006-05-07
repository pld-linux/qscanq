Summary:	Virus Scanning for Qmail
Summary(pl):	Skanowanie antywirusowe dla Qmaila
Name:		qscanq
Version:	0.43
Release:	0.2
License:	BSD-like
Group:		Applications
Source0:	http://jeenyus.net/~budney/software/qscanq/%{name}-%{version}.tar.gz
# Source0-md5:	f7fb2d5bb387feda34aac43dda857413
URL:		http://qscanq.org/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/qmail

%description
Qscanq scans every email message submitted to qmail before allowing it
to be added to qmail's mail queue. Infected emails are rejected, not
bounced, so you won't have to deal with double-bounces during virus
outbreaks. This program is not a malware scanner so you nead clamav or
AntiVir from Hbedv.

%description -l pl
Qscanq skanuje ka¿d± wiadomo¶æ e-mail dostarczon± do qmaila zanim
jeszcze bêdzie przeniesiona do kolejki poczty. Zara¿one wiadomo¶ci s±
odrzucane a nie odbijane, tak wiêc nie trzeba martwiæ siê o podwójne
odbicia podczas ataków wirusów. Ten program nie jest skanerem
antywirusowym, a wiêc potrzebuje clamava albo AntiVira z firmy Hbedv.

%prep
%setup -q -n mail

%build
cd %{name}-%{version}/src

echo '%{_prefix}' > home
echo '%{__cc} %{rpmcflags}' > conf-cc
echo '%{__cc}' > conf-ld
echo '%(id -un)
%(id -un)' > conf-users
echo '%(id -un)' > conf-groups

%{__make} -j1

%install
rm -rf $RPM_BUILD_ROOT
cd %{name}-%{version}/src
install -d $RPM_BUILD_ROOT%{_libexecdir}
install qscanq $RPM_BUILD_ROOT%{_libexecdir}
install cleanq $RPM_BUILD_ROOT%{_libexecdir}
install run-antivir $RPM_BUILD_ROOT%{_libexecdir}
install run-cleanq $RPM_BUILD_ROOT%{_libexecdir}
install install-post $RPM_BUILD_ROOT%{_libexecdir}
install install-cleanq $RPM_BUILD_ROOT%{_libexecdir}
install install-unwrap $RPM_BUILD_ROOT%{_libexecdir}
install install-wrap $RPM_BUILD_ROOT%{_libexecdir}
install qscanq-stdin $RPM_BUILD_ROOT%{_libexecdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{name}-%{version}/src/{Changelog,TODO,TEST-*}
%attr(755,root,root) %{_libexecdir}/cleanq
%attr(755,root,root) %{_libexecdir}/install-cleanq
%attr(755,root,root) %{_libexecdir}/install-post
%attr(755,root,root) %{_libexecdir}/install-unwrap
%attr(755,root,root) %{_libexecdir}/install-wrap
%attr(755,root,root) %{_libexecdir}/qscanq
%attr(755,root,root) %{_libexecdir}/qscanq-stdin
%attr(755,root,root) %{_libexecdir}/run-antivir
%attr(755,root,root) %{_libexecdir}/run-cleanq
