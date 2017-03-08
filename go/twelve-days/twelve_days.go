package twelve
import(
  "strings"
  "fmt"
)

const testVersion = 1

func Song() string {
}

func Verse(line int) string {
	numbers := map[int][2]string{
		1:  [2]string{"a", "first", "Partridge"},
		2:  [2]string{"two", "second", "Turtle Doves"},
		3:  [2]string{"three", "third", "French Hens"},
		4:  [2]string{"four", "fourth", "Calling Birds"},
		5:  [2]string{"five", "fifth", "Gold Rings"},
		6:  [2]string{"six", "sixth", "Geese-a-Laying"},
		7:  [2]string{"seven", "seventh", "Swans-a-Swimming"},
		8:  [2]string{"eight", "eighth", "Maids-a-Milking"},
		9:  [2]string{"nine", "nineth", "Ladies Dancing"},
		10: [2]string{"ten", "tenth", "Lords-a-Leaping"},
		11: [2]string{"eleven", "eleventh", "Pipers Piping"},
		12: [2]string{"twelve", "twelfth", "Drummers Drumming"}
	}
        for i := 1; i <= line; i++ {
          fmt.Sprintf("%s %s", numbers[i][0], numbers[i][2])
        }
}
