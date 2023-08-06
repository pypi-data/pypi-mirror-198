from typing import List

from pydantic import validator

from datagen_protocol.schema import humans as humans_core_schema
from datagen_protocol.schema.humans import Mask, Glasses


class Accessories(humans_core_schema.Accessories):
    @validator("mask", "glasses", always=True)
    def glasses_and_masks_mutually_exclusive(cls, mask: Mask, glasses: Glasses) -> Mask:
        if mask and glasses:
            raise ValueError("Glasses and masks are mutually exclusive")
        return mask
