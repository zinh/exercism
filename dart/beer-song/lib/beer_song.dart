class BeerSong {
  List<String> recite(int start, int end) {
    var result = <String>[];
    for (var n = 0; n < end; n++) {
      result = result + verse(start - n);
      if (n < end - 1)
        result.add('');
    }
    return result;
  }

  List<String> verse(int n) {
    if (n > 2) {
      return [
        "${n} bottles of beer on the wall, ${n} bottles of beer.",
        "Take one down and pass it around, ${n - 1} bottles of beer on the wall."
      ];
    }

    if (n == 2)
      return [
        "2 bottles of beer on the wall, 2 bottles of beer.",
        "Take one down and pass it around, 1 bottle of beer on the wall."
      ];

    if (n == 1)
      return [
        "1 bottle of beer on the wall, 1 bottle of beer.",
        "Take it down and pass it around, no more bottles of beer on the wall."
      ];

    return [
      "No more bottles of beer on the wall, no more bottles of beer.",
      "Go to the store and buy some more, 99 bottles of beer on the wall."
    ];
  }
}
