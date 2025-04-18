import re
from collections import defaultdict
import os
import string
from typing import Dict, List, Optional, Tuple
import argparse

class WordFrequencyAnalyzer:
    """A comprehensive word frequency analysis tool."""
    
    def __init__(self):
        self.stop_words = {
            'a', 'an', 'the', 'and', 'or', 'but', 'of', 'to', 'in', 'on', 
            'at', 'for', 'by', 'with', 'as', 'is', 'are', 'was', 'were'
        }
        self.word_counts = defaultdict(int)
        self.total_words = 0
        self.unique_words = 0

    def read_file(self, filename: str) -> Optional[str]:
        """Read text from a file with comprehensive error handling."""
        try:
            if not os.path.exists(filename):
                raise FileNotFoundError(f"File '{filename}' not found")
                
            if not os.path.isfile(filename):
                raise ValueError(f"'{filename}' is not a file")
                
            if os.path.getsize(filename) > 10 * 1024 * 1024:  # 10MB limit
                raise ValueError("File too large (max 10MB allowed)")
                
            with open(filename, 'r', encoding='utf-8', errors='replace') as f:
                return f.read()
                
        except Exception as e:
            print(f"Error reading file: {e}")
            return None

    def preprocess_text(self, text: str) -> List[str]:
        """Clean and tokenize text with advanced processing."""
        if not text:
            return []
            
        # Convert to lowercase and remove punctuation
        text = text.lower()
        text = text.translate(str.maketrans('', '', string.punctuation))
        
        # Handle contractions and special cases
        text = re.sub(r"won't", "will not", text)
        text = re.sub(r"can't", "can not", text)
        text = re.sub(r"n't", " not", text)
        text = re.sub(r"'s", " is", text)
        text = re.sub(r"'re", " are", text)
        text = re.sub(r"'d", " would", text)
        text = re.sub(r"'ll", " will", text)
        text = re.sub(r"'t", " not", text)
        text = re.sub(r"'ve", " have", text)
        text = re.sub(r"'m", " am", text)
        
        # Tokenize and filter
        words = re.findall(r'\b[\w-]+\b', text)
        return [word for word in words if word not in self.stop_words and len(word) > 1]

    def count_words(self, words: List[str]) -> None:
        """Count words and update statistics."""
        self.word_counts.clear()
        self.total_words = len(words)
        
        for word in words:
            self.word_counts[word] += 1
            
        self.unique_words = len(self.word_counts)

    def get_most_common(self, n: int = 10) -> List[Tuple[str, int]]:
        """Get the n most common words and their counts."""
        return sorted(self.word_counts.items(), key=lambda x: x[1], reverse=True)[:n]

    def get_word_stats(self) -> Dict[str, float]:
        """Calculate various word statistics."""
        if self.total_words == 0:
            return {}
            
        avg_word_length = sum(len(word) * count for word, count in self.word_counts.items()) / self.total_words
        word_diversity = self.unique_words / self.total_words
        
        return {
            'total_words': self.total_words,
            'unique_words': self.unique_words,
            'avg_word_length': round(avg_word_length, 2),
            'word_diversity': round(word_diversity, 4),
            'most_common': self.get_most_common(5)
        }

    def generate_report(self, output_file: Optional[str] = None) -> None:
        """Generate and display or save a comprehensive report."""
        stats = self.get_word_stats()
        report_lines = [
            "Word Frequency Analysis Report",
            "=" * 40,
            f"Total words: {stats['total_words']}",
            f"Unique words: {stats['unique_words']}",
            f"Average word length: {stats['avg_word_length']}",
            f"Word diversity: {stats['word_diversity']}",
            "\nTop 5 most frequent words:",
            "-" * 30
        ]
        
        for word, count in stats['most_common']:
            report_lines.append(f"{word:<20} {count:>5} ({count/stats['total_words']:.2%})")
            
        report = '\n'.join(report_lines)
        
        if output_file:
            try:
                with open(output_file, 'w', encoding='utf-8') as f:
                    f.write(report)
                print(f"Report saved to {output_file}")
            except Exception as e:
                print(f"Error saving report: {e}")
        else:
            print(report)

def main():
    """Command-line interface for the word frequency analyzer."""
    parser = argparse.ArgumentParser(description='Word Frequency Analyzer')
    parser.add_argument('input_file', help='Text file to analyze')
    parser.add_argument('-o', '--output', help='Output file for the report')
    parser.add_argument('--no-stopwords', action='store_true', 
                       help='Disable stop word filtering')
    args = parser.parse_args()

    analyzer = WordFrequencyAnalyzer()
    
    if args.no_stopwords:
        analyzer.stop_words = set()
    
    text = analyzer.read_file(args.input_file)
    if text is None:
        return
        
    words = analyzer.preprocess_text(text)
    analyzer.count_words(words)
    analyzer.generate_report(args.output)

if __name__ == '__main__':
    main()