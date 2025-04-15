import pytest
from main import check_balanced_brackets

class TestStack:
    def setup_method(self):
        pass

    def tearup_method(self):
        pass

    @pytest.mark.parametrize(
            'sequence, expected',
            (
                (r'(([[{{}}]]))', 'Сбалансированно'),
                (r'(([[]))', 'Несбалансированно')
            )
    )
    def test_sequences(self, sequence, expected):
        assert check_balanced_brackets(sequence) == expected

    def test_exception(self):
        try:
            check_balanced_brackets('(([[]))1')
        except Exception as e:
            assert str(e) == 'The sequence has unexpected elements'