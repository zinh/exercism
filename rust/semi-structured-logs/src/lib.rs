// This stub file contains items which aren't used yet; feel free to remove this module attribute
// to enable stricter warnings.
#![allow(unused)]

/// various log levels
#[derive(Clone, PartialEq, Debug)]
pub enum LogLevel {
    Info,
    Warning,
    Error,
    Debug
}
/// primary function for emitting logs
pub fn log(level: LogLevel, message: &str) -> String {
    if level == LogLevel::Info {
        format!("[INFO]: {}", message)
    } else if level == LogLevel::Warning {
        format!("[WARNING]: {}", message)
    } else if level == LogLevel::Debug {
        format!("[DEBUG]: {}", message)
    } else {
        format!("[ERROR]: {}", message)
    }
}
pub fn info(message: &str) -> String {
    log(LogLevel::Info, message)
}
pub fn warn(message: &str) -> String {
    log(LogLevel::Warning, message)
}
pub fn error(message: &str) -> String {
    log(LogLevel::Error, message)
}
