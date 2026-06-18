from eh_par import verifica_par_impar

def test_eh_par_4():
    assert verifica_par_impar(4) is True

def test_eh_par_5():
    assert verifica_par_impar(5) is False
    
