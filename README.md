
# Genetic Algorithm for Shortest Path

## Usage

The main script to run the genetic algorithm is `main.py`. You can configure the parameters of the genetic algorithm by editing the `config.json` file.

### Configuration

- `population_size`: Number of individuals in the population
- `mutation_rate`: Probability of mutation in an individual
- `num_generations`: Number of generations to evolve
- `crossover_method`: Method to use for crossover (e.g., one-point, two-point)
- `selection_method`: Method to use for selection (e.g., tournament, roulette-wheel)
- `graph`: Representation of the graph as an adjacency matrix or list

### Running the Algorithm

```bash
python main.py
```

### Example

Here's an example of how to use the genetic algorithm to find the shortest path in a sample graph.

Define your graph in `config.json`:

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

Run the genetic algorithm:

```bash
python main.py
```

Observe the output, which will show the shortest path found and its distance.

## Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

## Contact

If you have any questions or suggestions, feel free to reach out to me at `your-email@example.com`.

Thank you for using the Genetic Algorithm for Shortest Path! Happy coding!
```

Now you can copy the above content and paste it directly into your GitHub README file.
