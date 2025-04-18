import unittest
import os
import tempfile
import pytest
from word_frequency import WordFrequencyAnalyzer

class TestWordFrequencyAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """Create temporary test files for all tests"""
        cls.test_dir = tempfile.mkdtemp()
        
        # Create test files
        cls.sample_file = os.path.join(cls.test_dir, "sample.txt")
        with open(cls.sample_file, 'w', encoding='utf-8') as f:
            f.write("Hello world! Hello Python. World of Python. Let's test contractions like can't and won't.")
            
        cls.empty_file = os.path.join(cls.test_dir, "empty.txt")
        open(cls.empty_file, 'w').close()
            
        cls.special_chars_file = os.path.join(cls.test_dir, "special.txt")
        with open(cls.special_chars_file, 'w', encoding='utf-8') as f:
            f.write("This @#$%^&*()_+{}[];:'\"\\|,.<>/?`~ test")

    @classmethod
    def tearDownClass(cls):
        """Clean up the temporary directory"""
        import shutil
        shutil.rmtree(cls.test_dir)

    def setUp(self):
        """Create a fresh analyzer for each test"""
        self.analyzer = WordFrequencyAnalyzer()

    def test_read_file_valid(self):
        """Test reading a valid file"""
        content = self.analyzer.read_file(self.sample_file)
        self.assertIsNotNone(content)
        self.assertIn("Hello world!", content)
        
    def test_read_file_empty(self):
        """Test reading an empty file"""
        content = self.analyzer.read_file(self.empty_file)
        self.assertEqual(content, "")
        
    def test_read_file_nonexistent(self):
        """Test reading a non-existent file"""
        content = self.analyzer.read_file("nonexistent.txt")
        self.assertIsNone(content)

    def test_preprocess_text_normal(self):
        """Test normal text preprocessing"""
        text = "Hello, World! This is a test."
        result = self.analyzer.preprocess_text(text)
        expected = ['hello', 'world', 'this', 'test']
        self.assertEqual(result, expected)
        
    def test_preprocess_text_contractions(self):
        """Test contraction handling"""
        text = "I can't believe it won't work"
        result = self.analyzer.preprocess_text(text)
        expected = ['cannot', 'believe', 'will', 'not', 'work']
        self.assertEqual(result, expected)
        
    def test_preprocess_text_special_chars(self):
        """Test text with special characters"""
        text = "Email@test.com #hashtag $100"
        result = self.analyzer.preprocess_text(text)
        expected = ['email', 'test', 'com', 'hashtag', '100']
        self.assertEqual(result, expected)
        
    def test_preprocess_text_empty(self):
        """Test empty text preprocessing"""
        self.assertEqual(self.analyzer.preprocess_text(""), [])
        self.assertEqual(self.analyzer.preprocess_text(None), [])

    def test_count_words_normal(self):
        """Test normal word counting"""
        words = ['test', 'test', 'hello', 'world', 'test']
        self.analyzer.count_words(words)
        
        self.assertEqual(self.analyzer.word_counts['test'], 3)
        self.assertEqual(self.analyzer.word_counts['hello'], 1)
        self.assertEqual(self.analyzer.word_counts['world'], 1)
        self.assertEqual(self.analyzer.total_words, 5)
        self.assertEqual(self.analyzer.unique_words, 3)
        
    def test_count_words_empty(self):
        """Test counting empty word list"""
        self.analyzer.count_words([])
        self.assertEqual(self.analyzer.total_words, 0)
        self.assertEqual(self.analyzer.unique_words, 0)
        self.assertEqual(len(self.analyzer.word_counts), 0)

    def test_get_most_common(self):
        """Test getting most common words"""
        words = ['a', 'b', 'c', 'a', 'b', 'a']
        self.analyzer.count_words(words)
        
        most_common = self.analyzer.get_most_common(2)
        self.assertEqual(most_common, [('a', 3), ('b', 2)])
        
    def test_get_word_stats(self):
        """Test word statistics calculation"""
        words = ['aaa', 'bb', 'bb', 'c', 'c', 'c']
        self.analyzer.count_words(words)
        
        stats = self.analyzer.get_word_stats()
        
        self.assertEqual(stats['total_words'], 6)
        self.assertEqual(stats['unique_words'], 3)
        self.assertAlmostEqual(stats['avg_word_length'], (3+2+2+1+1+1)/6)
        self.assertAlmostEqual(stats['word_diversity'], 3/6)
        self.assertEqual(len(stats['most_common']), 3)

    def test_generate_report_console(self):
        """Test console report generation (captures print output)"""
        from io import StringIO
        import sys
        
        # Prepare test data
        words = ['test', 'test', 'hello']
        self.analyzer.count_words(words)
        
        # Redirect stdout
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        # Generate report
        self.analyzer.generate_report()
        
        # Get output
        output = sys.stdout.getvalue()
        sys.stdout = old_stdout
        
        # Verify output
        self.assertIn("Word Frequency Analysis Report", output)
        self.assertIn("Total words: 3", output)
        self.assertIn("test", output)
        self.assertIn("66.67%", output)

    def test_generate_report_file(self):
        """Test file report generation"""
        report_file = os.path.join(self.test_dir, "report.txt")
        
        # Prepare test data
        words = ['test', 'test', 'hello']
        self.analyzer.count_words(words)
        
        # Generate report
        self.analyzer.generate_report(report_file)
        
        # Verify file was created
        self.assertTrue(os.path.exists(report_file))
        
        # Check content
        with open(report_file, 'r', encoding='utf-8') as f:
            content = f.read()
            self.assertIn("Word Frequency Analysis Report", content)
            self.assertIn("Total words: 3", content)

    def test_full_workflow(self):
        """Test complete workflow from file reading to report"""
        # Process sample file
        content = self.analyzer.read_file(self.sample_file)
        self.assertIsNotNone(content)
        
        words = self.analyzer.preprocess_text(content)
        self.assertGreater(len(words), 0)
        
        self.analyzer.count_words(words)
        self.assertGreater(self.analyzer.total_words, 0)
        
        # Check specific expected words
        self.assertIn('hello', self.analyzer.word_counts)
        self.assertIn('python', self.analyzer.word_counts)
        #self.assertIn('cannot', self.analyzer.word_counts)  # from "can't"
        #self.assertIn('will', self.analyzer.word_counts)    # from "won't"

if __name__ == '__main__':
    unittest.main(failfast=True, verbosity=2)