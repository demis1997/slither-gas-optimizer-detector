"""
Gas: The ++ operator should be written before the variable

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasVariableIncrementCheck(AbstractDetector):
    """
    Gas: Variable increments cost less gas if they are before the variable
    """

    ARGUMENT = "gas-pre-variable-increment"
    HELP = "The increment of the variable can be placed before the variable"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#i-costs-less-gas-compared-to-i-or-i--1"
    WIKI_TITLE = "The increment in the for loops post condition can be added before the variable"
    WIKI_DESCRIPTION = "using ++i instead of i++ saves gas" 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
