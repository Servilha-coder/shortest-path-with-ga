## Algoritmo Genético para o Caminho Mais Curto
Uso
O script principal para executar o algoritmo genético é `main.py`. Você pode configurar os parâmetros do algoritmo genético editando o arquivo `config.json`.

## Configuração
- `population_size`: Número de indivíduos na população
- `mutation_rate`: Probabilidade de mutação em um indivíduo
- `num_generations`: Número de gerações para evoluir
- `crossover_method`: Método para realizar o cruzamento (por exemplo, um ponto, dois pontos)
- `selection_method`: Método para seleção (por exemplo, torneio, roleta)
- `graph`: Representação do grafo como matriz de adjacência ou lista
  
## Executando o Algoritmo
```bash
python main.py
```
## Exemplo
Aqui está um exemplo de como usar o algoritmo genético para encontrar o caminho mais curto em um grafo de exemplo.

Defina seu grafo em config.json:

```json
{
  "population_size": 100,
  "mutation_rate": 0.01,
  "num_generations": 200,
  "crossover_method": "one-point",
  "selection_method": "tournament",
  "graph": {
    "nodes": ["A", "B", "C", "D", "E"],
    "edges": {
      "A": {"B": 1, "C": 4},
      "B": {"A": 1, "C": 2, "D": 5},
      "C": {"A": 4, "B": 2, "D": 1},
      "D": {"B": 5, "C": 1, "E": 3},
      "E": {"D": 3}
    }
  }
}
```

Observe a saída, que mostrará o caminho mais curto encontrado e sua distância.

### Contribuições
Contribuições são bem-vindas! Por favor, siga estes passos:

Fork o repositório
Crie um novo branch (git checkout -b feature-branch)
Faça commit das suas mudanças (git commit -am 'Adicionar nova feature')
Faça push para o branch (git push origin feature-branch)
Crie um novo Pull Request
## Licença
Este projeto é licenciado sob a Licença MIT. Veja o arquivo LICENSE para detalhes.

## Contato
Se você tiver alguma pergunta ou sugestão, sinta-se à vontade para entrar em contato comigo em seu-email@example.com.

Obrigado por usar o Algoritmo Genético para o Caminho Mais Curto! Feliz codificação!
