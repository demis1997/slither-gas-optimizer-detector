"""
Gas: Using shift operators as opposed to multiplication/division operators where possible will save gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasShiftOperatorCheck(AbstractDetector):
    """
    Gas: Using shift operators as opposed to multiplication/division operators where possible will save gas.
    """

    ARGUMENT = "shift-operators-check"
    HELP = "Shift operators can be used in place of multiplication or division operators where possible."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-shift-rightleft-instead-of-divisionmultiplication-if-possible"
    WIKI_TITLE = "Use Shift Right/Left instead of Division/Multiplication if possible"
    WIKI_DESCRIPTION = "A division/multiplication by any number x being a power of 2 can be calculated by shifting log2(x) to the right or left." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
