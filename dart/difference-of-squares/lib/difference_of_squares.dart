class DifferenceOfSquares {
  int squareOfSum(int n) {
    int s = (n * (n + 1)) ~/ 2;
    return s*s;
  }

  int sumOfSquares(int n) {
    return (new List<int>.generate(n, (i) => i + 1)).reduce((memo, element) => memo + element*element);
  }

  int differenceOfSquares(int n) {
    return squareOfSum(n) - sumOfSquares(n);
  }
}
