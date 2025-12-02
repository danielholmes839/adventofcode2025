fn part1(ranges: &Vec<(i64, i64)>) -> i64 {
    let mut sum: i64 = 0;

    for (start, end) in ranges {
        for n in *start..*end + 1 {
            let nstr = n.to_string();
            if nstr.len() % 2 != 0 {
                continue;
            }

            let m = nstr.len() / 2;

            if nstr[0..m] == nstr[m..nstr.len()] {
                sum += n;
            }
        }
    }

    sum
}

fn main() {
    let path = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "data/day2.txt".to_string());

    println!("reading {}", path);

    let data = std::fs::read_to_string(path).unwrap();

    let ranges: Vec<_> = data
        .split(",")
        .map(|range| {
            let i = range.find("-").unwrap();
            let start: i64 = range[0..i].parse().unwrap();
            let end: i64 = range[i + 1..range.len()].parse().unwrap();
            (start, end)
        })
        .collect();

    println!("{}", part1(&ranges));
}
