"""
Gas: If the optimizer is enabled, using > 0 outside of a require statement is slightly more gas efficient than using ! = 0. Opposite applies for within a require statement (! = 0 is more efficient than > 0).

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasYesOptimizerInequalityCheck(AbstractDetector):
    """
    Gas: If the optimizer is enabled, using > 0 outside of a require statement is slightly more gas efficient than using ! = 0. Opposite applies for within a require statement (! = 0 is more efficient than > 0).
    """

    ARGUMENT = "yes-optimizer-inequality-efficiency"
    HELP = "Use ! = 0 within your require statements rather than > 0, and > 0 outside your require statements rather than ! = 0, to save gas."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#-0-is-cheaper-than--0-sometimes"
    WIKI_TITLE = "> 0 is cheaper than ! = 0 sometimes."
    WIKI_DESCRIPTION = "With optimizer enabled, using the > 0 inequality outside of any require statements is slightly more gas efficient than using ! = 0. The opposite applies inside a require statement, where ! = 0 rather than > 0 will be the more gas-efficient option." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
