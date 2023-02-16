import ast
import os
import sys


def get_all_modules(file_name: str) -> set[str]:
    """
    Find all modules that have had imported in file
    IT WORK ONLY ON THE SAME LEVEL AS THIS MODULE

    :param file_name: str
    :return: set[str]
    """
    modules = set()

    def visit_import(node):
        for name in node.names:
            modules.add(name.name.split(".")[0])

    def visit_import_from(node):
        if node.module is not None and node.level == 0:
            modules.add(node.module.split(".")[0])

    node_iter = ast.NodeVisitor()
    node_iter.visit_Import = visit_import
    node_iter.visit_ImportFrom = visit_import_from
    path = os.path.join(sys.path[0], file_name)
    with open(path, 'r', encoding='UTF-8') as f:
        node_iter.visit(ast.parse(f.read()))
    return modules


if __name__ == '__main__':
    get_all_modules('find_all_modules.py')
