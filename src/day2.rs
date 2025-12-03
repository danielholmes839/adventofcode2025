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

fn part2(ranges: &Vec<(i64, i64)>) -> i64 {
    let mut sum: i64 = 0;

    for (start, end) in ranges {
        for n in *start..*end + 1 {
            let str = n.to_string();
            let n_length = str.len();

            // println!("check num: {}", n);

            for pattern_length in 1..std::cmp::max(n_length/2, 2)+1 {
                if pattern_length == n_length {
                    continue
                }

                if n_length % pattern_length != 0 {
                    // println!("skip #1 check: {} {}", n, pattern);
                    continue
                }

                let pattern = &str[0..pattern_length];

                
                // println!("check: {} {}", n, pattern);

                let mut repeats = true;

                for i in 0..(n_length/pattern_length) {
                    if &str[i*pattern_length..(i+1)*pattern_length] != pattern {
                        repeats = false;
                        break
                    }
                }

                if repeats {
                    sum += n;
                    println!("for range {}-{}, {} {}", start, end, n, pattern);
                    break
                }
            }
        }
    }

    sum
}


// number needs to be made of a repeating sequence

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
    println!("{}", part2(&ranges));
}

mod tests {
    use crate::part2;


    #[test]
    fn tests() {
        let ranges = vec![(998, 1012)];
        let result = part2(&ranges);
        assert_eq!(result, 2009);
    }
}