class ResistorColorDuo {
  final List<String> colors = [
    'black',
    'brown',
    'red',
    'orange',
    'yellow',
    'green',
    'blue',
    'violet',
    'grey',
    'white'
  ];
  int value(List<String> namedColors) {
    String c =
        namedColors.map((namedColor) => colors.indexOf(namedColor)).join();
    return int.parse(c);
  }
}
