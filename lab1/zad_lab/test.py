from multiprocessing.sharedctypes import Value
from numpy import kron
from main import *
import unittest


class Test_TestOperations(unittest.TestCase):

    def test_add_normal(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        add_participant(courses_info, "krypto", "Bob")
        self.assertTrue("Bob" in courses_info["courses_list"]["krypto"])
    
    def test_add_full(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 1}
        add_participant(courses_info, "krypto", "Bob")
        self.assertTrue("Bob" not in courses_info["courses_list"]["krypto"])

    def test_add_nonexistent(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            add_participant(courses_info, "sieci", "Bob")

    def test_remove_normal(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        remove_participant(courses_info, "krypto", "Janusz")
        self.assertTrue("Janusz" not in courses_info["courses_list"]["krypto"])
    
    def test_remove_nonexistent(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            remove_participant(courses_info, "krypto", "Bob")

    def test_add_normal(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        add_course(courses_info, "sieci")
        self.assertIn("sieci", courses_info["courses_list"])
    
    def test_add_full(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 1, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            add_course(courses_info, "sieci")

    def test_add_existing(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            add_course(courses_info, "krypto")

    def test_remove_normal(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        remove_course(courses_info, "krypto")
        self.assertNotIn("krypto", courses_info["courses_list"])
    
    def test_remove_nonexistent(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            remove_course(courses_info, "sieci")

    def test_modify_normal(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        modify_course(courses_info, "krypto", "sieci")
        self.assertNotIn("krypto", courses_info["courses_list"])
        self.assertIn("sieci", courses_info["courses_list"])
        self.assertIn("Janusz", courses_info["courses_list"]["sieci"])

    def test_nonexistent(self):
        courses_info = {"courses_list": {
            "krypto": ["Janusz"]
        }, 
        "max_courses": 10, 
        "max_participants": 10}
        with self.assertRaises(ValueError):
            modify_course(courses_info, "sieci", "krypto")


if __name__ == "__main__":
    unittest.main()