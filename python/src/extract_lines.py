import sys
from pprint import pprint

def main():
  pass
def extract_specific_lines(file_path):
  with open(file_path, 'r',  encoding="utf8") as file:
    lines = file.readlines()
  # Extract lines containing "Error:"
  error_lines = lines[lines.index('Starting audit...\n') + 1: lines.index('Audit done.\n')]
  error_lines = [line.replace("[Error]", "").strip() for line in error_lines]
  return error_lines

if __name__ == '__main__':
  if len(sys.argv) != 2:
    print("Usage: python extract_lines.py <file_path>")
    sys.exit(1)

  file_path = sys.argv[1]
  error_lines = extract_specific_lines(file_path)

  for line in error_lines:
    print(line)