import unittest
from memescan.contract_analysis import analyze_contract

class TestContractAnalysis(unittest.TestCase):
    def test_analyze_contract(self):
        result = analyze_contract("example_contract_address")
        self.assertIn("vulnerabilities", result)

if __name__ == "__main__":
    unittest.main()
