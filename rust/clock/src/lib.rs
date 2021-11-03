use std::fmt;

#[derive(Eq, Debug)]
pub struct Clock {
    hours: i32,
    minutes: i32,
}

impl Clock {
    pub fn new(hours: i32, minutes: i32) -> Self {
        let mut new_hours = hours;
        let mut new_minutes = minutes;
        if minutes < 0 {
            new_minutes = minutes.rem_euclid(60);
            new_hours += minutes.div_euclid(60);
        }
        if new_hours < 0 {
            new_hours = new_hours.rem_euclid(24);
        }
        if new_minutes >= 60 {
            new_hours = new_hours + new_minutes.div_euclid(60);
            new_minutes = new_minutes.rem_euclid(60);
        }
        if new_hours >= 24 {
            new_hours = new_hours.rem_euclid(24);
        }
        Clock{ hours: new_hours, minutes: new_minutes }
    }

    pub fn add_minutes(&self, minutes: i32) -> Self {
        Clock::new(self.hours, self.minutes + minutes)
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
