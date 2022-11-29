"""
Gas: Module detecting Array length inside of loop

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType
from slither.slithir.operations import Send, Transfer, LowLevelCall
from slither.slithir.operations import Call

class GasInefficientLoopLength(AbstractDetector):
    """
    Gas: Array length inside of loop
    """

    ARGUMENT = "gas-length-within-for-loop"
    HELP = "Gas Inefficiencies Detected"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/crytic/slither/wiki/Detector-Documentation#missing-zero-address-validation"
    WIKI_TITLE = "Caching the length in for loops"
    WIKI_DESCRIPTION = "Reading array length at each iteration of the loop takes 6 gas" 
    