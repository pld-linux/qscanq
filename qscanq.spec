#
Summary:	Virus Scanning for Qmail
Summary(pl):	Skanowanie virus�w dla Qmaila
Name:		qscanq
Version:	0.43
Release:	0.1
License:	BSD-like
Group:		Applications
Source0:	http://jeenyus.net/~budney/software/qscanq/%{name}-%{version}.tar.gz
# Source0-md5:	f7fb2d5bb387feda34aac43dda857413
URL:		http://qscanq.org/
Requires:	qmail
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qscanq scans every email message submitted to qmail before allowing it
to be added to qmail's mail queue. Infected emails are rejected, not
bounced, so you won't have to deal with double-bounces during virus
outbreaks. This program is not a malware scanner so you nead clamav or
AntiVir from Hbedv.

%description -l pl
Qscanq skanuje ka�d� wiadomo�� email dostarczon� do qmaila zanim
jeszcze b�dzie przeniesiona do kolejki poczty. Zara�one wiadomo�ci s�
odrzucane a nie odbijane, tak wi�c nie b�dziesz musia� martwi� si� o
podw�jne odbicia podczas atak�w wirus�w. Ten program nie jest skanerem
antywirusowym a wi�c b�dziesz potrzebowa� clamava albo AntiVira z
firmy Hbedv.

%prep
%setup -q -n mail/%{name}-%{version}

%build
cd src
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*

%attr(755,root,root) %{_bindir}/*

%{_datadir}/%{name}

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}