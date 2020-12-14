import sys


class Usuario:

    def __init__(self, nome, carteira):
        self.__nome = nome
        self.__carteira = carteira

    def propoe_lance(self, leilao, valor: float):
        """
        teste 123
        """
        if self.__carteira >= valor:
            self.__carteira -= valor
            lance = Lance(self, valor)
            leilao.propoe(lance)
        else:
            raise ValueError('Saldo Invaldo')

    @property
    def nome(self):
        return self.__nome

    @property
    def carteira(self):
        return self.__carteira


class Lance:

    def __init__(self, usuario, valor):
        self.usuario = usuario
        self.valor = valor


class Leilao:

    def __init__(self, descricao):
        self.descricao = descricao
        self.maior_lance = sys.float_info.min
        self.menor_lance = sys.float_info.max
        self.__lances = []

    def propoe(self, lance: Lance):
        if self._proposta_isvalida(lance):
            if not self.__lances:
                self.menor_lance = lance.valor
            self.maior_lance = lance.valor

            self.__lances.append(lance)
        else:
            raise ValueError('Mesmo usario nao pode dar dois lances')

    @property
    def lances(self):
        return self.__lances[:]

    def _leila_isvazio(self):
        return not self.__lances

    def _usuario_diferente(self, lance):
        return self.__lances[-1].usuario != lance.usuario

    def _lance_maior_que_o_ultimo(self, lance):
        return lance.valor > self.__lances[-1].valor

    def _proposta_isvalida(self, lance):
        return self._leila_isvazio() or self._usuario_diferente(lance) and self._lance_maior_que_o_ultimo(lance)
