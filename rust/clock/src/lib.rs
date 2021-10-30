use std::fmt;

#[derive(Eq, Debug)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        Clock { hours, minutes }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        let new_minutes = self.minutes + minutes;
        if new_minutes < 60 {
            return Clock {
                hours: self.hours,
                minutes: new_minutes,
            };
        }
        let new_hours = self.hours + (new_minutes / 60);
        if new_hours < 24 {
            return Clock {
                hours: new_hours,
                minutes: new_minutes % 60,
            };
        }
        Clock {
            hours: new_hours % 24,
            minutes: new_minutes % 60,
        }
    }
}

impl fmt::Display for Clock {
    fn fmt(&self, f: &mut fmt::Formatter<'_>) -> fmt::Result {
        write!(f, "{:02}:{:02}", self.hours, self.minutes)
    }
}

impl std::cmp::PartialEq for Clock {
    fn eq(&self, other: &Self) -> bool {
        self.hours == other.hours && self.minutes == other.minutes
    }
}
