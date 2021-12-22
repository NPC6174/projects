#
# Example file for wotking with conditional statements
#

def main():
    x, y = 100, 100

    # conditional flow uses if, elif, else
    if x < y:
        result = "x is less than y"
    elif x == y:
        result = "x is the same as y"
    else:
        result = "x is greater than y"
    print(result)

    # conditional statemnts let you use "a if C else b"
    result = "x is less than y" if x < y else "x is greater or equal to y"
    print(result)

    # match-case makes it easy to compare multiple values and replaces if, elif, else statements, only works in Py3.10 or later
    value = "one"
    match value:
        case "one":
            result = 1
        case "two":
            result = 2
        case "three" | "four":
            result = (3,4)
        case _:
            result = -1
    print(result)

if __name__ == "__main__":
    main()

