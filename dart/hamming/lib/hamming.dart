class Hamming {
  int distance(String a, String b) {
    if (a.length != b.length)
      throw ArgumentError("left and right strands must be of equal length");
    if (a.length == 0)
      throw ArgumentError("no strand must be empty");
    var bRunes = b.runes.toList();
    var idx = -1;
    return a.runes.fold(0, (int value, int element) {
      idx += 1;
      if (bRunes[idx] != element)
        return value + 1;
      else
        return value;
    });
  }
}
