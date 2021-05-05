class SpaceAge {
  final ages = <String, double>{
    'Mercury': 0.2408467,
    'Venus': 0.61519726,
    'Earth': 1,
    'Mars': 1.8808158,
    'Jupiter': 11.862615,
    'Saturn': 29.447498,
    'Uranus': 84.016846,
    'Neptune': 164.79132
  };

  double age({String planet, int seconds}) {
    final int secondsInYear = 31557600;
    var earthYear = ages[planet];
    return double.parse((seconds / (secondsInYear * earthYear)).toStringAsFixed(2));
  }
}
