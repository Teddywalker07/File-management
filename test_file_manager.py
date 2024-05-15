import unittest
from unittest.mock import patch, mock_open
import os
import shutil
import hashlib
import tempfile

from file_manager import FileManager

class TestFileManager(unittest.TestCase):	
    def setUp(self):
        self.file_manager = FileManager()
        self.test_dir = os.path.join(os.path.dirname(__file__), 'test_files')
        os.makedirs(self.test_dir, exist_ok=True)
        self.test_file_path = os.path.join(self.test_dir, 'test.txt')
        with open(self.test_file_path, 'w') as f:
            f.write('test content')
        os.chmod(self.test_file_path, 0o400)  # Set file to read-only
        print(f"Starting test: {self._testMethodName}")

    def tearDown(self):
        os.chmod(self.test_file_path, 0o644)  # Restore file permissions
        shutil.rmtree(self.test_dir)
        print(f"Finished test: {self._testMethodName}")
    
        
    def test_change_to_valid_directory(self):
        ''' testing by passing valid directory'''
        self.file_manager.change_directory(self.test_dir)
        self.assertEqual(self.file_manager.current_directory, self.test_dir)

    def test_change_to_root_directory(self):
        ''' testing by passing the root of the curent directory'''
        self.file_manager.change_directory('/')
        self.assertEqual(self.file_manager.current_directory, '/')

  

if __name__ == '__main__':
    unittest.main()