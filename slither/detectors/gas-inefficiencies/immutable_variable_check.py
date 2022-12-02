"""
Gas: Setting state variables as immutable where possible will save gas.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasImmutableVariableCheck(AbstractDetector):
    """
    Gas: Setting state variables as immutable where possible will save gas.
    """

    ARGUMENT = "immutable-variable-check"
    HELP = "A state variable that will remain constant can be set as immutable to save gas."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#change-state-variables-to-immutable-where-possible"
    WIKI_TITLE = "Change state variables to immutable where possible"
    WIKI_DESCRIPTION = "Setting contract-level state variables to immutable at construction time will store the variable in code rather than storage. Any subsequent reads will be done by the push32 value instruction, rather than sload, making it much more gas-efficient." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
