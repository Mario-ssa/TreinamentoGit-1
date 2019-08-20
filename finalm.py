from random import randint
class monstros:
  fataq = 0
  fdef = 0
  ataque =[]
  defesa =[]

  def __str__(self):
      return self.nome

  def __init__(self, nome, tipo, pataque, pdefesa, vida, evo, nivel):
      self.nome = nome
      self.tipo = tipo
      self.pataque = pataque
      self.pdefesa = pdefesa
      self.vida = vida
      self.evo = evo
      self.nivel = nivel

  def fataq(self):
      self.ataque.clear()
      for _ in range(10):
          self.ataque.append(self.pataque * self.evo * self.nivel * randint(1, 5))

  def fdef(self):
      self.defesa.clear()
      for _ in range(10):
          self.defesa.append(self.pdefesa * self.evo * self.nivel * randint(1, 3))


m1 = monstros("m1", "eletrico", 1, 2, 200, 1, 5)
m2 = monstros("m2", "fogo", 1, 2, 200, 1, 5)
m3 = monstros("m3", "agua", 1, 2, 200, 1, 5)
m4 = monstros("m4", "terra", 1, 2, 200, 1, 5)
m5 = monstros("m5", "fisico", 1, 2, 200, 1, 5)
m6 = monstros("m6", "psiquico", 1, 2, 200, 1, 5)
m7 = monstros("m7", "venenoso", 1, 2, 200, 1, 5)
m8 = monstros("m8", "gelo", 1, 2, 200, 1, 5)
lutadores = [m1,m2,m3,m4,m5,m6,m7,m8]


def luta(lutador1,lutador2):
    lutador1.fataq()
    lutador2.fataq()
    lutador1.fdef()
    lutador2.fdef()
    ds1 = []
    ds2 = []


    for numero in range(10):
        ds1.append(lutador1.ataque[numero] - lutador2.defesa[numero])
        ds2.append(lutador2.ataque[numero] - lutador1.defesa[numero])


    for numero in range(10):
        if ds1[numero] > 0:
            lutador1.vida = lutador1.vida - ds1[numero]
        if ds2[numero] > 0:
            lutador2.vida = lutador2.vida - ds2[numero]

    if lutador1.vida > lutador2.vida:
        print('vencedor' + lutador1.__str__())
        return lutador1
    else:
        print('vencedor' + lutador2.__str__())
        return lutador2


def duelo():
    duelosemifinal = []
    duelofinal = []
    duelosemifinal.append(luta(lutadores[0], lutadores[1]))
    duelosemifinal.append(luta(lutadores[2], lutadores[3]))
    duelosemifinal.append(luta(lutadores[4], lutadores[5]))
    duelosemifinal.append(luta(lutadores[6], lutadores[7]))

    duelofinal.append(luta(duelosemifinal[0], duelosemifinal[1]))
    duelofinal.append(luta(duelosemifinal[2], duelosemifinal[3]))

    vencedor = luta(duelofinal[0], duelofinal[1])
    print("quem ganhou a luta final foi: " + vencedor.__str__())

duelo()
