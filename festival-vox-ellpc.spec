Summary:	Castillian Spanish male voice
Summary(pl):	Kastylia�ska odmiana hiszpa�skiego - g�os m�ski
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

%description -l pl
Ten pakiet udost�pnia g�os m�ski dla kastylia�skiej odmiany j�zyka
hiszpa�skiego. U�ywa wzbudzanej szcz�tkowo dwug�oskowej metody syntezy
LPC. Leksykon jest udost�pniony jako zestaw regu� przypisuj�cych
d�wi�ki literom, powoduj�cych akcenty wymowy i sylabizacj�. Czasy
trwania, intonacja i frazy prozodyczne s� minimalne, ale akceptowalne
dla prostych przyk�ad�w.

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
