from dominio import Usuario, Lance, Leilao

gui = Usuario('Gui')
yuri = Usuario('Yuri')

lance_do_yuri = Lance(yuri, 100.0)
lance_do_gui = Lance(gui, 150.0)

leilao = Leilao('Celular')

leilao.propoe(lance_do_yuri)
leilao.propoe(lance_do_gui)

for lance in leilao.lances:
    print(lance)

