from processamento import processar_dados

def test_processar_dados():
    assert processar_dados([1, 2, 3]) == [2, 4, 6]
    