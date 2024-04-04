Name: opentelemetry-collector-cloudwatch-config
Version: 1.0
Release: 2%{?dist}
Summary: Observability cloudwatch integration
BuildArch: noarch

License: Apache-2.0
Source1: config.yaml
Source2: opentelemetry-collector-cloudwatch-config.service

# Necessary to access the systemd macros
BuildRequires: systemd
Requires: opentelemetry-collector

%description
RHEL observability configuration for AWS cloudwatch integration.

%install
# create expected directory layout
mkdir -p %{buildroot}%{_sysconfdir}/opentelemetry-collector-cloudwatch-config
mkdir -p %{buildroot}%{_unitdir}

# install files
install -p -m 0644 -D %{SOURCE1} %{buildroot}%{_sysconfdir}/opentelemetry-collector-cloudwatch-config/config.yaml
install -p -m 0644 -D %{SOURCE2} %{buildroot}%{_unitdir}/%{name}.service

%post
/bin/systemctl --system daemon-reload 2>&1

%preun
if [ $1 -eq 0 ]; then
    /bin/systemctl --quiet stop %{name}.service
    /bin/systemctl --quiet disable %{name}.service
fi

%posttrans
/bin/systemctl is-enabled %{name}.service >/dev/null 2>&1
if [  $? -eq 0 ]; then
    /bin/systemctl restart %{name}.service >/dev/null
fi

%files
%{_unitdir}/%{name}.service
%{_sysconfdir}/opentelemetry-collector-cloudwatch-config/config.yaml

%changelog
* Thu Apr 04 2024 Felix Kolwa <fkolwa@redhat.com> - 1.0-2
- fix binary and config path in service file.
- version bump

* Wed Feb 7 2024 Nina Olear <nolear@redhat.com> - 1.0-1
- Adding installation routine for config and service file
