Summary:	Set of programs to see which routines in a C-project are used
Summary(pl):	Zestaw programów do monitorowania wykorzystywanych funkcji w C
Name:		usage
Version:	1.0
Release:	1
License:	improve-ware
Group:		Development/Languages
Source0:	http://members.lycos.nl/dpruimboom/%{name}.zip
# Source0-md5:	6318e9bc869d551686ccab0d09fb3667
Source1:	%{name}.redistribution
URL:		http://members.lycos.nl/dpruimboom/
BuildRequires:	flex
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This set of programs consist of 'usage' that can be used to see which
routines in a C-project are used and how often and what other routines
they call. Then there is the CallTree program, this program uses
output of the 'usage' program to make a call-tree of the C-project.

%description -l pl
Zestaw programów s³u¿±cych do monitorowania które funkcje w programach
C s± u¿ywane i jak czêsto inne funkcje je wywo³uj±. Jest te¿ program
CallTree, wykorzystuj±cy wyj¶cie z usage do stworzenia drzewa wywo³añ
w projekcie C.

%prep
%setup -q -n %{name}

%build
flex %{name}.lex
%{__cc} %{rpmcflags} -o %{name} lex.yy.c sys_nodelib.c -lfl
cd call_tree
%{__cc} %{rpmcflags} -o CallTree sys_nodelib.c CallTree.c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_sysconfdir}}

install %{name} call_tree/CallTree $RPM_BUILD_ROOT%{_bindir}
install %{name}.lst $RPM_BUILD_ROOT%{_sysconfdir}
install %{SOURCE1} $RPM_BUILD_DIR/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%verify(not md5 size mtime) %config(noreplace) %{_sysconfdir}/%{name}.lst
%doc Readme usage.redistribution
