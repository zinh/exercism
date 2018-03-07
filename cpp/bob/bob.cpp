#include "bob.h"
#include <boost/algorithm/string/trim.hpp>
#include <boost/algorithm/string/predicate.hpp>
#include <boost/algorithm/string/classification.hpp>

using namespace std;
namespace bob {
  string hey(string msg){
    boost::trim(msg);
    if (is_blank(msg))
      return "Fine. Be that way!";
    if (is_contain_letter(msg) && !is_contain_lowercase(msg))
      return "Whoa, chill out!";
    if (is_question(msg)) {
      return "Sure.";
    }
    return "Whatever.";
  }

  bool is_blank(string msg){
    return (msg == "");
  }

  bool is_question(string msg){
    return boost::ends_with(msg, "?");
  }

  bool is_contain_lowercase(string msg){
    for(auto c : msg){
      if (c >= 'a' && c <= 'z')
        return true;
    }
    return false;
  }

  bool is_contain_letter(string msg){
    for(auto c : msg){
      if ((c >= 'A' && c <= 'Z') || (c >= 'a' && c <= 'z')){
        return true;
      }
    }
    return false;
  }
}
