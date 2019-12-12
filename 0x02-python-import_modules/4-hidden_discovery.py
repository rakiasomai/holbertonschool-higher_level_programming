#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    direct = dir(hidden_4)
    avoid = "__"
    for i in range(0, len(direct)):
        if avoid not in direct[i]:
            print(direct[i])
