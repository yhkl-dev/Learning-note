import unitest
from nfa import *

class TestNFA(unitest.TestCase):

    def setUp(self):
        self.rulebook = DFARulebook(
                FARule(),
            ]
        )

    def test_rulebook(self):
        print(self.rulebook)
