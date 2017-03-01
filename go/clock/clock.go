package clock
import ("fmt")

const testVersion = 4

type Clock struct { hour, minute int }

func New(hour, minute int) Clock {
  if minute < 0 {
    hour = hour - 1 + minute / 60
    minute = 60 + minute % 60
  }

  if hour < 0 {
    hour = 24 + hour % 24
  }
  return Clock{((hour + minute / 60) % 24), (minute % 60)}
}

func (c Clock) String() string {
  return fmt.Sprintf("%02d:%02d", c.hour, c.minute)
}

func (c Clock) Add(minutes int) Clock {
  current_minute := c.minute + minutes
  return New(c.hour, current_minute)
}
