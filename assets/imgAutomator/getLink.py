 # %%
if __name__ == "__main__":
    head = '!['
    middle = '](https://drive.google.com/uc?id='
    tail = ')'
    file = './input.txt'

    names = ['백야', 10, 11, 5,6,7,8,9,1,2,3,4]
    names = list(map(str, names))
    with open(file, 'r') as f:
        links = f.readlines()

    result = dict()
    for name, link in zip(names, links):
        id = link.split('/')[5]
        embedLink = head + name + middle + id + tail
        result[name] = embedLink
    result = dict(sorted(result.items()))

    with open('output.txt', 'w', encoding='UTF-8') as f:
        onlyValues = list(result.values())
        onlyValues.sort()
        for value in onlyValues:
            print(value, file=f)
# %%
