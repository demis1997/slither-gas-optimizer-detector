"""
Gas: Using calldata instead of memory for read-only external function parameters will reduce gas fees as well as contract deployment time cost.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasCalldataParameterCheck(AbstractDetector):
    """
    Gas: Using calldata instead of memory for read-only external function parameters will reduce gas fees as well as contract deployment time cost.
    """

    ARGUMENT = "calldata-function-parameter-check"
    HELP = "You can use calldata as storage location in a function rather than memory, if the function is external and read-only."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-calldata-instead-of-memory-for-function-parameters"
    WIKI_TITLE = "Use calldata Instead of Memory for Function Parameters"
    WIKI_DESCRIPTION = "In some cases, having function arguments in calldata instead of memory is more optimal. When arguments are read-only on external functions, the data location should be calldata." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
