"""
Gas: Using a modifier instead of a function will save gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasModifierCheck(AbstractDetector):
    """
    Gas: Using a modifier instead of a function will save gas.
    """

    ARGUMENT = "modifier-check"
    HELP = "Rather than writing a function, you could trade that out for a modifier that does the same thing."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-modifiers-instead-of-functions-to-save-gas"
    WIKI_TITLE = "Use Modifiers Instead of Functions To Save Gas"
    WIKI_DESCRIPTION = "It is more efficient gas-wise to deploy with a modifier where applicable rather than with a function." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
