#include "etl.h"

using namespace std;
namespace etl {
  map<char, int> transform(std::map<int, std::vector<char>> const& old) {
    map<char, int> results;
    for (auto element : old) {
      int score = element.first;
      vector<char> labels = element.second;
      for(auto label : labels){
        results[label] = score;
      }
    }
    return results;
  }
}
