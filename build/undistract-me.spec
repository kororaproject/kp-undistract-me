Name:           undistract-me
Version:        14.6
Release:        1%{?dist}
Summary:        Alerts you when long-running commands finally complete.

Group:          System Environment/Base
License:        CC-BY-SA
URL:            https://launchpad.net/undistract-me
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch
Requires:       libnotify

%description
Some commands take ages to run!
You're doing some work, and as part of that you need to run a command on the
terminal that takes a little while to finish. Perhaps it's your test suite,
your build process, or an unusually big data run.

Watching commands is boring!
You run the command, watch it for maybe a second and then switch to doing
something else—answering email or something more useful and fun than staring
at a terminal.

Time flies when you're distracted!
You get so deeply involved in your email that twenty minutes fly by. When you
switch back to your terminal the command has finished, but you've got no idea
whether it was nineteen seconds ago or nineteen minutes ago.

Undistract me, please!
This happens to me a lot. I'm not prescient enough to predict which commands
will take a long time, and I'm not disciplined to add something to the end of
each one. If you are like me, then what we both need is something that alerts
us whenever long running commands finish.

This is it!

%prep
%setup -q

%build
# nada

%install
filterdir=$RPM_BUILD_ROOT/%{_sysconfdir}/undistract-me
profiledir=$RPM_BUILD_ROOT/%{_sysconfdir}/profile.d
targetdir=$RPM_BUILD_ROOT/%{_datadir}/undistract-me
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $filterdir
install -d -m 0755 $profiledir
install -d -m 0755 $targetdir
install -m 0644 LICENSE $targetdir
install -m 0644 *.bash $targetdir
install -m 0644 ignore $filterdir
install -m 0644 undistract-me.sh $profiledir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir %{_sysconfdir}/profile.d
%dir %{_sysconfdir}/undistract-me
%dir %{_datadir}/undistract-me
%{_datadir}/undistract-me/LICENSE
%{_datadir}/undistract-me/*.bash
%{_sysconfdir}/profile.d/undistract-me.sh
%config(noreplace) %{_sysconfdir}/undistract-me/ignore

%changelog
* Sat Jul 26 2014 Ian Firns <firnsy@kororaproject.org> - 12.1.4-1
- Merged upstream changes.

* Mon Sep 9 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.4-1
- Merged upstream changes and added pre-population of LONG_COMMAND_IGNORE_LIST when invoking

* Tue Apr 30 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.3-4
- Tweaked output messaging to be even less verbose.

* Wed Jan 30 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.3-3
- Tweaked output messaging to be less verbose.

* Tue Jan 29 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.3-2
- Added system and user level filtering for commands that don't necessitate
notification of completion.

* Tue Jan 15 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.3-1
- Initial spec.

