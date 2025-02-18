import pytest
import src.chalk.parser as par

def test_multiple_chalk():
    x = par.Parser("samples\\exception_tests\\to_many_chalk_block.chalk")
    pytest.raises(Exception)


if __name__ == "__main__":
    test_multiple_chalk()