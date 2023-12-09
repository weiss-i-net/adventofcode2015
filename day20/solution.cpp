#include <iostream>
#include <vector>
#include <algorithm>

int main() {
  const int num = 33100000;
  const int max_house = num / 10;
  std::vector<int> houses(max_house, 0);

  // Part 1
  for (int i = 1; i < max_house; ++i) {
    for (int j = i; j < max_house; j += i) {
      houses[j] += i;
    }
  }

  auto part1_it = std::find_if(houses.begin(), houses.end(), [num](int p) { return 10 * p >= num; });
  int part1 = std::distance(houses.begin(), part1_it);
  std::cout << "Part 1: " << part1 << std::endl;

  // Part 2
  std::fill(houses.begin(), houses.end(), 0); // Resetting the houses vector
  for (int i = 1; i < max_house; ++i) {
    for (int j = 1; j <= 50; ++j) {
      if (i * j >= max_house) {
        break;
      }
      houses[i * j] += i;
    }
  }

  auto part2_it = std::find_if(houses.begin(), houses.end(), [num](int p) { return 11 * p >= num; });
  int part2 = std::distance(houses.begin(), part2_it);
  std::cout << "Part 2: " << part2 << std::endl;

  return 0;
}
