import itertools

def binary_search(arr, target):
  low = 0
  high = len(arr) - 1

  while low <= high:
    mid = (low + high) // 2
    if arr[mid] == target:
      return mid
    elif arr[mid] < target:
      low = mid + 1
    else:
      high = mid - 1

  return -1

def main():    
    els = str(input("enter all fragments separated by spaces:")).lower().split()

    with open(r'words_alpha.txt', 'r') as fp:
        # read all lines using readline()
        words = fp.read().splitlines()

    matches = 0
    for i in range(1,5):
        sub_matches = 0
        print(f"{i} " + "_"*i)
        permutations = list(itertools.permutations(els, i))
        for perm in permutations:
            word = "".join(perm)
            if word == "frivolousness":
               pass
            if binary_search(words, word) != -1:
                sub_matches = sub_matches + 1
                matches = matches + 1
                print(f"{sub_matches}: {word}")

    print(matches)

main()
