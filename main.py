class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursively(self.root, value)

    def _insert_recursively(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursively(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursively(node.right, value)

    def search(self, value):
        return self._search_recursively(self.root, value)

    def _search_recursively(self, node, value):
        if node is None:
            return False
        if node.value == value:
            return True
        elif value < node.value:
            return self._search_recursively(node.left, value)
        else:
            return self._search_recursively(node.right, value)

    def display(self):
        lines = []
        self._display_recursively(self.root, 0, lines)
        for line in lines:
            print(line)

    def _display_recursively(self, node, level, lines):
        if node is not None:
            if level >= len(lines):
                lines.append("")
            lines[level] += f"{' ' * (2 ** (4 - level) - 1)}{node.value}{' ' * (2 ** (4 - level) - 1)}"
            self._display_recursively(node.left, level + 1, lines)
            self._display_recursively(node.right, level + 1, lines)



if __name__ == "__main__":
    bst = BinarySearchTree()

    values = [15, 10, 20, 8, 12, 17, 25]
    for val in values:
        bst.insert(val)

    print("Дерево:")
    bst.display()

    search_value = int(input("Введите значение для поиска: "))
    if bst.search(search_value):
        print(f"Значение {search_value} найдено в дереве.")
    else:
        print(f"Значение {search_value} не найдено в дереве.")
