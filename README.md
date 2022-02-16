Trabalho Prático

Link GIT https://github.com/GuilhermeBianeck/TEC2021-2/

O objetivo deste trabalho é trabalhar a simulação entre modelos de máquina de Turing. Para isto, será utilizada a sintaxe disponível no simulador online de máquinas de Turing em http://morphett.info/turing/turing.html

O trabalho consistirá na programação de um "tradutor" de modelos de máquina de Turing. 
A entrada será um arquivo texto com extensão .in com um programa para o simulador online, consistindo em um programa para a máquina de Turing utilizando fita semi-infinita (modelo de Sipser) e podendo fazer uso de movimento estacionário. 
A saída deve ser um arquivo texto com extensão .out com um programa capaz de ser executado no simulador a partir do modelo de fita duplamente infinita, SEM movimento estacionário e que NÃO escreve o símbolo de branco _ na fita.

Os arquivos serão constituídos exclusivamente de linhas no formato

    <current state> <current symbol> <new symbol> <direction> <new state>

conforme especificado no site do simulador (sem uso de comentários no arquivo de entrada). O estado inicial será sempre nomeado como 0.
Tem-se a garantia de que os símbolos £,¢,§ não serão utilizados em nenhum arquivo de entrada, podendo ser utilizados como eventuais símbolos auxiliares.
O programa deverá retornar como saída um arquivo txt com um programa equivalente para o simulador online com tipo de fita inverso ao indicado no arquivo de entrada.
Os arquivos de entrada serão apenas de máquinas de Turing determinísticas e com codificação válida para o simulador. 
Todos os programas dados como entrada serão para reconhecimento de linguagens sobre o alfabeto {0,1}. Note, portanto, que a máquina de Turing dada como saída também será um reconhecedor para essa mesma linguagem sobre o alfabeto {0,1}.
O programa deve ser possível de ser executado em um computador com sistema operacional Ubuntu 20.04.2 LTS de 64 bits. A linguagem de implementação é livre dentro destas restrições.
A entrega deverá ser feita via moodle, com o programa final, instruções claras de execução caso necessárias e endereço de repositório público no github com todo o código-fonte.


