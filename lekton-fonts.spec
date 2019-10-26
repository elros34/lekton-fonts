Name:    lekton-fonts
Version: 0.1
Release: 1
Summary: Monospaced Typewriter Font

Group:     User Interface/X
License:   SIL OPEN FONT LICENSE Version 1.1 
URL:       https://fonts.google.com/specimen/Lekton
Source0:   Lekton.tar.gz
Source1:   %{name}-fontconfig.conf

BuildArch:     noarch
BuildRequires: fontpackages-devel
Requires: fontpackages-filesystem

%description
Lekton has been designed at ISIA Urbino, Italy, and is inspired by some of the typefaces used on the Olivetti typewriters.
It was designed by: Paolo Mazzetti, Luciano Perondi, Raffaele Flaùto, Elena Papassissa, Emilio Macchia, Michela Povoleri, Tobias Seemiller, Riccardo Lorusso, Sabrina Campagna, Elisa Ansuini, Mariangela Di Pinto, Antonio Cavedoni, Marco Comastri, Luna Castroni, Stefano Faoro, Daniele Capo, and Jan Henrik Arnold.



%prep
%setup -n Lekton

%build

%install
rm -fr %{buildroot}

install -m 0755 -d %{buildroot}%{_fontdir}

install -m 0644 -p *.ttf %{buildroot}%{_fontdir}

install -m 0755 -d %{buildroot}%{_fontconfig_templatedir} \
                   %{buildroot}%{_fontconfig_confdir}

install -m 0644 -p %{SOURCE1} \
        %{buildroot}%{_fontconfig_templatedir}/95-lekton.conf

ln -s %{_fontconfig_templatedir}/95-lekton.conf \
        %{buildroot}%{_fontconfig_confdir}/95-lekton.conf

%clean
rm -fr %{buildroot}


%_font_pkg -n lekton -f ??-lekton.conf Lekton-Regular.ttf Lekton-Italic.ttf Lekton-Bold.ttf
%doc *.txt

