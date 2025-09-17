# Programacao_com_Python-25E3_2_AT

O AT proposto deve implementar um caixa de supermercado de forma que o operador do caixa insira os produtos e as quantidades e, ao final, exiba uma “nota fiscal” com os itens comprados e o total da compra. Ao final do programa, deverá ser exibido um extrato com o total das vendas do caixa. Considere que existe apenas um caixa operando no supermercado.

1. Crie um diretório para armazenar todos os programas e arquivos desenvolvidos neste projeto, inclusive o arquivo de produtos, descrito posteriormente, que será processado na abertura e fechamento do caixa.
2. Inicialmente, o programa deverá abrir o caixa e ler um arquivo de produtos no formato CSV (produtos.csv) com os dados abaixo e armazenar em uma lista de produtos. Cada produto tem um id, um nome, a quantidade em estoque e o seu preço. **Não deverá ser utilizado estruturas do tipo dicionário, apenas listas. Também não deve ser utilizado o conceito de Orientação a Objetos, ou seja, classes.**1,Produto 1,1,102,Produto 2,2,203,Produto 3,3,304,Produto 4,4,405,Produto 5,5,50
3. Afinal do programa, ou seja, no fechamento do caixa, a lista de produtos deverá ser gravada no mesmo arquivo com as alterações feitas durante o processamento, que serão detalhadas nos próximos itens.
4. Após a abertura do caixa, o atendente poderá realizar o atendimento de vários clientes. Para cada cliente, o programa deverá exibir a opção de “Iniciar atendimento” e ao final do atendimento exibir a opção “Finalizar atendimento”.
5. Cada cliente, deverá ser identificado como “Cliente #”, onde # deverá ser o número do cliente atendido. Por exemplo, o primeiro cliente deverá ser identificado como “Cliente 1”, o segundo como “Cliente 2” e assim por diante.
6. Para cada cliente, o atendente deve inserir uma lista de itens referentes a cada produto comprado. Cada item deve ser armazenado em uma lista de itens que deve conter o id do item, o nome do produto, a quantidade do produto, o preço unitário e o preço total do item.
7. O preço total do item é a multiplicação do preço unitário do produto e a quantidade do produto comprado pelo cliente.
8. Para cada item, o atendente deve inserir o id do produto e a quantidade a ser comprada. O id do produto deve constar da lista de produtos. Por exemplo, no arquivo produtos.csv, apresentado anteriormente, o id do produto deve estar entre um e cinco, caso contrário o programa deverá exibir uma mensagem de erro “Erro: produto não cadastrado.
9. A quantidade de produtos comprados deve ser maior que zero, caso contrário o programa deverá exibir uma mensagem de erro “Erro: quantidade deve ser maior que zero”. Não se preocupe se a quantidade de produtos no estoque estará disponível para a compra.
10. Para cada item comprado, o programa deverá dar a baixa no estoque, ou seja, subtrair a quantidade do produto comprado da lista de produtos.
11. Quando o caixa finalizar o atendimento de um cliente, o programa deverá exibir uma “nota fiscal” com as informações abaixo. Para formatar os dados de saída em forma de tabela, você pode utilizar a formatação do próprio Python ou utilizar um pacote que facilite esse processo. Nos exemplos abaixo, foi utilizado o pacote [Tabulate](https://pypi.org/project/tabulate/).
    
    ![image.png](attachment:d0abdc61-4a59-45d2-9389-3b80c313e308:image.png)
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfVmKAp-H-Dal5JY85lyZjEtA-v6uD209N7qITYpBKU2vZQGRWmGvMEHk8I56Ig34E4gGe3iwA49PdMeaDN9qlGgrPyu0G8ScB8BaLQjhOca8bbuR6IHhwUpRt8kXq3ZwoTLufsyw?key=LLOVojLWOoIW5GFyeZmVTBM8)
    
12. Quando o atendente fechar o caixa, o programa deverá exibir uma lista de clientes atendidos com o total de compra de cada cliente e o total de vendas realizadas, como no exemplo abaixo.
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcPIsD_NJpJDpHlND8_wmqmewZXlkT-_ZBn1_oU22ZuKz0yQX-QfQCS22fDZBCBbDR4kRh30XJ0HrmDtH6DnovRRyOPYXHp1WsuzMe7V9-k8XgPG8l-My1XOsnDaCO6L7fenl-eaw?key=LLOVojLWOoIW5GFyeZmVTBM8)
    
13. Além disso, o programa deverá exibir uma lista de produtos que estejam sem estoque, ou seja, a quantidade do produto igual a zero. Considerando os exemplos anteriores, o programa exibirá a saída abaixo:
    
    ![image.png](attachment:f46cfc67-70fb-403d-8de8-f239c244cb2d:image.png)
    
14. Finalmente, o programa deverá gravar o arquivo de produtos atualizado, ou seja, com o novo estoque de cada produto vendido.
15. O sistema considerou que apenas um caixa estava operando no supermercado. Cite um problema caso houvesse mais de um caixa operando ao mesmo tempo no supermercado?
16. Qual seria uma possível solução para o problema anterior considerando o conteúdo apresentado no bloco?
