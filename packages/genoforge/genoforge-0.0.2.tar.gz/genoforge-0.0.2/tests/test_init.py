from genoforge import hello_geno


def test_hello_geno(capsys):
    hello_geno()
    captured = capsys.readouterr()
    assert captured.out == "Hi, lets build together!!\n"
    assert captured.err == ''