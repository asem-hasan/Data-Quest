import sys

if __name__ == "__main__":
    print("=== Player Score Analytics ===")
    num = []
    i = 1
    while i < len(sys.argv):
        try:
            score = int(sys.argv[i])
            num.append(score)
        except ValueError:
            print(f"Invalid parameter: ’{sys.argv[i]}’")
        i += 1
    if len(num) == 0:
        print(f"No scores provided. Usage: python3 {sys.argv[0]} ", end="")
        print("<score1> <score2> ...")
    else:
        print(f"Scores processed: {num}")
        print(f"Total players: {len(num)}")
        print(f"Total scores: {sum(num)}")
        print(f"Average score: {sum(num) / len(num):.2f}")
        print(f"Highe score: {max(num)}")
        print(f"Lowe score: {min(num)}")
        print(f"Score range: {max(num) - min(num)}")
