import os
import re
from collections import Counter

def count_includes(directory):
    include_pattern = re.compile(r'^\s*#\s*include\s*[<"]([^">]+)[">]')
    include_counter = Counter()

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.c'):
                filepath = os.path.join(root, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            match = include_pattern.match(line)
                            if match:
                                include = match.group(1)
                                include_counter[include] += 1
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")

    return dict(include_counter)

# Example usage:
if __name__ == "__main__":
    directory = "/workspaces/rust-for-linux/rpi-linux/drivers/iio"  # Change to your directory
    includes_count = count_includes(directory)
    for include, count in includes_count.items():
        print(f"{count} {include}")