"""
Gas: If the optimizer is disabled, using ! = 0 outside of a require statement is slightly more gas efficient than using > 0. Same costs for a require.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasNoOptimizerInequalityCheck(AbstractDetector):
    """
    Gas: If the optimizer is disabled, using ! = 0 outside of a require statement is slightly more gas efficient than using > 0. Same costs for a require.
    """

    ARGUMENT = "no-optimizer-inequality-efficiency"
    HELP = "Consider using ! = 0 outside of any require statements rather than > = 0 to save gas."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#-0-is-cheaper-than--0-sometimes"
    WIKI_TITLE = "> 0 is cheaper than ! = 0 sometimes."
    WIKI_DESCRIPTION = "With optimizer disabled, using the ! = 0 inequality outside of any require statements is slightly more gas efficient than using > 0." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
