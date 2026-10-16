# test_glossarybay.py
"""
Tests for GlossaryBay module.
"""

import unittest
from glossarybay import GlossaryBay

class TestGlossaryBay(unittest.TestCase):
    """Test cases for GlossaryBay class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = GlossaryBay()
        self.assertIsInstance(instance, GlossaryBay)
        
    def test_run_method(self):
        """Test the run method."""
        instance = GlossaryBay()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
