#include <string>
#include <vector>
#include <algorithm>
#include <boost/algorithm/string.hpp>

using namespace std;
namespace anagram {
  class anagram {
    string targetWord;
    public:
    anagram(string);
    vector<string> matches(vector<string> const&);
    private:
    bool isAnagram(string const&, string const&);
    string sortString(string&);
  };
}
