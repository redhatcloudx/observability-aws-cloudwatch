Name: rhel-observability-aws-cloudwatch
Version: 1.0
Release: 1%{?dist}
Summary: Observability cloudwatch integration

# Copy the config.yaml file to /etc/observability-aws/config.yaml
%files
/etc/observability-aws/config.yaml

# Install the systemd file
%post
systemctl daemon-reload
systemctl enable observability-aws-cloudwatch.service
systemctl start observability-aws-cloudwatch.service

