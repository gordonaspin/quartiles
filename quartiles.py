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
        dictionary_words = fp.read().splitlines()

    matches = 0
    for i in range(1,5):
        words = []
        permutations = list(itertools.permutations(els, i))
        for perm in permutations:
            word = "".join(perm)
            if binary_search(dictionary_words, word) != -1:
                words.append(word)
                #print(f"{sub_matches}: {word}")
        words.sort()
        matches = matches + print_words(i, matches, words)

def print_words(i, matches, wordlist):
    print(f"{i} " + "_"*i)
    for word in wordlist:
        matches = matches + 1
        print(f"{matches}: {word}")
    return len(wordlist)

main()
