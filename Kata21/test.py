import unittest
from single_link_list import SingleLinkedList

class TestSingleLinkedList(unittest.TestCase):

    list = SingleLinkedList()

    def test_emptylist(self):
        self.assertEqual(self.list.find("fred"), "")

    def test_elementadd(self):
        self.list.add("fred")
        self.assertEqual("fred", self.list.find("fred").value())

    def test_nonmember(self):
        self.assertEqual(self.list.find("wilma"), "")

    def test_twomembers(self):
        self.list.add("wilma")
        self.assertEqual("fred",  self.list.find("fred").value())
        self.assertEqual("wilma", self.list.find("wilma").value())
        self.assertEqual(["fred", "wilma"], self.list.values())

    def test_threemembers(self):
        self.list = SingleLinkedList()
        self.list.add("fred")
        self.list.add("wilma")
        self.list.add("betty")
        self.list.add("barney")
        self.assertEqual(["fred", "wilma", "betty", "barney"], self.list.values())

    def test_listremove3(self):
        self.list.delete(self.list.find("wilma"))
        self.assertEqual(["fred", "betty", "barney"], self.list.values())

    def test_listremove2(self): 
        self.list.delete(self.list.find("barney"))
        self.assertEqual(["fred", "betty"], self.list.values())

    def test_listremove1(self):
        self.list.delete(self.list.find("fred"))
        self.assertEqual(["betty"], self.list.values())

    def test_listremove0(self):    
        self.list.delete(self.list.find("betty"))
        self.assertEqual([], self.list.values())

if __name__ == '__main__':
    unittest.main()
