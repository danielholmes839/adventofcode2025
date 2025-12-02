fn rotations_past_0(initial_rotation: i32, direction: i32, turns: i32) -> i32 {
    // for even rotations of 100 just return that divided by 100 as the number of times we point to 0
    let inc = turns / 100;
    if turns % 100 == 0 {
        return inc;
    }

    // if we start on 0, we can't go past an extra time
    if initial_rotation == 0 {
        return inc;
    }

    let final_rotation = (initial_rotation + direction * turns).rem_euclid(100);

    // if we end on 0, add 1
    if final_rotation == 0 {
        return inc + 1;
    }

    // if we turned right, and are now "behind" our initial rotation we went past 0
    if direction == 1 && final_rotation < initial_rotation {
        return inc + 1;
    }

    // if we turned left, and we are now "ahead" of our initial rotation we went past 0
    if direction == -1 && final_rotation > initial_rotation {
        return inc + 1;
    }

    // we did not pass 0
    return inc;
}

fn main() {
    let path = std::env::args()
        .nth(1)
        .unwrap_or_else(|| "data/day1.txt".to_string());

    println!("reading {}", path);

    let data = std::fs::read_to_string(path).unwrap();

    let mut password_part2 = 0;
    let mut password_part1 = 0;
    let mut rotation = 50;

    data.lines().for_each(|line| {
        let initial_rotation = rotation;
        let direction = match line.get(0..1).unwrap() {
            "R" => 1,
            "L" => -1,
            _ => panic!("invalid direction"),
        };

        let turns: i32 = line.get(1..).unwrap().parse().unwrap();

        rotation = (rotation + direction * turns).rem_euclid(100);

        // add number of times the dial is left on 0 for part 1
        if rotation == 0 {
            password_part1 += 1
        }

        password_part2 += rotations_past_0(initial_rotation, direction, turns);
    });

    println!(
        "password: {}, password part2: {}",
        password_part1, password_part2
    );
}

#[cfg(test)]
mod tests {
    use crate::rotations_past_0;

    #[test]
    fn part2() {
        let mut result: i32;

        result = rotations_past_0(0, 1, 100);
        assert_eq!(result, 1);

        result = rotations_past_0(0, -1, 100);
        assert_eq!(result, 1);

        result = rotations_past_0(0, 1, 200);
        assert_eq!(result, 2);

        result = rotations_past_0(0, -1, 200);
        assert_eq!(result, 2);

        result = rotations_past_0(75, 1, 24);
        assert_eq!(result, 0);

        result = rotations_past_0(75, 1, 25);
        assert_eq!(result, 1);

        result = rotations_past_0(75, 1, 26);
        assert_eq!(result, 1);

        result = rotations_past_0(75, -1, 74);
        assert_eq!(result, 0);

        result = rotations_past_0(75, -1, 75);
        assert_eq!(result, 1);

        result = rotations_past_0(75, -1, 76);
        assert_eq!(result, 1);

        result = rotations_past_0(0, -1, 1);
        assert_eq!(result, 0);

        result = rotations_past_0(0, 1, 1);
        assert_eq!(result, 0);

        result = rotations_past_0(1, -1, 102);
        assert_eq!(result, 2);
    }
}
