"""
Gas: It is more gas efficient to declare a storage variable and use it than to repeatedly fetch the reference in a map or array.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasStorageDeclarationCheck(AbstractDetector):
    """
    Gas: It is more gas efficient to declare a storage variable and use it than to repeatedly fetch the reference in a map or array.
    """

    ARGUMENT = "storage-declaration-check"
    HELP = "You can streamline the referencing of a storage variable by declaring and using it, rather than fetching the variable repeatedly in a map or an array."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#help-the-optimizer-by-saving-a-storage-variables-reference"
    WIKI_TITLE = "Help the Optimizer by Saving a Storage Variable’s Reference"
    WIKI_DESCRIPTION = "To help the optimizer, declare a storage type variable and use it instead of repeatedly fetching the reference in a map or an array. The effect can be quite significant." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
