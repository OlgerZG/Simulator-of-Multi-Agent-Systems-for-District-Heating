import unittest
import inspect

from objects import*
from inputs import*

# python -m unittest test.py 

class TestSim(unittest.TestCase):

    def test_agent_data_structure(self):
        with self.subTest(i=1):
            heater = agent("a", 5)
            self.assertEqual(heater.name, "a")

    def test_print_connections(self):
        agent1 = agent("Agent 1",1,5)
        agent2 = agent("Agent 2",1,5)
        agent3 = agent("Agent 3",1,5)

        agent1.add_link(agent2, agent3)

        expected = "Agent 1 is linked to: Agent 2 Agent 3 "
        
        self.assertEqual(expected, agent1.get_connections_string())

'Agent 1 is linked to: Agent 2 Agent 3 '
'Agent 1 is linked to: Agent 2 Agent 3 '