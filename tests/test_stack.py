import pytest
from main import check_balanced_brackets

class TestStack:

    @pytest.mark.parametrize(
            'sequence, expected',
            (
                (r'(([[{{}}]]))', True),
                (r'(([[]))', False)
            )
    )
    def test_sequences(self, sequence, expected):
        assert check_balanced_brackets(sequence) == expected

    def test_exception(self):
        result = None
        try:
            result = check_balanced_brackets('(([[]))1')
        except Exception as e:
            assert str(e) == 'The sequence has unexpected elements'
            return
        assert result not in (True, False)