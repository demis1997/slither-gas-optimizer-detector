"""
Gas: The increment in the for loop post condition can be made unchecked

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType
from slither.slithir.operations import Send, Transfer, LowLevelCall
from slither.slithir.operations import Call

class GasInefficientLoopCheck(AbstractDetector):
    """
    Gas: Checked variable increment
    """

    ARGUMENT = "gas-chekced-increment-for-loop"
    HELP = "The increment in the for loop post condition can be made unchecked"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/crytic/slither/wiki/Detector-Documentation#missing-zero-address-validation"
    WIKI_TITLE = "The increment in the for loops post condition can be made unchecked"
    WIKI_DESCRIPTION = "Overflow checks are made by the compiler and you can use unchecked within the for loop to save gas" 
    