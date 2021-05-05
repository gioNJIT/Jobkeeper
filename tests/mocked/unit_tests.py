import unittest
import unittest.mock as mock
from unittest.mock import patch
import os
import sys
from app import db


        
sys.path.append(os.path.abspath('../'))
from app import add_user
import models

KEY_INPUT = "input"
KEY_EXPECTED = "expected"

INITIAL_USERNAME = 'user1'

class AddUserTestCase(unittest.TestCase):
    def setUp(self):
        self.success_test_params = [
            {
                KEY_INPUT: 'naman',
                KEY_EXPECTED: [INITIAL_USERNAME, 'naman'],
            },
            
            {
                KEY_INPUT: 'naman',
                KEY_EXPECTED: [INITIAL_USERNAME, 'naman',''],
            },
             {
                KEY_INPUT: 'naman',
                KEY_EXPECTED: [INITIAL_USERNAME, 'naman','',''],
            },
         
        ]
        
        self.failure_test_params = [
            {
               KEY_INPUT: 'naman',
               KEY_EXPECTED: [INITIAL_USERNAME, 'namann', ''],
            },
            
            {
               KEY_INPUT: 'Hossein',
               KEY_EXPECTED: [INITIAL_USERNAME, 'naann',],
            },
            
            {
               KEY_INPUT: 'Hossein',
               KEY_EXPECTED: [INITIAL_USERNAME, '', ''],
            },
          
        ]
        
        
        self.in_test_params = [
            {
               KEY_INPUT: 'naman',
               KEY_EXPECTED: [INITIAL_USERNAME, 'naman', ''],
            },
            
            {
               KEY_INPUT: 'Hossein',
               KEY_EXPECTED: [INITIAL_USERNAME, 'naman',],
            },
            
            {
               KEY_INPUT: 'Hossein',
               KEY_EXPECTED: [INITIAL_USERNAME, 'naman', ''],
            },
          
        ]
        
        initial_person = models.User(username=INITIAL_USERNAME, email='{0}@stuff.com'.format(INITIAL_USERNAME))
        self.initial_db_mock = [initial_person]
    
    def mocked_db_session_add(self, username):
        self.initial_db_mock.append(username)
    
    def mocked_db_session_commit(self):
        pass
    
    def mocked_person_query_all(self):
        return self.initial_db_mock
    
    def test_success(self):
        for test in self.success_test_params:
            with patch('app.db.session.add', self.mocked_db_session_add):
                with patch('app.db.session.commit', self.mocked_db_session_commit):
                    with patch('models.User.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                        actual_result = add_user(test[KEY_INPUT])
                        expected_result = test[KEY_EXPECTED]
                        
                        self.assertEqual(len(actual_result), len(expected_result))
                        self.assertEqual(actual_result[1], expected_result[1])
      
                        
    def test_failure(self):
         for test in self.failure_test_params:
            with patch('app.db.session.add', self.mocked_db_session_add):
                with patch('app.db.session.commit', self.mocked_db_session_commit):
                    with patch('models.User.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                        actual_result = add_user(test[KEY_INPUT])
                        expected_result = test[KEY_EXPECTED]
    
                        
                        self.assertNotEqual(len(actual_result), len(expected_result))
                        self.assertNotEqual(actual_result[1], expected_result[1])
                        
    
    def test_in(self):
         for test in self.in_test_params:
            with patch('app.db.session.add', self.mocked_db_session_add):
                with patch('app.db.session.commit', self.mocked_db_session_commit):
                    with patch('models.User.query') as mocked_query:
                        mocked_query.all = self.mocked_person_query_all
                        actual_result = add_user(test[KEY_INPUT])
                        expected_result = test[KEY_EXPECTED]
    
                        
                        self.assertIn(actual_result[1], expected_result[1])
                        self.assertNotIn(actual_result[1], expected_result[0])

if __name__ == '__main__':
    unittest.main()