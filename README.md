# Pi Digits Repository

This repository contains different sets of digits of the mathematical constant π (pi). The digits are computed using a high-performance algorithm and stored using Git LFS (Large File System) due to the large size of the files.

## Files

- `pi_digits_1000.txt`: The first 1000 digits of pi.
- `pi_digits_10000.txt`: The first 10,000 digits of pi.
- `pi_digits_100000.txt`: The first 100,000 digits of pi.
- `pi_digits_1000000.txt`: The first 1,000,000 digits of pi.
- `pi_digits_10000000.txt`: The first 10,000,000 digits of pi.
- `pi_digits_100000000.txt`: The first 100,000,000 digits of pi.

## Usage

To clone this repository and access the pi digit files, you can use the following command:

```bash
git clone --recursive https://github.com/your_username/pi-digits-repository.git
```

## Contributing

If you would like to contribute to this repository by adding more pi digits, please follow the format below:

1. Start the file with a line `3.`.
2. The digits must be formatted with a line break after every 50 digits.
3. Each line must contain a space between 10 digits.
4. Include the digit position (e.g., `: 50`, `: 100`, etc.) at the end of each line.

Example:
```plaintext
3.
1415926535 8979323846 2643383279 5028841971 6939937510 : 50
5820974944 5923078164 0628620899 8628034825 3421170679 : 100
8214808651 3282306647 0938446095 5058223172 5359408128 : 150
. . .
9948682556 3967530560 3352869667 7734610718 4471868529 : 99999950
7572203175 2074898161 1683139375 1497058112 0187751592 : 100000000
```
