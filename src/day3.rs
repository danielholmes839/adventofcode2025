fn part1_power(line: &str) -> i32 {
    let digits: Vec<i32> = line
        .as_bytes()
        .iter()
        .map(|ch| (ch - b'0').into())
        .collect();

    let mut max = 0;
    let digits_max_to_left: Vec<_> = digits.iter().map(|digit| {
        if max < *digit {
            max = *digit;
        }
        return max
    }).collect();

    let mut max_power = 0;
    for i in (1..digits.len()).rev() {
        let power = 10 * digits_max_to_left[i-1] + digits[i];
        if power > max_power {
            max_power = power;
        }
    }

    max_power
}

fn main() {
    let path = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "data/day3.txt".to_string());

    println!("reading {}", path);

    let data = std::fs::read_to_string(path).unwrap();
    let sum: i32 = data.lines().map(|line| {
        let power = part1_power(line);
        println!("{} {}", line, power);
        power
    }).sum();

    println!("{}", sum);
}
