#[derive(Debug)]
pub enum CalculatorInput {
    Add,
    Subtract,
    Multiply,
    Divide,
    Value(i32),
}

pub fn evaluate(inputs: &[CalculatorInput]) -> Option<i32> {
    let mut stack: Vec<i32> = Vec::new();
    for input in inputs {
        match input {
            CalculatorInput::Value(n) => stack.push(*n),
            CalculatorInput::Multiply => match stack.pop().and_then(|a| stack.pop().map(|b| a * b))
            {
                None => return None,
                Some(num) => stack.push(num),
            },
            CalculatorInput::Divide => match stack.pop().and_then(|a| stack.pop().map(|b| b / a)) {
                None => return None,
                Some(num) => stack.push(num),
            },
            CalculatorInput::Add => match stack.pop().and_then(|a| stack.pop().map(|b| a + b)) {
                None => return None,
                Some(num) => stack.push(num),
            },
            CalculatorInput::Subtract => match stack.pop().and_then(|a| stack.pop().map(|b| b - a))
            {
                None => return None,
                Some(num) => stack.push(num),
            },
        }
    }
    if stack.len() > 1 {
        None
    } else {
        stack.pop()
    }
}
