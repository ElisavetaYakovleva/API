def main1(a, m, n, x):
    sum1 = 1
    for i in range(1, a + 1):
        sum2 = 1
        for j in range(1, m + 1):
            sum2 *= (23 * i ** 4 + i + (47 * i - 24 * j ** 2) ** 6)
        sum1 *= sum2
    res1 = 0
    for k in range(1, n + 1):
        res2 = 0
        for c in range(1, m + 1):
            res2 += (60 - c ** 4 - (21 * k ** 2 - x ** 3 - 28 * x))
        res1 += res2
    return sum1 + res1


print('{:.2e}'.format(main1(5, 2, 7, 0.06)))


def main(example):
    res = {}
    example = example.split("new")[1:]
    for i in range(len(example)):
        s = example[i]
        st = s[s.find('"') + 2:s.find('" := ')].strip()
        nums = s[s.find("#") + 1:].split(" ")
        res[st] = []
        for k in nums:
            res[st].append(int(k.strip()))
    return res

print(main('<: new @"beinen_669":=#3690 new @"usleen" := #-2098 new @"inmaa":= #3305 :>'))