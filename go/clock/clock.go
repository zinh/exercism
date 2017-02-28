package clock
import ("fmt")

const testVersion = 4

type Clock struct { hour, minute int }

func New(hour, minute int) Clock {
  return Clock{((hour + minute / 60) % 24), (minute % 60)}
}

func (c Clock) String() string {
  return fmt.Sprintf("%02d:%02d", c.hour, c.minute)
}

func (c Clock) Add(minutes int) Clock {
  current_minute := c.minute + minutes
  c.hour = (c.hour + (current_minute) / 60) % 24
  c.minute = (current_minute % 60)
  return c
}
