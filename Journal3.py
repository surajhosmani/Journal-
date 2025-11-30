import sys

def main():
    try:
        print("Enter scores separated by spaces:")
        user_input = sys.stdin.readline().strip()

        if not user_input:
            print("No input given. Please enter numbers.")
            return

        scores = list(map(float, user_input.split()))
        
        total = sum(scores)
        average = total / len(scores)
        maximum = max(scores)
        minimum = min(scores)

        print(f"Sum of scores: {total}")
        print(f"Average of scores: {average}")
        print(f"Maximum score: {maximum}")
        print(f"Minimum score: {minimum}")

    except ValueError:
        print("Invalid input! Please enter numeric values only.")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
