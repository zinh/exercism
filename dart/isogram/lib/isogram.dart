class Isogram {
  bool isIsogram(String s) {
    var m = <int>{};
    for (var rune in s.toLowerCase().runes) {
      if (rune == 32 || rune == 45)
        continue;
      if (m.contains(rune))
        return false;
      else
        m.add(rune);
    }
    return true;
  }
}
