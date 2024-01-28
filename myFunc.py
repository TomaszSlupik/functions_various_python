import sys
print(sys.version[:7])
print('---')

# funkcja która sprawdzi czy przekazana lista jest zagnieżdżona
# i składa się z elementów typu list (lista składająca się z list).


def is_nested(myList):
    for checkList in myList:
        if not isinstance(checkList, list):
            return False
    return True


print(is_nested([[3, 4]]))
print(is_nested([[3, 4], 4]))
print(is_nested([[3, 4], [2, 1]]))
print(is_nested([[3, 4], 0, [2, 1]]))

print('---')

# funkcja która sprawdzi czy przekazana lista składa się z tych samych elementów.


def is_all_equal(myList):
    if len(myList) == 3 and myList[0] == myList[1] == myList[2]:
        return True
    return False


print(is_all_equal([4, 5, 7]))
print(is_all_equal([4, 4, 4]))
print(is_all_equal(['Q', 'Q', 'Q']))
print(is_all_equal(['Q', 'Q', 'DQ']))

print("---")

# funkcja która za argument przyjmie listę i zamieni pierwszy i ostatni element tej listy.


def swap_elements(reverseList):
    myNewList = []
    myNewList.append(reverseList[-1])
    myNewList.append(reverseList[1:-1])
    myNewList.append(reverseList[0])
    flatList = [item for sublist in myNewList for item in (
        sublist if isinstance(sublist, list) else [sublist])]
    return flatList


print(swap_elements([4, 5, 6, 7]))
print(swap_elements([4, 5, 6, 7, 1]))
print(swap_elements([4, 5]))

print("---")

# funkcję o nazwie, która za argument przyjmie listę oraz dwa indeksy i zamieni elementy na wskazanych indeksach.


def swap_index(indexList, searchIndex, finalIndex):

    firstItem = indexList[searchIndex]
    secondItem = indexList[finalIndex]

    indexList.insert(finalIndex, firstItem)
    indexList.pop(finalIndex + 1)
    indexList.insert(searchIndex, secondItem)
    indexList.pop(searchIndex + 1)

    return indexList


print(swap_index([4, 5, 6, 7, 1], 1, 2))
print(swap_index(['A', 'B', 'C', 'D', 'E'], 4, 2))
print(swap_index([2.1, 5.2, 6.2, 7.1, 2.6, 2.1], 3, 2))

print("---")

# funkcja która za argument przyjmie tekst i odwróci kolejność słów w podanym tekście.
# Dla uproszczenia zakładamy, że tekst nie zawiera żadnych znaków interpunkcyjnych.


def reverse_words(reverseText):
    myText = reverseText.split()
    myText.reverse()
    result = " ".join(myText)
    return result


print(reverse_words('python is the best'))
print(reverse_words('you should learn python language'))

print("---")

# funkcja która za argument przyjmie dwie listy, usunie ich wspólne elementy i zwróci te listy.
# Przykład:
# [IN]: ([4, 3, 5, 2], [3, 8])
# [OUT]: ([4, 5, 2], [8])


def remove_common_elements(l1, l2):
    for i in l1[:]:
        if i in l2:
            l1.remove(i)
            l2.remove(i)
    return (l1, l2)


print(remove_common_elements([4, 3, 5, 2], [3, 8]))
print(remove_common_elements([4, 3, 5, 2], [1, 8]))
print(remove_common_elements([4, 3, 5, 2], [1, 3, 5, 8]))

print("---")

# funkcja która za argument przyjmie listę oraz szukany element
# i zwróci listę wszystkich indeksów na których znajduje się szukany element.
# Jeśli element nie występuje w liście funkcja zwraca pustą listę.


def get_indices(mylist, searchIndex):
    try:
        indices = [index for index, item in enumerate(
            mylist) if item == searchIndex]
        return indices
    except:
        return []


print(get_indices([4, 3, 5, 2], 2))
print(get_indices(['Q', 'DQ', 'DQ', 'DQ', 'Q', 'Q'], 'Q'))

print("---")

# która za argument przyjmie listę oraz zwróci listę wszystkich
# indeksów na których znajduje się element typu str.
# Jeśli lista nie posiada żadnych elementów typu str funkcja ma zwrócić pustą listę.


def get_indices_str(myList):
    indices = [index for index, item in enumerate(myList) if type(item) == str]
    return indices


print(get_indices_str(
    ['https://www.e-smartdata.org', 'response', 202, 'code']))
print(get_indices_str(['Q', 34, 'DQ', True]))
print(get_indices_str([4, 3, 5, 2]))

print("---")

# Pogrupowanie wartości do kluczy 
data = [
    {'user': 'joe', 'main_technology': 'python'},
    {'user': 'tom', 'main_technology': 'c/cpp'},
    {'user': 'michael', 'main_technology': 'cloud'},
    {'user': 'bob', 'main_technology': 'php'},
    {'user': 'lil', 'main_technology': 'html'},
    {'user': 'alice', 'main_technology': 'sql'},
]

def convert(data):
    keysData = set(keys for d in data for keys in d.keys())
    grouped_data = {key: [d[key] for d in data if key in d] for key in keysData}
    return grouped_data

print(convert(data))

print("---")

# do poprawienie 
def concat(listToConcat, listToConcatSecond):
    num = 0
    while len(listToConcat) > num:
        nested_lists = [listToConcat[num], listToConcatSecond[num]]
        mergeList = [item for sublist in nested_lists for item in sublist]
        num += 1
    return mergeList

print(concat([[6, 2], [6, 3, 7], [3, 5]], [[3], [4, 2], [0, 5, 1, 5]]))
