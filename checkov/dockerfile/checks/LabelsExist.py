from __future__ import annotations

from typing import TYPE_CHECKING, List
import re

from checkov.common.models.enums import CheckCategories, CheckResult
from checkov.dockerfile.base_dockerfile_check import BaseDockerfileCheck

if TYPE_CHECKING:
    from dockerfile_parse.parser import _Instruction


class LabelCheck(BaseDockerfileCheck):

    def __init__(self, labels_to_check: List[dict]) -> None:
        name = "Ensure that specified LABEL instructions have been added to container images"
        id = "CKV_DOCKER_LABEL_CHECK"
        supported_instructions = ("*",)
        categories = (CheckCategories.NETWORKING,)
        self.labels_to_check = labels_to_check
        super().__init__(name=name, id=id, categories=categories, supported_instructions=supported_instructions)

    def scan_resource_conf(self, conf: dict[str, list[_Instruction]]) -> Tuple[CheckResult, Union[list[_Instruction], None]]:  # type:ignore[override]  # special wildcard behaviour
        
        label_pattern = re.compile(r'(\S+)=((["\'])([^\3]*?)\3)')
        label_pairs = {}

        for instruction, content in conf.items():
            if instruction == "LABEL":
                pairs = label_pattern.findall(content)
                for pair in pairs:
                    key, value = pair.split("=",1)
                    label_pairs[key] = value
        
        keys_present = label_pairs.keys()
        for mandatory_label in self.labels_to_check:
            if mandatory_label['key'] in keys_present:
                allowed_values_pattern = re.compile(mandatory_label['allowed_values'])
                if allowed_values_pattern.match(label_pairs[mandatory_label['key']]):
                    continue
                else:
                    self.details.append("Label "+mandatory_label['key']+" exists but does not match allowed values "+mandatory_label['allowed_values'])
                    return CheckResult.FAILED, None
            else:
                self.details.append("Label "+mandatory_label['key']+" does not exist")
                return CheckResult.FAILED, None

labels_to_check = [
    {
        "key": "John Doe",
        "allowed_values": ".*",
        "version": "1.0",
        "description": "A sample label"
    },
    {
        "key": "workload",
        "allowed_values": ".*",
        "version": "1.0",
        "description": "A sample label"
    }
]

check = LabelCheck(labels_to_check)