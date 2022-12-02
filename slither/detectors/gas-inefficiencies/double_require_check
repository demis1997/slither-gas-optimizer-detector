"""
Gas: Using double require rather than && operator saves gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasDoubleRequireCheck(AbstractDetector):
    """
    Gas: Using double require rather than && operator saves gas.
    """

    ARGUMENT = "double-require-check"
    HELP = "Replace && with double require to save gas."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-double-require-instead-of-operator-"
    WIKI_TITLE = "Use Double Require Instead of Operator &&"
    WIKI_DESCRIPTION = "Usage of double require will save you around 10 gas with the optimizer enabled." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
