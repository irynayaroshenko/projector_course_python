"""
You have 100 cats.
One day you decide to arrange all your cats in a giant circle. Initially, none of your cats have any hats on.
You walk around the circle 100 times, always starting at the same spot, with the first cat (cat # 1).
Every time you stop at a cat, you either put a hat on it if it doesn’t have one on, or you take its hat off if it has one on.

The first round, you stop at every cat, placing a hat on each one.
The second round, you only stop at every second cat (#2, #4, #6, #8, etc.).
The third round, you only stop at every third cat(#3, #6, #9, #12, etc.).
You continue this process until you’ve made 100 rounds around the cats (e.g., you only visit the 100th cat).
Write a program that simply outputs which cats have hats at the end.

Optional: Make function that can calculate hat with any amount of rounds and cats.

Here you should write an algorithm, after that, try to make pseudocode. Only after that start to work.
Code is simple here, but you might struggle with algorithm. Therefore, don`t try to write a code from the first attempt.
"""
import time

# Solution 1. With list. Function with optional parameter in the task
def cats_and_hats(cats_num: int, rounds: int):
    cats = [False for _ in range(cats_num)]

    for i in range(rounds):
        for j, value in enumerate(cats):
            if (j + 1) % (i + 1) == 0:
                if not cats[j]:
                    cats[j] = True
                else:
                    cats[j] = False
    # for cat in range(len(cats)):
    #     if cats[cat]:  # if in hat (if True)
    #         cats_fin.append(cat+1)
    cats_fin = [cat + 1 for cat in range(len(cats)) if cats[cat]]
    print(cats_fin)
    return cats_fin

start1 = time.perf_counter()
start2 = time.time()

cats_and_hats(100, 100)

end1 = time.perf_counter()
end2 = time.time()
ms = (end1-start1) * 10**6
print(f"Elapsed {ms:.03f} micro sec.")
print("Execution time:", end2 - start2, "sec")

#####  Solution 2. With dict  #####
start3 = time.perf_counter()
start4 = time.time()


def cats_hats():
    d = {}.fromkeys(range(1, 100), 0)
    list_of_cats = []
    final_cats_in_hats = []

    for i in range(1, 101):
        list_of_cats.extend(j for j in range(0, 101, i))  # add each 2nd through one iteration, each 3rd, 4th and so on

    for c in list_of_cats:
        if c != 0:
            d[c] = list_of_cats.count(c)  # I got 0 in list which I don't need. Here omit all 0 and count cats interact

    for key, value in d.items():
        if value % 2:
            final_cats_in_hats.append(key)  # leave only cats in hats after 100th iteration
    print(final_cats_in_hats)
    return final_cats_in_hats


cats_hats()

end3 = time.perf_counter()
end4 = time.time()
ms = (end3-start3) * 10**6
print(f"Elapsed {ms:.03f} micro secs.")
print("Execution time:", end4 - start4, "sec")
