#include "anagram.h"

namespace anagram {
  anagram::anagram(string in){
    targetWord = in;
  }
  vector<string> anagram::matches(vector<string> const& words){
    vector<string> results;
    for(auto const& word : words){
      if (isAnagram(targetWord, word)){
        results.push_back(word);
      }
    }
    return results;
  }

  bool anagram::isAnagram(string const& left, string const& right){
    string sortedLeft = left;
    string sortedRight = right;
    boost::to_lower(sortedLeft);
    boost::to_lower(sortedRight);
    if (sortedLeft == sortedRight)
      return false;
    sort(sortedLeft.begin(), sortedLeft.end());
    sort(sortedRight.begin(), sortedRight.end());
    if (sortedLeft == sortedRight)
      return true;
    return false;
  }
}
