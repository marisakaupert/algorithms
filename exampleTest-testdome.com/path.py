import unittest
import re


class Path:
    def __init__(self, path):
        self.current_path = path
        self.pattern = re.compile("^([A-Za-z/])+$")

    def cd(self, new_path):
        splitPath = new_path.split('/')
        curPath = self.current_path.split('/')

        if new_path == '/':
            self.current_path = '/'
            return

        while len(splitPath) > 0:
            if splitPath[0] == '..':
                if curPath == '':
                    splitPath.pop(0)
                else:
                    curPath.pop()
                    splitPath.pop(0)
            else:
                curPath.append(splitPath[0])
                splitPath.pop(0)

        print(f"{curPath}")
        self.current_path = '/'.join(curPath)


class TestPath(unittest.TestCase):
    def test_is_valid_file_name(self):
        path = Path('/a/b/c/d')
        pattern = re.compile("^([A-Za-z/])+$")
        self.assertRegex(path.current_path, pattern)

    def test_can_move_forward(self):
        path = Path('/a/b/c/d')
        childDirectory = path.cd('x')
        self.assertEqual(path.current_path, '/a/b/c/d/x')

    def test_can_move_backward(self):
        path = Path('/a/b/c/d')
        parentDirectory = path.cd('../')
        self.assertEqual(path.current_path, '/a/b/c')

    def test_cannot_go_past_root(self):
        path = Path('/')
        parentDirectory = path.cd('../')
        self.assertEqual(path.current_path, '/')

    def test_can_go_to_root(self):
        path = Path('/a/b/c/d')
        parentDirectory = path.cd('/')
        self.assertEqual(path.current_path, '/')

    # def test_can_complete_multiple_moves(self):
    #     path = Path('/a/b/c/d')
    #     parentDirectory = path.cd('../x')
    #     self.assertEqual(path.current_path, '/a/b/c/x')

if __name__ == '__main__':
    unittest.main()

