import unittest
from unittest.mock import patch
from lab1 import text_to_morse, morse_to_text, MORSE_CODE_DICT, main


class TestMorseCodeDict(unittest.TestCase):
    """Test the Morse code dictionary"""
    
    def test_dict_not_empty(self):
        """Test that the Morse code dictionary is not empty"""
        self.assertGreater(len(MORSE_CODE_DICT), 0)
    
    def test_dict_contains_letters(self):
        """Test that dictionary contains all letters A-Z"""
        for letter in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            self.assertIn(letter, MORSE_CODE_DICT)
    
    def test_dict_contains_numbers(self):
        """Test that dictionary contains all numbers 0-9"""
        for number in '0123456789':
            self.assertIn(number, MORSE_CODE_DICT)
    
    def test_dict_values_valid_morse(self):
        """Test that all dictionary values contain only dots and dashes"""
        valid_chars = set('.-')
        for morse_code in MORSE_CODE_DICT.values():
            self.assertTrue(set(morse_code).issubset(valid_chars))


class TestTextToMorse(unittest.TestCase):
    """Test text to Morse code conversion"""
    
    def test_single_letter(self):
        """Test conversion of single letters"""
        self.assertEqual(text_to_morse('A'), '.-')
        self.assertEqual(text_to_morse('B'), '-...')
        self.assertEqual(text_to_morse('Z'), '--..')
    
    def test_single_number(self):
        """Test conversion of single numbers"""
        self.assertEqual(text_to_morse('1'), '.----')
        self.assertEqual(text_to_morse('5'), '.....')
        self.assertEqual(text_to_morse('0'), '-----')
    
    def test_simple_word(self):
        """Test conversion of simple words"""
        self.assertEqual(text_to_morse('SOS'), '... --- ...')
        self.assertEqual(text_to_morse('HELLO'), '.... . .-.. .-.. ---')
    
    def test_multiple_words(self):
        """Test conversion of multiple words"""
        result = text_to_morse('HELLO WORLD')
        expected = '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
        self.assertEqual(result, expected)
    
    def test_case_insensitive(self):
        """Test that function handles both upper and lower case"""
        self.assertEqual(text_to_morse('hello'), text_to_morse('HELLO'))
        self.assertEqual(text_to_morse('Hello'), text_to_morse('HELLO'))
    
    def test_punctuation(self):
        """Test conversion of punctuation marks"""
        self.assertEqual(text_to_morse('!'), '-.-.--')
        self.assertEqual(text_to_morse('?'), '..--..')
        self.assertEqual(text_to_morse('.'), '.-.-.-')
    
    def test_mixed_content(self):
        """Test conversion of mixed letters, numbers, and punctuation"""
        result = text_to_morse('ABC123!')
        expected = '.- -... -.-. .---- ..--- ...-- -.-.--'
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        """Test conversion of empty string"""
        self.assertEqual(text_to_morse(''), '')
    
    def test_unsupported_characters(self):
        """Test that unsupported characters are skipped"""
        # Characters like é, ñ, etc. should be skipped
        self.assertEqual(text_to_morse('AéB'), '.- -...')
        self.assertEqual(text_to_morse('A#B'), '.- -...')


