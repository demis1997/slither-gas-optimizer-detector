"""
Gas: Module detecting default variable initialization

"""
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.analyses.callgraph import CallGraph
from slither.solc_parsing import parse_from_input_string
from slither.core.solidity_types.elementary_type import ElementaryType

class DefaultVariableInitialization(AbstractDetector):
    """
    Gas: Default Variable Initialization
    """

    ARGUMENT = "default-variable-initialization"
    HELP = "The variable can simply be declared instead of initialized to its default value"
    IMPACT = DetectorClassification.LOW
    CONFIDENCE = DetectorClassification.MEDIUM

    WIKI = "https://github.com/demis1997/slither-gas-optimizer-detector/wiki/Solidity-Gas-Optimizations-and-Tricks#no-need-to-explicitly-initialize-variables-with-default-values"
    WIKI_TITLE = "No need to explicitly initialize variables with default values"
    WIKI_DESCRIPTION = "If a variable is not set/initialized, it is assumed to have the default value (0 for uint, false for bool, address(0) for address, etc.). Explicitly initializing it with its default value is an anti-pattern and wastes gas."

    def _get_variable_initialization(self, contract):
        """
        Get the initialization code for each variable in the contract
        """
        variable_init = {}
        for variable in contract.variables:
            if isinstance(variable.type, ElementaryType):
                variable_init[variable.name] = variable.initial_value
        return variable_init

    def _check_for_default_initialization(self, variable_init):
        """
        Check if any variable is explicitly initialized with its default value
        """
        for variable, value in variable_init.items():
            if value is not None and value != '0':
                return True
        return False

    def analyze(self):
        """
        Analyze the contract for default variable initialization
        """
        for contract in self.contracts:
            variable_init = self._get_variable_initialization(contract)
            if self._check_for_default_initialization(variable_init):
                self.alert(f"Contract {contract.name} explicitly initializes variables with default values.", contract=contract)
