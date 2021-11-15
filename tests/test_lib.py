from bbquote.lib import get_quote

def test_get_quote():
  # check that the len is not 0
  assert len(get_quote()) != 0