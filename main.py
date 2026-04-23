import itertools
import string
import time
import multiprocessing
from functools import partial

def drake_ascii():
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⠛⠛⠛⠛⠛⠛⠛⠷⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⣠⠤⠤⠤⠤⠤⠤⠤⠤⣄⠀⠀⠀⠘⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⢹⡆⠀⠀⠀⢹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⢀⣀⣀⣀⡀⠀⢸⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⣴⠟⠉⠉⠙⠻⣦⢸⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⢰⡏⠀⠀⠀⠀⠀⠀⢹⡇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠘⣧⡀⠀⠀⠀⠀⢀⣼⠇⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠈⠙⠛⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡀⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣧⠀⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣆⠀⠀⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢷⣄⢸⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡴⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⣷⣤⣤⣤⣤⣤⣤⣤⣤⣴⠾⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    
    By: DrakeDev23
    """)

def fast_brute_force():
    drake_ascii()
    print("\n" + "="*60)
    print("BRUTE FORCE")
    print("="*60)
    
    print("\nEnter a password to crack:")
    target = input("Password: ").strip()
    
    if not target:
        target = "abc123"
        print(f"Using default: {target}")
    
    has_digits = any(c.isdigit() for c in target)
    has_lower = any(c.islower() for c in target)
    has_upper = any(c.isupper() for c in target)
    
    chars = ""
    if has_digits:
        chars += string.digits
    if has_lower:
        chars += string.ascii_lowercase
    if has_upper:
        chars += string.ascii_uppercase
    
    if not chars:
        chars = string.ascii_lowercase
    
    print(f"\n[*] Target: '{target}' (length: {len(target)})")
    print(f"[*] Character set size: {len(chars)}")
    print("-"*50)
    
    attempts = 0
    start_time = time.time()
    found = False
    
    print(f"\n[>] Trying passwords of length {len(target)}...")
    
    for guess_tuple in itertools.product(chars, repeat=len(target)):
        attempts += 1
        guess = ''.join(guess_tuple)
        
        if attempts % 100000 == 0:
            elapsed = time.time() - start_time
            print(f"    Attempts: {attempts:,} | Time: {elapsed:.1f}s | Speed: {attempts/elapsed:,.0f}/s")
        
        if guess == target:
            elapsed = time.time() - start_time
            print("\n" + "="*50)
            print(f"SUCCESS! Password found: '{guess}'")
            print(f"Total attempts: {attempts:,}")
            print(f"Time taken: {elapsed:.2f} seconds")
            print(f"Speed: {attempts/elapsed:,.0f} attempts/second")
            print("="*50)
            found = True
            break
    
    if not found:
        for length in range(1, len(target)):
            for guess_tuple in itertools.product(chars, repeat=length):
                attempts += 1
                guess = ''.join(guess_tuple)
                
                if guess == target:
                    elapsed = time.time() - start_time
                    print("\n" + "="*50)
                    print(f"SUCCESS! Password found: '{guess}'")
                    print(f"Total attempts: {attempts:,}")
                    print(f"Time taken: {elapsed:.2f} seconds")
                    print("="*50)
                    found = True
                    break
            if found:
                break
    
    return attempts

def smart_brute_force():
    drake_ascii()
    print("\n" + "="*60)
    print("SMART BRUTE FORCE")
    print("="*60)
    
    print("\nEnter a password to crack:")
    target = input("Password: ").strip()
    
    if not target:
        target = "admin123"
        print(f"Using default: {target}")
    
    chars = string.ascii_lowercase + string.digits
    attempts = 0
    start_time = time.time()
    
    common_patterns = [
        "password", "123456", "12345678", "qwerty", "abc123", 
        "admin", "admin123", "root", "user", "letmein",
        "welcome", "monkey", "dragon", "master", "sunshine"
    ]
    
    print("\n[>] Trying common passwords...")
    for pattern in common_patterns:
        attempts += 1
        if pattern == target:
            elapsed = time.time() - start_time
            print(f"\nSUCCESS! Password found: '{pattern}'")
            print(f"Attempts: {attempts}")
            print(f"Time: {elapsed:.2f} seconds")
            return
    
    print("[>] Trying dictionary words...")
    common_words = ["cat", "dog", "bird", "fish", "tree", "house", "car", "blue", "red", "green"]
    for word in common_words:
        attempts += 1
        if word == target:
            elapsed = time.time() - start_time
            print(f"\nSUCCESS! Password found: '{word}'")
            print(f"Attempts: {attempts}")
            print(f"Time: {elapsed:.2f} seconds")
            return
    
    print(f"[>] Brute forcing length {len(target)}...")
    for guess_tuple in itertools.product(chars, repeat=len(target)):
        attempts += 1
        guess = ''.join(guess_tuple)
        
        if attempts % 50000 == 0:
            elapsed = time.time() - start_time
            print(f"    Attempts: {attempts:,} | Time: {elapsed:.1f}s")
        
        if guess == target:
            elapsed = time.time() - start_time
            print("\n" + "="*50)
            print(f"SUCCESS! Password found: '{guess}'")
            print(f"Total attempts: {attempts:,}")
            print(f"Time taken: {elapsed:.2f} seconds")
            print("="*50)
            break

def crack_chunk(chunk_start, chunk_size, chars, password_length, target, core_id):
    start_idx = chunk_start
    end_idx = chunk_start + chunk_size
    
    current_idx = 0
    for guess_tuple in itertools.product(chars, repeat=password_length):
        if current_idx >= start_idx and current_idx < end_idx:
            guess = ''.join(guess_tuple)
            if guess == target:
                return guess
        current_idx += 1
        if current_idx >= end_idx:
            break
    return None

def ultra_fast_parallel():
    drake_ascii()
    print("\n" + "="*60)
    print("REAL PARALLEL BRUTE FORCE")
    print("="*60)
    
    print("\nEnter a password to crack:")
    target = input("Password: ").strip()
    
    if not target:
        target = "abc123"
        print(f"Using default: {target}")
    
    chars = string.ascii_lowercase + string.digits
    password_length = len(target)
    
    total_combinations = len(chars) ** password_length
    num_cores = multiprocessing.cpu_count()
    chunk_size = total_combinations // num_cores
    
    print(f"\n[*] Target: '{target}' (length: {password_length})")
    print(f"[*] Character set size: {len(chars)}")
    print(f"[*] Total combinations: {total_combinations:,}")
    print(f"[*] Using {num_cores} CPU cores in parallel")
    print(f"[*] Each core testing {chunk_size:,} combinations")
    print("-"*50)
    
    start_time = time.time()
    
    with multiprocessing.Pool(processes=num_cores) as pool:
        chunks = []
        for i in range(num_cores):
            chunk_start = i * chunk_size
            chunks.append((chunk_start, chunk_size, chars, password_length, target, i))
        
        results = pool.starmap(crack_chunk, chunks)
        
        for result in results:
            if result is not None:
                elapsed = time.time() - start_time
                print("\n" + "="*50)
                print(f"SUCCESS! Password found: '{result}'")
                print(f"Time taken: {elapsed:.2f} seconds")
                print(f"Used {num_cores} cores in parallel")
                print("="*50)
                return
    
    elapsed = time.time() - start_time
    print("\n" + "="*50)
    print(f"FAILED! Password not found")
    print(f"Time taken: {elapsed:.2f} seconds")
    print("="*50)

def benchmark():
    drake_ascii()
    print("\n" + "="*60)
    print("SPEED BENCHMARK")
    print("="*60)
    
    test_cases = [
        ("1", "numbers"),
        ("12", "numbers"),
        ("123", "numbers"),
        ("a", "letters"),
        ("ab", "letters"),
        ("abc", "letters"),
    ]
    
    print(f"\n{'Password':<10} {'Length':<8} {'Attempts':<12} {'Time':<10} {'Speed/s':<12}")
    print("-"*60)
    
    for password, ptype in test_cases:
        chars = string.digits if ptype == "numbers" else string.ascii_lowercase
        attempts = 0
        start = time.time()
        
        for guess_tuple in itertools.product(chars, repeat=len(password)):
            attempts += 1
            guess = ''.join(guess_tuple)
            if guess == password:
                break
        
        elapsed = time.time() - start
        print(f"{password:<10} {len(password):<8} {attempts:<12,} {elapsed:<10.4f} {attempts/elapsed:<12,.0f}")

def interactive_menu():
    while True:
        print("\n" + "="*50)
        print("BRUTE FORCE MENU")
        print("By: DrakeDev23")
        print("="*50)
        print("1. Fast crack (direct length search)")
        print("2. Smart crack (common patterns first)")
        print("3. REAL parallel crack (multi-core)")
        print("4. Speed benchmark")
        print("5. Exit")
        print("-"*50)
        
        choice = input("Choose (1-5): ").strip()
        
        if choice == "1":
            fast_brute_force()
        elif choice == "2":
            smart_brute_force()
        elif choice == "3":
            ultra_fast_parallel()
        elif choice == "4":
            benchmark()
        elif choice == "5":
            print("\nGoodbye! Use strong passwords")
            break
        else:
            print("Invalid choice")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    multiprocessing.freeze_support()
    interactive_menu()