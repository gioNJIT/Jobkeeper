'''
    update_users_test.py
    
    Fill in what this test is for here
'''

import unittest
from app import add

USERNAME_INPUT = "username"
USERS_INPUT = 'users'
EXPECTED_OUTPUT = "expected"

class UpdateUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                USERNAME_INPUT: "Naman",
                USERS_INPUT: {
                    'player': None,
                    
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "Naman",
                    
                    'waitList': [],
                }
            },
            
            {
                USERNAME_INPUT:  "Hossein",
                USERS_INPUT: {
                    'player': None,
                   
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "Hossein",
                   
                    'waitList': [],
                }
            },
            
            {
                USERNAME_INPUT:  "",
                USERS_INPUT: {
                    'player': None,
                    
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "",
                    
                    'waitList': [],
                }
            },
            
        ]
        
        self.failure_test_params = [
            {
                USERNAME_INPUT: "Naman",
                USERS_INPUT: {
                    'player': None,
                   
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': None,
                
                    'waitList': [],
                }
            },
            
            {
                USERNAME_INPUT: "Naman",
                USERS_INPUT: {
                    'player': None,
                    
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': None,
                    
                    'waitList': ["Naman"],
                }
            },
            
            {
                USERNAME_INPUT: "Naman",
                USERS_INPUT: {
                    'player': None,
                   
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "nama",
                  
                    'waitList': [],
                }
            },
        ]
        
        
        self.in_test_params = [
            {
                USERNAME_INPUT: "Naman",
                USERS_INPUT: {
                    'player': None,
                    
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "Naman",
                    
                    'waitList': ["Nama"],
                }
            },
            
            {
                USERNAME_INPUT: "Hossein",
                USERS_INPUT: {
                    'player': None,
                    
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "Hossein",
                   
                    'waitList': ["Hosein"],
                }
            },
            
            {
                USERNAME_INPUT: "",
                USERS_INPUT: {
                    'player': None,
                   
                    'waitList': [],
                },
                EXPECTED_OUTPUT: {
                    'player': "",
                    
                    'waitList': ["Naman"],
                }
            },
            
        ]
    def test_add_user(self):
        for test in self.success_test_params:
            adding_user = add(test[USERNAME_INPUT],test[USERS_INPUT])
            actual_result = adding_user
            expected_result = test[EXPECTED_OUTPUT]

            self.assertEqual(len(actual_result), len(expected_result))
            self.assertEqual(actual_result, expected_result)
            self.assertEqual(actual_result['player'], expected_result['player'] )
            
    def test_user(self):
        for test in self.failure_test_params:
            adding_user = add(test[USERNAME_INPUT],test[USERS_INPUT])
            actual_result = adding_user
            expected_result = test[EXPECTED_OUTPUT]

            #self.assertNotEqual(len(actual_result), len(expected_result))
            self.assertNotEqual(actual_result, expected_result)
            self.assertNotEqual(actual_result['player'], expected_result['player'] )
    
    def test_user_in(self):
        for test in self.in_test_params:
            adding_user = add(test[USERNAME_INPUT],test[USERS_INPUT])
            actual_result = adding_user
            expected_result = test[EXPECTED_OUTPUT]

            #self.assertNotEqual(len(actual_result), len(expected_result))
            #self.assertIn(actual_result, expected_result)
            self.assertIn(actual_result['player'], expected_result['player'] )
            self.assertNotIn(actual_result['player'], expected_result['waitList'] )

if __name__ == "__main__":
    unittest.main()