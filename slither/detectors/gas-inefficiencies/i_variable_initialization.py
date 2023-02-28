from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.slithir.operations import VariableIncrements
from slither.analyses.data_dependency.data_dependency import is_tainted
from slither.core.solidity_types.elementary_type import ElementaryType



class GasIVariableInitCheck(AbstractDetector):
    """
    Gas: Not initializing the i variable in a for loop will not save gas; it might take up more.
    """

    ARGUMENT = "i-variable-initialization"
    HELP = "The i variable should still be initializated in the for loop."
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#dont-remove-the-initialization-of-i-variable-in-for-loops"
    WIKI_TITLE = "Don't remove the initialization of i variable in for loops"
    WIKI_DESCRIPTION = "Removing the i variable initialization to outside of the loop is thought to save gas; it does not, and should remain within the for loop." 

    def _is_instance(self, ir):
        return isinstance(ir, VariableIncrements)

    def _process_contract(self, contract):
        for function in contract.functions:
            for ir in function.slithir:
                if isinstance(ir, For):
                    if is_tainted(ir.loop_variable, ir.start) or is_tainted(ir.loop_variable, ir.end) or is_tainted(ir.loop_variable, ir.step):
                        self._issues.append({"variable": ir.loop_variable.name, "location": ir.node_id})

"run slither analyze my_contract.sol GasIVariableInitCheck"