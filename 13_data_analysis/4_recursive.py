def generate_strings(n):
    if n == 0:
        return [""]
    else:
        smaller_strings = generate_strings(n - 1)
        result = []
        for s in smaller_strings:
            result.append(s + "0")
            result.append(s + "1")
        return result


if __name__ == "__main__":
    n = 3
    strings = generate_strings(n)
    print(strings)
