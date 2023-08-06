from enum import Enum

from protocols.core.datagen_protocol.resources.expressions_presets.anger import ANGER_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.contempt import CONTEMPT_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.disgust import DISGUST_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.fear import FEAR_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.happiness import HAPPINESS_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.open_mouth import OPEN_MOUTH_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.sadness import SADNESS_PRESET
from protocols.core.datagen_protocol.resources.expressions_presets.surprise import SURPRISE_PRESET
from protocols.core.datagen_protocol.schema.humans.human import ExpressionName


class ExpressionPresets(Enum):
    ANGER = ExpressionName.ANGER, ANGER_PRESET
    CONTEMPT = ExpressionName.CONTEMPT, CONTEMPT_PRESET
    DISGUST = ExpressionName.DISGUST, DISGUST_PRESET
    FEAR = ExpressionName.FEAR, FEAR_PRESET
    HAPPINESS = ExpressionName.HAPPINESS, HAPPINESS_PRESET
    OPEN_MOUTH = ExpressionName.MOUTH_OPEN, OPEN_MOUTH_PRESET
    SADNESS = ExpressionName.SADNESS, SADNESS_PRESET
    SURPRISE = ExpressionName.SURPRISE, SURPRISE_PRESET
    NONE = ExpressionName.NEUTRAL, {}

    def __new__(cls, *args, **kwds):
        obj = object.__new__(cls)
        obj._value_ = args[0]
        return obj

    def __init__(self, _: str, expression_preset: dict):
        self.expression_preset = expression_preset

    def get_expression_prest(self) -> dict:
        return self.expression_preset
