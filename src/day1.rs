fn main() {
    let data = std::fs::read_to_string("data/day1_part1.txt").unwrap();

    let mut password = 0;
    let mut rotation = 50;

    data.lines().for_each(|line| {
        let direction = match line.get(0..1).unwrap() {
            "R" => 1,
            "L" => -1,
            _ => panic!("invalid direction")
        };

        let turns: i32 = line.get(1..).unwrap().parse().unwrap();
        rotation = (rotation + (direction * turns)) % 100;
        if rotation == 0 {
            password += 1
        }
    });

    println!("password: {}", password);
}
