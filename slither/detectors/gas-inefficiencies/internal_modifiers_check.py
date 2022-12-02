"""
Gas: It is recommended to move require statements into internal virtual functions to save bytecode.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasInternalModifierCheck(AbstractDetector):
    """
    Gas: It is recommended to move require statements into internal virtual functions to save bytecode.
    """

    ARGUMENT = "internal-modifier-check"
    HELP = "Place require statements into internal virtual functions for smaller contract size."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-internal-view-functions-in-modifiers-to-save-bytecode"
    WIKI_TITLE = "Use internal view functions in modifiers to save bytecode"
    WIKI_DESCRIPTION = "Putting the require in an internal function decreases contract size when a modifier is used multiple times. There is no difference in deployment gas cost with private and internal functions.." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
