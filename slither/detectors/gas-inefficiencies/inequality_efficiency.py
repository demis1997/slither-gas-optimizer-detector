"""
Gas: Using non-strict inequalities (>=) is more efficient gas-wise than using strict inequalities (>).

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasInequalityEfficiencyCheck(AbstractDetector):
    """
    Gas: Using non-strict inequalities (>=) is more efficient gas-wise than using strict inequalities (>).
    """

    ARGUMENT = "inequality-efficiency-check"
    HELP = "Switch out non-strict inequalities (>=) for strict ones (>) to save gas."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#-is-cheaper-than-"
    WIKI_TITLE = ">= is cheaper than >"
    WIKI_DESCRIPTION = "Non-strict inequalities (>=) are cheaper than strict ones (>). This is due to some supplementary checks (ISZERO, 3 gas))." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
