"""
Gas: Make sure your struct and contract variables are packed in a way that the variables will sequentially climb up to 256 bits. This will save you gas in deployment.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasVariablePackCheck(AbstractDetector):
    """
    Gas: Make sure your struct and contract variables are packed in a way that the variables will sequentially climb up to 256 bits. This will save you gas in deployment.
    """

    ARGUMENT = "pack-order-check"
    HELP = "Variable packing in a contract or struct should go from low to high bitsize and should lead up to 256."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#pack-structs-in-solidity"
    WIKI_TITLE = "Pack Structs in Solidity"
    WIKI_DESCRIPTION = "It is more gas efficient if your variables, both in structs and in the contract, are packed in a way that begins from the lower bitsize to 256." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
