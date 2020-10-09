import unittest
from LinkedListFile import *
from InventoryItemFile import *

class MyTestCase(unittest.TestCase):
#     def test_something(self):
#         self.assertual(True, False)
    def setUp(self):
        self.genericItem:InventoryItem  = InventoryItem()
        self.swordItem:InventoryItem    = InventoryItem(item_name="sword", item_type=InventoryType.MEELEE, item_power=5)
        self.wandItem:InventoryItem     = InventoryItem(item_name="wand", item_type=InventoryType.MAGIC, item_power=3)
        self.poulticeItem:InventoryItem = InventoryItem(item_name="poultice", item_type=InventoryType.HEALING, item_power=2)
        self.clubItem:InventoryItem     = InventoryItem(item_name="club", item_type=InventoryType.MEELEE, item_power=2)
        self.daggerItem:InventoryItem   = InventoryItem(item_name="dagger", item_type=InventoryType.MEELEE, item_power=3)
        self.potionItem:InventoryItem   = InventoryItem(item_name="potion", item_type=InventoryType.MAGIC, item_power=2)


    def test_a_is_empty(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        self.assertTrue(l_list.is_empty())
        l_list.add_to_end(self.genericItem)
        self.assertFalse(l_list.is_empty())

    #@unittest.skip("Skipping test b. Get test a working first.")
    def test_b_add_to_end(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        self.assertEqual(l_list.toList(), [])
        l_list.add_to_end(self.genericItem)
        l_list.add_to_end(self.swordItem)
        self.assertEqual(l_list.toList(), [self.genericItem, self.swordItem])


    #@unittest.skip("Skipping test c. Get test b working first.")
    def test_c_add_to_start(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_to_end(InventoryItem())
        l_list.add_to_end(InventoryItem(item_name="sword", item_type=InventoryType.MEELEE, item_power=5))
        l_list.add_to_start(InventoryItem(item_name="wand", item_type=InventoryType.MAGIC, item_power=3))
        self.assertEqual(l_list.toList(), [self.wandItem, self.genericItem, self.swordItem])


    #@unittest.skip("Skipping test d. Get test c working first.")
    def test_d_add_items(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_to_start(self.wandItem)
        l_list.add_all_to_end([self.clubItem, self.potionItem, self.swordItem])
        self.assertEqual(l_list.toList(), [self.wandItem, self.clubItem, self.potionItem, self.swordItem])


    #@unittest.skip("Skipping test e. Get test d working first.")
    def test_e_len(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        self.assertEqual(len(l_list), 0)
        l_list.add_all_to_end([self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem])
        self.assertEqual(len(l_list), 5)
        l_list.add_to_end([self.clubItem])
        self.assertEqual(len(l_list), 6)


    #@unittest.skip("Skipping test f. Get test e working first.")
    def test_f_contains(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.poulticeItem, self.clubItem, self.genericItem, self.wandItem])
        self.assertTrue(self.clubItem in l_list)
        self.assertTrue(self.wandItem in l_list)
        self.assertFalse(self.daggerItem in l_list)


    #@unittest.skip("Skipping test g. Get test f working first.")
    def test_g_index(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.poulticeItem, self.clubItem, self.genericItem, self.wandItem])
        self.assertEqual(l_list.index(self.wandItem), 0)
        self.assertEqual(l_list.index(self.clubItem), 2)


    #@unittest.skip("Skipping test h. Get test g working first.")
    def test_h_item_at_index(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        self.assertEqual(l_list.item_at_index(0), self.genericItem)
        self.assertEqual(l_list.item_at_index(2), self.poulticeItem)
        self.assertRaises(IndexError, l_list.item_at_index, 20)


    #@unittest.skip("Skipping test i. Get test h working first.")
    def test_i_item_at_start_and_end(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        self.assertEqual(l_list.item_at_start(), self.genericItem)
        self.assertEqual(l_list.item_at_end(), self.swordItem)


    #@unittest.skip("Skipping test j. Get test i working first.")
    def test_j_insert_item_at_start(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        l_list.insert_value_at_start(self.clubItem)
        self.assertEqual(l_list.item_at_start(), self.clubItem)
        self.assertEqual(l_list.item_at_index(1), self.genericItem)
        self.assertEqual(l_list.item_at_index(2), self.wandItem)
        self.assertEqual(len(l_list), 7)
        l_list = LinkedList()
        l_list.insert_value_at_start(self.clubItem)
        self.assertEqual(l_list.item_at_start(), self.clubItem)
        self.assertEqual(len(l_list), 1)


    #@unittest.skip("Skipping test k. Get test j working first.")
    def test_k_insert_value_at_index(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end(
            [self.genericItem, self.wandItem, self.poulticeItem, self.potionItem, self.daggerItem, self.swordItem])
        l_list.insert_value_at_index(self.clubItem, 3)
        self.assertEqual(len(l_list), 7)
        self.assertEqual(l_list.item_at_index(3), self.clubItem)
        self.assertEqual(l_list.item_at_index(4), self.potionItem)


    #@unittest.skip("Skipping test l. Get test k working first.")
    def test_l_insert_all(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.wandItem, self.clubItem, self.potionItem])
        l_list.insert_all_at_index([self.swordItem, self.poulticeItem, self.genericItem], 1)
        self.assertEqual(l_list.toList(), [self.wandItem, self.swordItem, self.poulticeItem, self.genericItem, \
                                         self.clubItem, self.potionItem])

        l_list.insert_all_at_index([self.wandItem, self.potionItem], 0)
        self.assertEqual(l_list.toList(), [self.wandItem, self.potionItem, self.wandItem, self.swordItem, \
                                          self.poulticeItem, self.genericItem, self.clubItem, self.potionItem])

        l_list.insert_all_at_index([self.wandItem], 8)
        self.assertEqual(l_list.toList(), [self.wandItem, self.potionItem, self.wandItem, self.swordItem, \
                                         self.poulticeItem, self.genericItem, self.clubItem, self.potionItem, \
                                         self.wandItem])

        self.assertRaises(IndexError, l_list.insert_all_at_index, [self.genericItem, self.genericItem], 12)

    #@unittest.skip("Skipping test m. Get test l working first.")
    def test_m_remove_first_and_last(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.genericItem, self.wandItem, self.potionItem, self.daggerItem])
        l_list.remove_first_item()
        self.assertEqual(len(l_list), 3)
        self.assertEqual(l_list.toList(), [self.wandItem, self.potionItem, self.daggerItem])
        l_list.remove_last_item()
        self.assertEqual(len(l_list), 2)
        self.assertEqual(l_list.toList(), [self.wandItem, self.potionItem])


    #@unittest.skip("Skipping test n. Get test m working first.")
    def test_n_remove_from_middle(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.potionItem, self.swordItem, self.clubItem, self.potionItem, self.poulticeItem])
        l_list.remove_item_at_index(2)
        self.assertEqual(len(l_list), 4)
        self.assertEqual(l_list.toList(), [self.potionItem, self.swordItem, self.potionItem, self.poulticeItem])

        l_list.remove_item_at_index(0)
        self.assertEqual(len(l_list), 3)
        self.assertEqual(l_list.toList(), [self.swordItem, self.potionItem, self.poulticeItem])

        l_list.remove_item_at_index(2)
        self.assertEqual(len(l_list), 2)
        self.assertEqual(l_list.toList(), [self.swordItem, self.potionItem])


    #@unittest.skip("Skipping test o. Get test n working first.")
    def test_o_contains(self):
        # Note the syntax "a in b" automatically calls "b.__contains__(a)"
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.clubItem, self.swordItem, self.genericItem])
        self.assertTrue(self.swordItem in l_list)
        self.assertTrue(self.clubItem in l_list)
        self.assertTrue(self.genericItem in l_list)
        self.assertFalse(self.poulticeItem in l_list)


    #@unittest.skip("Skipping test p. Get test o working first.")
    def test_p_remove_item(self):
        l_list:LinkedList[InventoryItem] = LinkedList[InventoryItem]()

        l_list.add_all_to_end([self.swordItem, self.clubItem, self.wandItem, self.clubItem, self.poulticeItem, \
                             self.swordItem, self.daggerItem, self.wandItem, self.clubItem])
        l_list.remove(self.clubItem)
        self.assertEqual(len(l_list), 6)
        self.assertEqual(l_list.toList(),
                         [self.swordItem, self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem, self.wandItem])

        l_list.remove(self.swordItem, first_only=True)
        self.assertEqual(len(l_list), 5)
        self.assertEqual(l_list.toList(), [self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem, self.wandItem])

        l_list.remove(self.genericItem)
        self.assertEqual(len(l_list), 5)
        self.assertEqual(l_list.toList(), [self.wandItem, self.poulticeItem, self.swordItem, self.daggerItem, self.wandItem])



    #@unittest.skip("Skipping test q. Get test p working first.")
    def test_q_other_list_types(self):
        l_list:LinkedList[int] = LinkedList[int]()

        l_list.add_to_end(12)
        l_list.add_to_end(18)
        l_list.add_to_start(6)
        self.assertEqual(l_list.toList(), [6,12,18])

        l_list2:LinkedList[str] = LinkedList[str]()

        l_list2.add_to_start("first")
        items = ("second","third","fourth")
        l_list2.add_all_to_end(items)
        l_list2.add_to_end("fifth")
        self.assertEqual(l_list2.toList(), ["first","second","third","fourth","fifth"])

if __name__ == '__main__':
    unittest.main()
