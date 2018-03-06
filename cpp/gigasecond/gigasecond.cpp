#include "gigasecond.h"
using namespace boost::posix_time;
namespace gigasecond {
  ptime
    advance(ptime input){
      return input + seconds(1000000000);
    }
}
