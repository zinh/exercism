pub fn build_proverb(list: Vec<&str>) -> String {
    let mut idx: usize = 0;
    let mut result: Vec<String> = Vec::new();
    if list.len() == 0 {
        return String::new()
    }
    loop {
        let current_item = list[idx];
        if idx == list.len() - 1 {
            result.push(format!("And all for the want of a {}.", list[0]));
            break;
        } else {
            result.push(format!("For want of a {} the {} was lost.", current_item, list[idx + 1]));
        }
        idx = idx + 1;
    }
    return result.join("\n");
}
