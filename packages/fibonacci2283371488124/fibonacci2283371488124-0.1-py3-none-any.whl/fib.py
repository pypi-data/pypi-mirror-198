def fibonacci(n):
    if n <= 0:
        return []

    fib_numbers = [0, 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers[:n]

print(fibonacci(10))

import ast
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt
import astunparse

def build_ast_tree(node, graph=None, parent=None):
    if graph is None:
        graph = nx.DiGraph()

    name = ast.dump(node, indent=None)
    graph.add_node(name)
    
    if parent is not None:
        graph.add_edge(parent, name)

    for child in ast.iter_child_nodes(node):
        build_ast_tree(child, graph, name)

    return graph



import ast
import networkx as nx
from networkx.drawing.nx_agraph import graphviz_layout
import matplotlib.pyplot as plt

def get_node_color(node):
    if isinstance(node, ast.Constant):
        return "cyan"
    elif isinstance(node, ast.Call):
        return "green"
    elif isinstance(node, (ast.BinOp, ast.Compare, ast.BoolOp)):
        return "red"
    else:
        return "blue"

def get_node_name(node):
    if isinstance(node, ast.Name):
        return f"Name: {node.id}"
    elif isinstance(node, ast.Constant):
        return f"Constant: {node.value}"
    elif isinstance(node, ast.Attribute):
        return f"Attribute: {node.attr}"
    elif isinstance(node, (ast.BinOp, ast.UnaryOp, ast.Compare, ast.BoolOp)):
        return f"Operator: {ast.unparse(node).strip()}"
    elif isinstance(node, ast.Call):
        return f"Call: {ast.unparse(node.func).strip()}"
    else:
        return node.__class__.__name__

def build_ast_tree(node, graph=None, parent=None):
    if graph is None:
        graph = nx.DiGraph()

    name = get_node_name(node)
    graph.add_node(name, color=get_node_color(node))

    if parent is not None:
        graph.add_edge(parent, name)

    for child in ast.iter_child_nodes(node):
        build_ast_tree(child, graph, name)

    return graph

source = '''
def fibonacci(n):
    if n <= 0:
        return []

    fib_numbers = [0, 1]
    for i in range(2, n):
        fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

    return fib_numbers[:n]
'''

tree = ast.parse(source)
ast_graph = build_ast_tree(tree)

plt.figure(figsize=(12, 12))
pos = graphviz_layout(ast_graph, prog='dot')
colors = [ast_graph.nodes[node]['color'] for node in ast_graph.nodes]
nx.draw(ast_graph, pos, with_labels=True, arrows=True, node_color=colors, font_size=10)
plt.tight_layout()
plt.show()

def gen_img():
    source = '''
  def fibonacci(n):
      if n <= 0:
          return []

      fib_numbers = [0, 1]
      for i in range(2, n):
          fib_numbers.append(fib_numbers[-1] + fib_numbers[-2])

      return fib_numbers[:n]
  '''

  tree = ast.parse(source)
  ast_graph = build_ast_tree(tree)

  pos = graphviz_layout(ast_graph, prog='dot')
  nx.draw(ast_graph, pos, with_labels=True, arrows=True)
  plt.savefig('foo.png')

