"""
Gas: Consider using a clone when deploying a factory contract.

"""
from collections import defaultdict

from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType


class GasCloneApplicabilityCheck(AbstractDetector):
    """
    Gas: Consider using a clone when deploying a factory contract.
    """

    ARGUMENT = "clone-applicability-check"
    HELP = "If this is a factory contract, a clone will save you a lot of gas and provide identical function and utility."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#use-clones-for-cheap-contract-deployments"
    WIKI_TITLE = "Use Clones for Cheap Contract Deployments"
    WIKI_DESCRIPTION = "Porter Finance deployed using clones and found that it was 10x cheaper gas-wise. It is worth checking the wiki to see how you could make your factory contract a clone." 

    def _is_instance(self, ir):  # pylint: disable=no-self-use
        return isinstance(ir, VariableIncrements)
