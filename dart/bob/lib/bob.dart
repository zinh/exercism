class Bob {
  String response(String rawInput) {
    var input = rawInput.trim();
    if (noLetter(input) && !endByQuestion(input)) return 'Fine. Be that way!';
    if (endByQuestion(input)) {
      if (allCapital(input))
        return "Calm down, I know what I'm doing!";
      else
        return 'Sure.';
    }
    if (allCapital(input) && !onlyNumbers(input)) return 'Whoa, chill out!';

    return 'Whatever.';
  }

  bool endByQuestion(String input) {
    if (input.length == 0) return false;
    return input[input.length - 1] == '?';
  }

  bool allCapital(String input) => !RegExp(r'[a-z]').hasMatch(input);

  bool noLetter(String input) {
    RegExp exp = RegExp(r'[a-zA-Z0-9]');
    return !exp.hasMatch(input);
  }

  bool onlyNumbers(String input) =>
      !RegExp(r'[^a-zA-Z]').hasMatch(input) && RegExp(r'[0-9]').hasMatch(input);
}
