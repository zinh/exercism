class WordCount {
  Map<String, int> countWords(String s) {
    final exp = RegExp(r"([a-zA-Z0-9]+('[a-zA-Z0-9]+)*)");
    var m = <String, int>{};

    for (var word in exp.allMatches(s.toLowerCase()).map((match) => match[0])) {
      if (m.containsKey(word)) {
        m[word] += 1;
      } else {
        m[word] = 1;
      }
    }
    return m;
  }
}
