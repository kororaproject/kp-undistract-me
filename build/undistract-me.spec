Name:           undistract-me
Version:        12.1.3
Release:        1%{?dist}
Summary:        Alerts you when long-running commands finally complete.

Group:          System Environment/Base
License:        CC-BY-SA
URL:            http://kororaproject.org
Source0:        %{name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildArch:      noarch

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
profiledir=$RPM_BUILD_ROOT/etc/profile.d
targetdir=$RPM_BUILD_ROOT/usr/share/undistract-me
rm -rf $RPM_BUILD_ROOT
install -d -m 0755 $profiledir
install -d -m 0755 $targetdir
install -m 0644 LICENSE $targetdir
install -m 0644 *.bash $targetdir
install -m 0644 undistract-me.sh $profiledir

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%dir /etc/profile.d
%dir /usr/share/undistract-me
/usr/share/undistract-me/LICENSE
/usr/share/undistract-me/*.bash
/etc/profile.d/undistract-me.sh

%changelog
* Tue Jan 15 2013 Ian Firns <firnsy@kororaproject.org> - 12.1.3-1
- Initial spec.

