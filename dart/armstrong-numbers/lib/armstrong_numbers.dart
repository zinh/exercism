import 'dart:math';

class ArmstrongNumbers {
  bool isArmstrongNumber(int n) {
    final digitsN = digits(n);
    final l = digitsN.length;
    final digitsPower = digitsN.map((d) => pow(d, l));
    final s = digitsPower.reduce((a, b) => a + b);
    return s == n;
  }

  List<int> digits(int n) {
    if (n == 0)
      return [0];
    var result = <int>[];
    while(n > 0) {
      result.add(n % 10);
      n = n ~/ 10;
    }
    return result;
  }
}
