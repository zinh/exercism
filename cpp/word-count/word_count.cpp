#include "word_count.h"

using namespace std;
namespace word_count {
  map<string, int> words(string input) {
    auto it = std::find_if(input.begin(), input.end(), [](const char element) -> bool{
        return std::is_space(element) || std::ispunct(element);
        });
  }
}
