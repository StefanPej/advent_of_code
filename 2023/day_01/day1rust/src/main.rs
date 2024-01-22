use std::collections::HashMap;
use std::fs;

fn main() {
    let inp_raw = fs::read_to_string("input.txt").expect("wtf this bit do?");
    let inp: Vec<&str> = inp_raw.lines().collect();

    part_1(&inp);
    part_2(&inp);
}

fn part_1(inp: &Vec<&str>) {
    let mut nums: Vec<i32> = Vec::new();
    for line in inp {
        let chars: Vec<char> = line.chars().collect();
        let mut digits: Vec<char> = Vec::new();
        for char in chars {
            if char.is_numeric() {
                digits.push(char);
            }
        }

        let number = vec![digits[0].to_string(), digits[digits.len() - 1].to_string()].join("");
        let number_int = number.parse::<i32>().unwrap();

        nums.push(number_int);
    }
    let sum: i32 = nums.iter().sum();
    println!("Part 1: {}", sum);
}

fn part_2(inp: &Vec<&str>) {
    let mut nums: Vec<i32> = Vec::new();

    let mut nums_map = HashMap::new();
    nums_map.insert("one", "1");
    nums_map.insert("two", "2");
    nums_map.insert("three", "3");
    nums_map.insert("four", "4");
    nums_map.insert("five", "5");
    nums_map.insert("six", "6");
    nums_map.insert("seven", "7");
    nums_map.insert("eight", "8");
    nums_map.insert("nine", "9");
    nums_map.insert("1", "1");
    nums_map.insert("2", "2");
    nums_map.insert("3", "3");
    nums_map.insert("4", "4");
    nums_map.insert("5", "5");
    nums_map.insert("6", "6");
    nums_map.insert("7", "7");
    nums_map.insert("8", "8");
    nums_map.insert("9", "9");

    for line in inp {
        let mut digits: Vec<char> = Vec::new();
        let line_len = line.len();
        for i in 0..line_len {
            let sub_s = &line[i..];
            for &num in nums_map.keys() {
                if sub_s.starts_with(num) {
                    digits.push(nums_map.get(&num).unwrap().chars().next().unwrap());
                }
            }
        }
        let number = vec![digits[0].to_string(), digits[digits.len() - 1].to_string()].join("");
        let number_int = number.parse::<i32>().unwrap();

        nums.push(number_int);
    }
    let sum: i32 = nums.iter().sum();
    println!("Part 2: {}", sum);
}
