#include "hamming.h"

namespace hamming {
  int compute(std::string left, std::string right){
    if (left.length() != right.length())
      throw std::domain_error("Length is not equal");
    int distance = 0;
    for(std::string::size_type i = 0; i < left.size(); i++){
      if (left[i] != right[i])
        distance++;
    }
    return distance;
  }
}
