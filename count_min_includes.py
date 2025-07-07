import os
import re

def print_linux_includes_per_c_file(directory):
    # Matches lines like: #include <linux/something.h>
    include_pattern = re.compile(r'^\s*#\s*include\s*<linux/[^>]+>')

    for root, _, files in os.walk(directory):
        for filename in files:
            if filename.endswith('.c'):
                filepath = os.path.join(root, filename)
                count = 0
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        for line in f:
                            if include_pattern.match(line):
                                count += 1
                except Exception as e:
                    print(f"Error reading {filepath}: {e}")
                if count > 0:
                    print(f"{count}\t{filepath}")

# Example usage:
if __name__ == "__main__":
    directory = "/workspaces/rust-for-linux/rpi-linux/drivers/iio"  # Change to your directory
    print_linux_includes_per_c_file(directory)