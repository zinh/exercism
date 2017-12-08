pub fn reply(message: &str) -> &str {
    if is_blank(message.trim()) {
        return "Fine. Be that way!";
    }
    if is_contain_letter(message.trim()) && !is_contain_lowercase(message.trim()) {
        return "Whoa, chill out!";
    }

    if is_question(message.trim()) {
        return "Sure.";
    }

    return "Whatever.";
}

pub fn is_question(message: &str) -> bool {
    message.ends_with("?")
}

pub fn is_blank(message: &str) -> bool {
    message == ""
}

pub fn is_contain_lowercase(message: &str) -> bool {
    for c in message.chars() {
        if c.is_lowercase() {
            return true;
        }
    }
    return false;
}

fn is_contain_letter(message: &str) -> bool {
    for c in message.chars() {
        if c.is_alphabetic() {
            return true;
        }
    }
    return false;
}
