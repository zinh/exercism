package house

const testVersion = 1

func Verse(line int) string {
  lyrics := map[string]string {
    "ate": "the malt",
    "killed": "the rat",
    "worried": "the cat",
    "tossed": "the dog",
    "milked": "the cow with the crumpled horn",
    "kissed": "the maiden all forlorn",
    "married": "the man all tattered and torn",
    "woke": "the priest all shaven and shorn",
    "kept": "the rooster that crowed in the morn",
    "belonged": "to the farmer sowing his corn" }

  if line <= 1 {
    return "This is the house that Jack built."
  }
  Verse(line - 1)
}

func Song() string {
  return Verse(1)
}
