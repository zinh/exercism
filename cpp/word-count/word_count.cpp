#include "word_count.h"

using namespace std;
namespace word_count {
  map<string, int> words(string input){
    map<string, int> result{{input, 1}};
    return result;
  }
}
