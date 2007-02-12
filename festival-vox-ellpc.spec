Summary:	Castillian Spanish male voice
Summary(pl.UTF-8):	Kastyliańska odmiana hiszpańskiego - głos męski
Name:		festival-vox-ellpc
Version:	0.1
Release:	3
License:	non-commercial use
Group:		Applications/Sound
Source0:	http://www.cstr.ed.ac.uk/download/festival/1.4.2/festvox_ellpc11k.tar.gz
# Source0-md5:	e96a97644d36fcb89952ca65c283cea3
Requires:	festival
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This voice provides a Castilian Spanish male voice using a
residual excited LPC diphone synthesis method.  The lexicon
is provived by a set of letter to sound rules producing pronunciation
accents and syllabification.  The durations, intonation and
prosodic phrasing are minimal but are acceptable for simple
examples.

%description -l pl.UTF-8
Ten pakiet udostępnia głos męski dla kastyliańskiej odmiany języka
hiszpańskiego. Używa wzbudzanej szczątkowo dwugłoskowej metody syntezy
LPC. Leksykon jest udostępniony jako zestaw reguł przypisujących
dźwięki literom, powodujących akcenty wymowy i sylabizację. Czasy
trwania, intonacja i frazy prozodyczne są minimalne, ale akceptowalne
dla prostych przykładów.

%prep
%setup -q -c

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
