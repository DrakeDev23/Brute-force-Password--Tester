Disclaimer
FOR EDUCATIONAL PURPOSES ONLY - This tool is designed to help understand cybersecurity concepts and password strength. Only use on passwords you own or have explicit permission to test. Never use this against systems or accounts you don't own.

Features
Multi-method cracking - 4 different attack strategies

Real parallel processing - Utilizes all CPU cores for maximum speed

Smart pattern detection - Common password dictionary included

Auto character detection - Automatically identifies required character sets

Real-time progress tracking - Watch attempts and speed in real-time

Speed benchmarking - Compare performance across methods

Attack Methods Explained
1. Fast Crack (Direct Length Search)
How it works: Jumps directly to your password's exact length instead of wasting time trying shorter passwords first.

Best for: Passwords where you know the approximate length or want a balanced approach

Example: Cracking "abc123" (length 6) - Skips lengths 1-5 and starts testing 6-character combinations immediately

Speed: Moderate | Intelligence: Low | Cores: 1

2. Smart Crack (Common Patterns First)
How it works: Tries the most common passwords, dictionary words, and patterns before attempting brute force.

Priority order:

Top 15 most common passwords ("password", "123456", "admin", etc.)

Dictionary words ("cat", "dog", "bird", etc.)

Common patterns ("abc123", "admin123", etc.)

Brute force (if all else fails)

Best for: Weak or human-chosen passwords

Example: Cracking "admin" - Finds it in under 10 attempts instead of millions

Speed: Very fast on weak passwords | Intelligence: High | Cores: 1

3. Real Parallel Crack (Multi-Core)
How it works: Splits all possible password combinations equally across all your CPU cores and tests them simultaneously.

Technical details:

Detects your available CPU cores

Divides total combinations into equal chunks

Each core tests a different range of passwords

First core to find the password stops all others

Best for: Long, random, or complex passwords where maximum speed is needed

Example: With 8 CPU cores, cracks passwords 8x faster than single-core methods

Speed: Very fast (multi-core) | Intelligence: Low | Cores: All available

4. Speed Benchmark
How it works: Tests and compares cracking speed on different password types (numbers only, letters only, mixed)

Shows:

Time taken for each password length

Attempts per second rate

Performance comparison across methods

Best for: Understanding how password length and character set affect cracking time

System Requirements
Python 3.6 or higher

No external libraries required (uses only built-in modules)

Multi-core CPU recommended for parallel cracking

Installation
Clone the repository:

text
git clone https://github.com/yourusername/bruteforce-simulator.git
Navigate to the directory:

text
cd bruteforce-simulator
Run the program:

text
python bruteforce.py
Usage Examples
Test weak passwords:

text
Enter password: admin
Method: Smart Crack
Result: Found in 5 attempts (0.01 seconds)
Test numeric passwords:

text
Enter password: 12345
Method: Fast Crack
Result: Found in 12,345 attempts (0.05 seconds)
Test performance:

text
Enter password: abc123
Method: Real Parallel
Result: Found in 0.8 seconds using 8 cores
Security Lessons Learned
Password Length Matters - Each additional character exponentially increases cracking time

Avoid Common Passwords - "password", "123456", "admin" are cracked instantly

Use Mixed Character Sets - Lowercase + uppercase + numbers + symbols dramatically increases combinations

Strong Passwords Work - A 12-character random password would take centuries to crack

Real hackers use these same techniques with massive password databases and GPU clusters

Performance Comparison
Password	Fast Crack	Smart Crack	Parallel (8 cores)
admin	0.5 sec	0.01 sec	0.1 sec
abc123	3.0 sec	2.5 sec	0.4 sec
password123	8.0 sec	0.02 sec	1.0 sec
random8	30 sec	30 sec	4 sec
Technical Details
Built with Python standard libraries:

itertools - Generates password combinations

string - Provides character sets

time - Measures performance

multiprocessing - Enables parallel processing

Future Improvements
GPU acceleration support

Custom wordlist import

Hash cracking mode (MD5, SHA1, SHA256)

Resume functionality for long cracks

GUI interface

Contributing
Feel free to fork and submit pull requests. Focus areas:

Additional cracking algorithms

Performance optimizations

Better progress visualization

Documentation improvements

Author
-DrakeDev23-

Acknowledgments
Inspired by real-world password cracking tools like John the Ripper and Hashcat. Created for cybersecurity education and awareness.

