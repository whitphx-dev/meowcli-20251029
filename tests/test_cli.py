from meow.cli import meow


def test_meow_once(capsys):
    meow()
    out, _ = capsys.readouterr()
    assert "Meow!" in out


def test_meow_multiple(capsys):
    meow(times=3)
    out, _ = capsys.readouterr()
    assert out.count("Meow!") == 3


def test_meow_no_emoji(capsys):
    meow(times=1, emoji=False)
    out, _ = capsys.readouterr()
    assert "🐱" not in out
