Summary:	Castillian Spanish male voice
Name:		festival-vox-ellpc
Version:	0.1
Release:	1
License:	Non-commercial use, distributable
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_ellpc11k.tar.gz
Requires:	festival
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides a Castilian Spanish male voice using a
residual excited LPC diphone synthesis method.  The lexicon
is provived by a set of letter to sound rules producing pronunciation
accents and syllabification.  The durations, intonation and
prosodic phrasing are minimal but are acceptable for simple
examples.

%prep
%setup -q -c %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices

cd festival/lib/voices
cp -r spanish $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices
rm $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/spanish/el_diphone/COPYING

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc festival/lib/voices/spanish/el_diphone/COPYING
%{_datadir}/festival/lib/voices/spanish
