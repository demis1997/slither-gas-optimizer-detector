"""
Gas: Using custom errors as opposed to revert strings is more convenient and gas-efficient.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasCustomErrorCheck(AbstractDetector):
    """
    Gas: Using custom errors as opposed to revert strings is more convenient and gas-efficient.
    """

    ARGUMENT = "custom-error-check"
    HELP = "Custom errors allow for a more convenient and gas-efficient way of explaining to users why an operation failed."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-custom-errors-instead-of-revert-strings-to-save-gas"
    WIKI_TITLE = "Use Custom Errors Instead of Revert Strings To Save Gas"
    WIKI_DESCRIPTION = "Custom errors from Solidity 0.8.4 are cheaper than revert strings (cheaper deployment cost and runtime cost when the revert condition is met)." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