class TestMorseToText(unittest.TestCase):
    """Test Morse code to text conversion"""
    
    def test_single_letter(self):
        """Test conversion of single Morse code letters"""
        self.assertEqual(morse_to_text('.-'), 'A')
        self.assertEqual(morse_to_text('-...'), 'B')
        self.assertEqual(morse_to_text('--..'), 'Z')
    
    def test_single_number(self):
        """Test conversion of single Morse code numbers"""
        self.assertEqual(morse_to_text('.----'), '1')
        self.assertEqual(morse_to_text('.....'), '5')
        self.assertEqual(morse_to_text('-----'), '0')
    
    def test_simple_word(self):
        """Test conversion of simple Morse code words"""
        self.assertEqual(morse_to_text('... --- ...'), 'SOS')
        self.assertEqual(morse_to_text('.... . .-.. .-.. ---'), 'HELLO')
    
    def test_multiple_words(self):
        """Test conversion of multiple Morse code words"""
        morse = '.... . .-.. .-.. --- / .-- --- .-. .-.. -..'
        self.assertEqual(morse_to_text(morse), 'HELLO WORLD')
    
    def test_punctuation(self):
        """Test conversion of Morse code punctuation"""
        self.assertEqual(morse_to_text('-.-.--'), '!')
        self.assertEqual(morse_to_text('..--..'), '?')
        self.assertEqual(morse_to_text('.-.-.-'), '.')
    
    def test_empty_string(self):
        """Test conversion of empty Morse code"""
        self.assertEqual(morse_to_text(''), '')
    
    def test_invalid_morse_code(self):
        """Test handling of invalid Morse code"""
        # Invalid codes should be skipped
        result = morse_to_text('.- invalid -...')
        self.assertEqual(result, 'AB')
    
    def test_extra_spaces(self):
        """Test handling of extra spaces in Morse code"""
        result = morse_to_text('.-  -...')  # Extra space
        self.assertEqual(result, 'AB')


class TestRoundTripConversion(unittest.TestCase):
    """Test that text->morse->text conversions work correctly"""
    
    def test_simple_text_roundtrip(self):
        """Test round trip conversion for simple text"""
        original = 'HELLO'
        morse = text_to_morse(original)
        converted_back = morse_to_text(morse)
        self.assertEqual(original, converted_back)
    
    def test_complex_text_roundtrip(self):
        """Test round trip conversion for complex text"""
        original = 'HELLO WORLD 123!'
        morse = text_to_morse(original)
        converted_back = morse_to_text(morse)
        self.assertEqual(original, converted_back)
    
    def test_numbers_roundtrip(self):
        """Test round trip conversion for numbers"""
        original = '1234567890'
        morse = text_to_morse(original)
        converted_back = morse_to_text(morse)
        self.assertEqual(original, converted_back)
    
    def test_punctuation_roundtrip(self):
        """Test round trip conversion for punctuation"""
        original = 'HELLO, WORLD!'
        morse = text_to_morse(original)
        converted_back = morse_to_text(morse)
        self.assertEqual(original, converted_back)


class TestEdgeCases(unittest.TestCase):
    """Test edge cases and potential error conditions"""
    
    def test_very_long_text(self):
        """Test conversion of very long text"""
        long_text = 'A' * 1000
        morse = text_to_morse(long_text)
        converted_back = morse_to_text(morse)
        self.assertEqual(long_text, converted_back)
    
    def test_special_characters_mixed(self):
        """Test text with mix of supported and unsupported characters"""
        text_with_special = 'HELLO@#$WORLD'
        morse = text_to_morse(text_with_special)
        # Should only convert supported characters
        self.assertIn('....', morse)  # H
        self.assertIn('.--.-', morse)  # @
    
    def test_multiple_consecutive_spaces(self):
        """Test text with multiple consecutive spaces"""
        result = text_to_morse('A   B')
        self.assertEqual(result, '.- / / / -...')
    
    def test_morse_with_mixed_separators(self):
        """Test Morse code with different separator styles"""
        # Test with different word separators
        morse1 = '.- / -...'
        morse2 = '.-/-...'
        # Both should work, though format might differ
        result1 = morse_to_text(morse1)
        self.assertIn('A', result1)
        self.assertIn('B', result1)


if __name__ == '__main__':
    # Create a test suite
    suite = unittest.TestSuite()
    
    # Add all test classes
    test_classes = [
        TestMorseCodeDict,
        TestTextToMorse,
        TestMorseToText,
        TestRoundTripConversion,
        TestEdgeCases
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        suite.addTests(tests)
    
    # Run the tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print(f"\n{'='*50}")
    print(f"Tests run: {result.testsRun}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print(f"Success rate: {((result.testsRun - len(result.failures) - len(result.errors))/result.testsRun)*100:.1f}%")
    print(f"{'='*50}")