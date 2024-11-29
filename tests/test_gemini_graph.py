
import unittest
from algorithms.graph.graph import Node, DirectedEdge, DirectedGraph


class TestNodeGeminiTest(unittest.TestCase):
    def test_gemini_node_get_name(self):
        node = Node("A")
        self.assertEqual("A", Node.get_name(node))
        self.assertEqual("A", Node.get_name("A"))
        self.assertEqual("", Node.get_name(1))

    def test_gemini_node_eq(self):
        node1 = Node("A")
        node2 = Node("A")
        self.assertEqual(node1, node2)
        self.assertEqual(node1, "A")

    def test_gemini_node_repr(self):
        node = Node("A")
        self.assertEqual("A", repr(node))

    def test_gemini_node_ne(self):
        node1 = Node("A")
        node2 = Node("B")
        self.assertNotEqual(node1, node2)
        self.assertNotEqual(node1, "B")

    def test_gemini_node_lt(self):
        node1 = Node("A")
        node2 = Node("B")
        self.assertLess(node1, node2)

    def test_gemini_node_le(self):
        node1 = Node("A")
        node2 = Node("B")
        self.assertLessEqual(node1, node2)
        self.assertLessEqual(node1, node1)

    def test_gemini_node_gt(self):
        node1 = Node("A")
        node2 = Node("B")
        self.assertGreater(node2, node1)

    def test_gemini_node_ge(self):
        node1 = Node("A")
        node2 = Node("B")
        self.assertGreaterEqual(node2, node1)
        self.assertGreaterEqual(node1, node1)

    def test_gemini_node_bool(self):
        node1 = Node("A")
        node2 = Node("")
        self.assertTrue(bool(node1.name))
        self.assertFalse(bool(node2.name))


class TestDirectedEdgeGeminiTest(unittest.TestCase):
    def test_gemini_directed_edge_eq(self):
        edge1 = DirectedEdge(Node("A"), Node("B"))
        edge2 = DirectedEdge(Node("A"), Node("B"))
        self.assertEqual(edge1, edge2)
        self.assertNotEqual(edge1, 1)

    def test_gemini_directed_edge_repr(self):
        edge = DirectedEdge(Node("A"), Node("B"))
        self.assertEqual("(A -> B)", repr(edge))


class TestDirectedGraphGeminiTest(unittest.TestCase):
    def test_gemini_directed_graph_add_node(self):
        graph = DirectedGraph()
        graph.add_node("A")
        self.assertEqual(1, len(graph.nodes))
        graph.add_node("A")
        self.assertEqual(1, len(graph.nodes))

    def test_gemini_directed_graph_add_edge(self):
        graph = DirectedGraph()
        graph.add_node("A")
        graph.add_node("B")
        graph.add_edge("A", "B")
        self.assertEqual(1, len(graph.edges))
        graph.add_edge("A", "C")
        self.assertEqual(1, len(graph.edges))

    def test_gemini_directed_graph_init_with_dict(self):
        graph = DirectedGraph({"A": ["B", "C"], "B": ["C"]})
        self.assertEqual(3, len(graph.nodes))
        self.assertEqual(3, len(graph.edges))
