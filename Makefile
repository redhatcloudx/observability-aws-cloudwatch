SOURCES_DIR := SOURCES
SPECS_DIR := SPECS

RPM_SPEC_FILE := $(SPECS_DIR)/observability-aws-cloudwatch.spec
RPM_TARGET := rpm

SOURCE_FILES := config.yaml

$(RPM_TARGET): $(addprefix $(SOURCES_DIR)/,$(SOURCE_FILES))
    rpmbuild -ba $(RPM_SPEC_FILE)

$(SOURCES_DIR)/%.yaml: %.yaml
    cp $< $@
    
copr: $(addprefix $(SOURCES_DIR)/,$(SOURCE_FILES))
    rpmbuild -bs $(RPM_SPEC_FILE)
    copr-cli build miyunari/observability-aws-cloudwatch SRPMS/observability-aws-cloudwatch-1.0-1.fc39.src.rpm

