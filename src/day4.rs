fn part1(rows: Vec<Vec<u8>>) -> i32 {
    let offsets: Vec<(i32, i32)> = vec![
        (-1, 1),
        (1, 0),
        (1, 1),
        (-1, 0),
        (1, 0),
        (-1, -1),
        (-1, 0),
        (1, -1),
    ];

    let mut count = 0;

    for i in 0..rows.len() {
        for j in 0..rows.get(i).unwrap().len() {
            if rows.get(i).unwrap().get(j).unwrap() != &b'@' {
                continue
            } 

            let mut adjacent = 0;
            for (di, dj) in offsets.iter() {
                // ??????????????????????
                if let Some(new_i) = i.checked_add_signed(*di as isize) {
                    if let Some(new_j) = j.checked_add_signed(*dj as isize) {
                        
                        if let Some(row) = rows.get(new_i) {
                            if let Some(chr) = row.get(new_j) {
                                if chr == &b'@' {
                                    adjacent += 1;
                                }
                            }
                        }
                    }
                }
            }

            if adjacent < 4 {
                count += 1;
            }
        }
    }

    count
}

fn main() {
    let path = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "data/day4.txt".to_string());

    println!("reading {}", path);

    let data = std::fs::read_to_string(path).unwrap();

    let rows: Vec<Vec<u8>> = data.lines().map(|line| line.bytes().collect()).collect();

    println!("{}", part1(rows));
}
