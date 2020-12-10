import pytest
from src.leilao.dominio import Usuario, Lance, Leilao

@pytest.fixture
def Lucas():
    return Usuario('Lucas', 300.0)


@pytest.fixture
def Celular():
    return Leilao('Celular')

def test_deve_subtrair_valor_da_carteira_do_usuario_quando_este_propor_um_lance(Lucas,Celular):   
    Lucas.propoe_lance(Celular,100)
    assert Lucas.carteira  == 200

def test_deve_permitir_propor_lance_quando_o_valor_eh_menor_que_o_valor_da_carteira(Lucas,Celular):
    Lucas.propoe_lance(Celular,100)
    assert Lucas.carteira  == 200

def test_deve_permitir_propor_lance_quando_o_valor_eh_igual_ao_valor_da_carteira(Lucas,Celular):
    Lucas.propoe_lance(Celular,300)
    assert Lucas.carteira  == 0

    
def test_nao_deve_permitir_propor_lance_com_valor_maior_que_o_da_carteira(Lucas,Celular):
    with pytest.raises(ValueError):
        Lucas.propoe_lance(Celular,350)