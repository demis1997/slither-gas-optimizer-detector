"""
Gas: If there are many zeroes in an address, consider packing them into the same storage slot and simply prepending the necessary amount of zeroes before them. This will save you storage space.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasZeroCheck(AbstractDetector):
    """
    Gas: If there are many zeroes in an address, consider packing them into the same storage slot and simply prepending the necessary amount of zeroes before them. This will save you storage space.
    """

    ARGUMENT = "zero-check"
    HELP = "If the address has many zeroes in a row, pack them into the same storage slot and prepend the necessary amount of zeroes when you want to use them."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#using-addresses-with-lots-of-leading-zeroes"
    WIKI_TITLE = "Using Addresses With Lots of Leading Zeroes"
    WIKI_DESCRIPTION = "Because of the leading zeroes, you can pack them both into the same storage slot, then just prepend the necessary amount of zeroes when using them. This saves you storage when doing things such as checking the owner of a contract." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
