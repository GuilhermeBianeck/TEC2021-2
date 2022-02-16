import sys

 # A saída deve ser um arquivo texto com extensão .out com um 
 # programa capaz de ser executado no simulador a partir do modelo de fita duplamente infinita, 
 # não possui movimento estacionário e que n escreve o símbolo de branco _ na fita.

#  <new symbol> Não pode ser _ 

#  <current state> <current symbol> <new symbol> <direction> <new state>
ESTADO_ATUAL    = 0
SIMBULO_ATUAL   = 1
SIMBULO_NOVO    = 2
DIRECAO         = 3
ESTADO_NOVO     = 4




def convert(fita: str):
    # posicionamento da barreira na esquerda e redirecionamento
    saida = [["0 * * l 1?"],
    ["1? * £ r 0?"],["* £ £ r *"],]
    flag = False
    flag2 = False
    fitaAUX = []
    i = 0
        
    for line in fita:  
        sintaxe = line.replace("\n", "").split(" ")
        
        if flag == True: # Caso ele tenha encontrado um movimento estacionario e nao seja em um estado halt-accept.
            # aqui estamos jogando o estado modificado la pro final pois nao podemos perder ele, coloco ele em um auxiliar pra depois ser colocado junto no final do for todo
            # perceba que nao foi feito o mesmo no caso do halt-accept pois nao muda absolutamente nada, ja que ele vai aceitar! :)
            Formatacao = fita[i]
            Formatacao = Formatacao.replace("\n", "").split(" ")
            fitaAUX.append(Formatacao)
            print(line)
            sintaxe[DIRECAO] = "l" 
            sintaxe[ESTADO_ATUAL] = DestinoNovo
            sintaxe[ESTADO_NOVO] = DestinoOriginal
            sintaxe[SIMBULO_NOVO] = "*"
            sintaxe[SIMBULO_ATUAL] = "*"
            flag = False

        # aqui estamos tirando o movimento estacionario onde nao tem halt nem accept, ai a gente cria um novo estado e redireciona. mais detalhes no pdf.
        if sintaxe[DIRECAO] == "*" and sintaxe[ESTADO_NOVO] != "halt-accept" and sintaxe[ESTADO_NOVO] != "halt":
            sintaxe[DIRECAO] = "r" 
            DestinoOriginal = sintaxe[ESTADO_NOVO]
            sintaxe[ESTADO_NOVO] = sintaxe[ESTADO_NOVO] + "?" # os estados criados com esse objetivo sempre teráo o estado destino anterior + o simbulo " ? ".
            DestinoNovo = sintaxe[ESTADO_NOVO]
            flag = True  # esta flag serve para avisar que temos que criar um novo estado na proxima iteração line.
        # caso for haltaccept ou halt e tem movimento estacionaro apenas coloca pra direita pra facilitar, ja que vai aceitar mesmo.
        elif (sintaxe[DIRECAO] == "*" and sintaxe[ESTADO_NOVO] != "halt-accept") or (sintaxe[DIRECAO] == "*" and sintaxe[ESTADO_NOVO] != "halt"):
            sintaxe[DIRECAO] = "r" 


        if sintaxe[ESTADO_ATUAL] == "0":
            sintaxe[ESTADO_ATUAL] = "0?"
        if sintaxe[ESTADO_NOVO] == "0":
            sintaxe[ESTADO_NOVO] = "0?"

        if flag2 == True: # Caso ele tenha encontrado um espaço em branco
            # aqui estamos jogando o estado modificado la pro final pois nao podemos perder ele, coloco ele em um auxiliar pra depois ser colocado junto no final do for todo
            Formatacao = fita[i]
            Formatacao = Formatacao.replace("\n", "").split(" ")
            fitaAUX.append(Formatacao)
            # criando a nova flecha para acomodar o novo § inserido na iteração
            sintaxe[SIMBULO_ATUAL] = "§"
            sintaxe[SIMBULO_NOVO] = "§"
            sintaxe[ESTADO_ATUAL] = OrigemAntiga
            sintaxe[ESTADO_NOVO] = DestinoOriginal
            flag2 = False
        
        if sintaxe[SIMBULO_NOVO] == "_":
            DestinoOriginal = sintaxe[ESTADO_NOVO]
            OrigemAntiga = sintaxe[ESTADO_ATUAL]
            sintaxe[SIMBULO_NOVO] = "§"
            flag2 = True
       

        saida.append(sintaxe)
        i = i+1


    print("alocados para o final da fita: ", fitaAUX)
    saida.extend(fitaAUX)
    return saida

def ler_arquivo(path: str):
    arquivo_entrada = open(path, "r") 
    lines = arquivo_entrada.readlines()
    arquivo_entrada.close()
    saida = None
    saida = convert(lines[0:])
    arquivo_saida = open(path.split(".")[0] + ".out", "w")
    for line in saida:
        arquivo_saida.write(" ".join(line) + "\n")
    arquivo_saida.close()

if __name__ == "__main__":
    arquivo_entrada = sys.argv[1]
    ler_arquivo(arquivo_entrada)

    