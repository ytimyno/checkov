## Run
cd checkov/dockerfile/extra_checks/extra_test
checkov -d images/ --external-checks-dir ../../extra_checks --framework dockerfile -c CKV_DOCKER_LABEL_CHECK

## Customise

Customise with policy.json as needed. Else, it will use a pre-def set of values. To customise a file, it needs to be in the dir where checkov runs from (see future work).

## Overall Things to Do:

- Combine Checks: Explore combining Cloud-Native (CN) and traditional IaC checks into a unified metadata validation approach.
- Customize Input Paths: Customize the path to input files (policy.json, cloud_specific_configurations.json) for higher flexibility.