use time::PrimitiveDateTime as DateTime;
use time::Duration;

pub fn after(start_date: DateTime) -> DateTime {
    start_date + Duration::seconds(1_000_000_000)
}
