import unittest

from todo import add_task, delete_task, format_list, toggle_task


class TodoTest(unittest.TestCase):
    def test_add_list_toggle_delete(self):
        tasks = []
        add_task(tasks, "  buy milk  ")
        add_task(tasks, "")
        self.assertEqual(format_list(tasks), "1. [ ] buy milk")

        toggle_task(tasks, 1)
        self.assertEqual(format_list(tasks), "1. [x] buy milk")

        add_task(tasks, "walk dog")
        delete_task(tasks, 1)
        self.assertEqual(format_list(tasks), "1. [ ] walk dog")
        self.assertIsNone(toggle_task(tasks, 9))


if __name__ == "__main__":
    unittest.main()
