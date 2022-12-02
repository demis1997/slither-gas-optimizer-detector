"""
Gas: Changing constant keccak variables to immutable will save gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasConstantImmutableCheck(AbstractDetector):
    """
    Gas: Changing constant keccak variables to immutable will save gas.
    """

    ARGUMENT = "constant-to-immutable-check"
    HELP = "The keccak variable can be changed to immutable rather than constant."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#change-constant-to-immutable-for-keccak-variables"
    WIKI_TITLE = "Change Constant to Immutable for keccak Variables"
    WIKI_DESCRIPTION = "Saving keccak variables as constants results in hashing being done whenever the variable is used. Extra hashing means extra gas. Changing these keccak variables from constant to immutable will save gas." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
