"""
Gas: Explicitly initializing a variable with its default value wastes gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasDefaultVariableCheck(AbstractDetector):
    """
    Gas: Explicitly initializing a variable with its default value wastes gas.
    """

    ARGUMENT = "default-variable-initialization"
    HELP = "The variable can simply be declared instead of initialized to its default value"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#no-need-to-explicitly-initialize-variables-with-default-values"
    WIKI_TITLE = "No need to explicitly initialize variables with default values"
    WIKI_DESCRIPTION = "If a variable is not set/initialized, it is assumed to have the default value (0 for uint, false for bool, address(0) for address, etc.). Explicitly initializing it with its default value is an anti-pattern and wastes gas." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
