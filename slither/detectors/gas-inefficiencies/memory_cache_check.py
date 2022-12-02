"""
Gas: Caching storage variables into memory is cheaper than reading it directly from storage every time.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasMemoryCacheCheck(AbstractDetector):
    """
    Gas: Caching storage variables into memory is cheaper than reading it directly from storage every time.
    """

    ARGUMENT = "memory-cache-check"
    HELP = "Consider caching your storage variables into memory rather than in storage. It is much more efficient gas-wise when reading the variable if it is cached in memory."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#caching-storage-variables-in-memory-to-save-gas"
    WIKI_TITLE = "Caching Storage Variables in Memory To Save Gas"
    WIKI_DESCRIPTION = "Anytime you are reading from storage more than once, it is cheaper in gas cost to cache the variable in memory: a SLOAD cost 100gas, while MLOAD and MSTORE cost 3 gas. Gas savings: at least 97 gas." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
