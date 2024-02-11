from itertools import permutations
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
    grouped_data = {key: [d[key] for d in data if key in d]
                    for key in keysData}
    return grouped_data


print(convert(data))

print("---")

# funkcja która za dwa argumenty przyjmie dwie listy zagnieżdżone
# oraz zwróci nową listę, która połączy elementy list
# zagnieżdżonych na odpowiadających im pozycjach


def concat(listToConcat, listToConcatSecond):
    result = []
    num = 0
    while len(listToConcat) > num:
        nested_lists = [listToConcat[num], listToConcatSecond[num]]
        mergeList = [item for sublist in nested_lists for item in sublist]
        result.append(mergeList)
        num += 1
    return result


print(concat([[6, 2], [6, 3, 7], [3, 5]], [[3], [4, 2], [0, 5, 1, 5]]))
print(concat([[6, 2, 5, 2], [6, 3, 7]], [[4, 2], [0, 5, 1, 5]]))

print("---")

# funkcja która za argument przyjmie listę zagnieżdżoną
# i posortuje ją rosnąco po każdej wewnętrznej liście.
data = [
    [4, 7, 2, 7, 9, 1],
    [6, 3, 2, 8, 8],
    [9, 7, 3, 2, 7]
]


def sort_by_row(data):
    sortList = [sorted(li)for li in data]
    return sortList


print(sort_by_row([[4, 7, 2, 7, 9, 1], [6, 3, 2, 8, 8], [9, 7, 3, 2, 7]]))
print(sort_by_row([[5, -2, 3, 7, 4], [6, 3]]))

print("---")

# funkcja która za argument przyjmie listę zagnieżdżoną
# I zwróci trzy największe wartości z każdej wewnętrznej listy posortowane malejąco


def top3(data):
    myTop3 = [sorted(li, reverse=True)[:3] for li in data]
    return myTop3


print(top3([[4, 7, 2, 7, 9, 1, 3], [6, 3, 2, 8, 8, 7], [9, 7, 3, 2, 10, 2]]))

print("---")

# funkcja która za argument przyjmie listę zagnieżdżoną,
# I pozostawi tylko te słowniki, w których występuje klucz o nazwie 'level'
user_data = [
    {'user_id': '3546', 'level': 64, 'is_active': True},
    {'user_id': '3467', 'level': 34, 'is_active': False},
    {'user_id': '6673', 'is_active': True},
    {'user_id': '8454', 'level': 1, 'is_active': False},
    {'user_id': '3757', 'level': 63, 'is_active': True},
    {'user_id': '1668', 'is_active': False},
]


def filter_users(user_data):
    resultData = []
    for usKey in user_data:
        if 'level' in usKey:
            resultData.append(usKey)
    return resultData


print(filter_users(user_data))

print("---")

# funkcja ma zwrócić listę wszystkich możliwych permutacji wyrazów przekazanego zdania
textPython = 'python is the best'


def calculate(textPython):
    words = textPython.split()
    permutationList = list(permutations(words))
    mutatedText = [" ".join(permutations) for permutations in permutationList]

    return mutatedText


print(calculate(textPython))

print('---')
# funkcja która przyjmie dwie listy i zwróci listę będąca maskę logiczną - przyjmującą 1,
# gdy te listy mają tą samą wartość na odpowiadających pozycjach, przeciwnie 0.

listOne = [4, 5, 7, 2, 8, 10]
listTwo = [3, 5, 4, 2, 8, 12]


def create_mask(firstList, secondList):
    finalResult = []
    num = 0
    while len(secondList) > num:
        if firstList[num] == secondList[num]:
            finalResult.append(1)
        else:
            finalResult.append(0)
        num += 1
    return finalResult


print(create_mask(listOne, listTwo))
print(create_mask([2, 4, 1], [2, 3, 1]))

print('---')

# funkcja która przyjmie za argument listę i dokona następującego przekształcenia:
# wszystkie liczby nieparzyste mnoży przez 2
# [IN]: calculate([4, 5, 6, 7])
# [OUT]: [4, 10, 6, 14]
listToChange = [4, 5, 6, 7]


def calculate(listToMultiply):
    result = []
    for num in listToMultiply:
        if num % 2 == 1:
            result.append(num * 2)
        else:
            result.append(num)
    return result


print(calculate(listToChange))
print(calculate([9, 6, 3, 7, 11, 31, 40]))

print('---')
# funkcja która przyjmie za argument listę tupli o podanej strukturze
# I posortuje listę po drugim elemencie tupli.


def sort_tuple(listUser):
    listUserSort = sorted([user for user in listUser], key=lambda x: x[1])
    return listUserSort


print(sort_tuple([('mike', 34), ('bob', 41), ('john', 36), ('leo', 28)]))
print(sort_tuple([('mike', 'music'), ('bob', 'art'),
      ('john', 'math'), ('leo', 'english')]))

print('---')

# funkcja która przyjmie za argument listę liczb i każdą ujemną liczbę zastąpi 0


def replace_neg(listToReplace):
    listResult = []
    for i in listToReplace:
        if 0 > i:
            listResult.append(0)
        else:
            listResult.append(i)
    return listResult


print(replace_neg([4, -5, 2, 0, -4]))
print(replace_neg([-10, -5, 8, -3, 7, -2]))

# funkcja która przyjmie za argument listę i zwróci liczbę
# liczb dodatnich oraz ujemnych (zero uznajemy za liczbę dodatnią) w podanej liście


def count(myList):
    numbPositive = []
    numbNegative = []

    for li in myList:
        if li >= 0:
            numbPositive.append(li)
        else:
            numbNegative.append(li)
    return (len(numbPositive), len(numbNegative))


print(count([4, 5, 6]))
print(count([5, 2, -1, -5, -2]))

print("---")

# funkcja która przyjmie za argument ciąg znaków i przekształci ten ciąg znaków na liczbę całkowitą


def preprocess(strNumber):
    return int(strNumber[2:].replace(",", ""))


print(preprocess('$ 975,400'))
print(preprocess('$ 158,400,800'))

print("---")

# funkcja która przyjmie za argument listę słów i zwróci ciąg hashtagów utworzonych z tych słów


def make_hashtags(hashWord):
    return "#" + " #".join(hashWord)


print(make_hashtags(['gym', 'sport', 'fit']))
print(make_hashtags(['python', 'code', 'udemy', 'course']))

print("---")

# funkcja która przyjmie za argument tekst w języku angielskim i zamieni wszystkie cyfry (nie liczby) w tekście na zapis słowny
# Tylko liczby 2, 3


def convert(textConvert):
    for li in textConvert:
        if li == "2":
            textConvert = textConvert.replace("2", "two", 1)
        elif li == "3":
            textConvert = textConvert.replace("3", "three", 1)
    return textConvert


print(convert('you need to have 2 tickets'))
print(convert('3 tickets cost 15 euro'))

print("---")

# funkcja która będzie konwertować ciąg znaków zapisany jako snake_case na PascalCase


def convert(convertStr):
    parts = convertStr.split("_")
    return "".join(word.capitalize() for word in parts)


print(convert('some_important_function'))
print(convert('calculate_summary'))

print("---")

# funkcja która będzie konwertować ciąg znaków zapisany jako snake_case na camelCase (patrz poniżej):


def convertCamelCase(convertCamel):
    items = convertCamel.split("_")
    return items[0] + "".join(word.capitalize() for word in items[1:])


print(convertCamelCase('some_important_function'))
print(convertCamelCase('calculate_summary'))

print("---")
# funkcja która będzie przyjmować listę - strumień nazw plików i pozostawi tylko te nazwy plików, które kończą się na '.png'


def preprocess(checkList):
    onlyPng = []
    for png in checkList:
        if png.endswith(".png"):
            onlyPng.append(png)

    return onlyPng


print(preprocess(['img546.png', 'img243.png', 'img247.txt', 'img2456.pdf']))

# funkcja która za argument będzie przyjmować listę krotek (tupli) i usunie z tej listy wszystkie jednoelementowe krotki (tuple).


def preprocess_tuple(tupleList):
    resultTuple = []
    for li in tupleList:
        if len(li) > 1:
            resultTuple.append(li)

    return resultTuple


print(preprocess_tuple([(4, 5), (4, ), (5, 2), (5, 3, 2), (5, )]))

print("---")

# funkcja która za argument będzie przyjmować listę krotek (tupli) i
# usunie z tej listy wszystkie krotki zawierające tylko wartości None
# usuwam (None, None) lub (None,)


def preprocessNone(listNone):
    listResult = []
    for li in listNone:
        if li[0] or li[-1]:
            listResult.append(li)
    return listResult


print(preprocessNone([(4, 5), (4,), (5, None), (5, 3, 2), (None,)]))
print(preprocessNone([(5, None), (None,), (3, None, None), (None, None)]))

print("---")

# funkcja która za argument będzie przyjmować zagnieżdżoną listę lub krotkę i zwracać jej wypłaszczoną formę


def flatten(*listNumber):
    listNumberFlattened = []
    for li in listNumber:
        listNumberFlattened.extend(li)
    return listNumberFlattened


print(flatten([5], [6], [2], [3]))
print(flatten([5], [6], [2, 4, 2], [3, 4]))

print("---")

# Funkcja ma przetworzyć podaną krotkę i zwrócić jeden ciąg będący ciągiem hashtagów utworzonych z podanych słów


def flatten(listWithoutHash):
    listHash = []
    for li in listWithoutHash:
        if li:
            str_hash = " #".join(li)
            listHash.append('#' + str_hash)
    return (" ").join(listHash)


print(flatten((['apple'], ['gym', 'fit'], ['movie', 'netflix'])))
print(flatten((['orange'], [], ['movie', 'netflix'])))

print("---")

# funkcja która za argument będzie przyjmować słowniki powyższej postaci i zwracać poniższe statystki:
# temperaturę minimalną
# temperaturę maksymalną
# temperaturę średnią - wynik zaokrąglij do dwóch miejsc po przecinku

data = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}


def calculate(data):
    minTemp = min(data['temp'])
    maxTemp = max(data['temp'])
    avgTemp = sum(data['temp']) / len(data['temp'])
    avgTempRound = f'{avgTemp:.2f}'
    return (minTemp, maxTemp, avgTempRound)


print(calculate(data))

print("---")

# funkcję o nazwie convert(), która za argument będzie przyjmować słowniki
# powyższej postaci i konwertować je na listy zagnieżdżone o poniższej postaci


def convert(data):
    keyData = []
    for myKey in data.keys():
        keyData.append(myKey)

    dataDevice = [keyData[0], data['device_id']]
    dataTemp = [keyData[1], data['temp']]
    dataCity = [keyData[2], data['city']]
    dataCountry = [keyData[3], data['country']]
    return [dataDevice, dataTemp, dataCity, dataCountry]


print(convert(data))

print("---")

# funkcja która za argument będzie przyjmować słowniki powyższej postaci i zwracać dane dotyczące temperatury w formacie CSV:
# Taki format: 'temp,23.5,22.0,23.1,25.5,24.1'
dataCsv = {
    'device_id': '3057304985',
    'temp': [23.5, 22.0, 23.1, 25.5, 24.1],
    'city': 'Warsaw',
    'country': 'Poland'
}


def to_csv(dataCsv):
    myData = dataCsv['temp']
    allData = 'temp,' + ",".join(map(str, myData))
    return f"""'{allData}'"""


print(to_csv(dataCsv))

print("---")

# funkcja która za argument będzie przyjmować ciąg znaków - wyrazów i zwracać akronim podanego ciągu wyrazów


def acronym(strText):
    words = strText.split()
    acr = "".join(word[0].upper() for word in words)
    return acr


print(acronym('object oriented programming'))
print(acronym('Python Software Foundation'))

print("---")

# podziel podany ciąg znaków na mniejsze kawałki o długości num.


def get_chunks(text, num):
    chunks = []
    while len(text) > 0:
        if len(text) >= num:
            new_chunk = text[:num]
            chunks.append(new_chunk)
            text = text[num:]
        else:
            chunks.append(text)
            text = ''
    return chunks


print(get_chunks('python programming', 3))
print(get_chunks('object oriented programming', 5))

print("---")

# funkcja która sprawdzi, czy dany obiekt jest iterowalny (iterable)
def is_iterable (obj):
    try:
        iter(obj)
        return True
    except:
        return False

print(is_iterable([4, 5]))
print(is_iterable('python'))
print(is_iterable(3.14))

print("---")

# funkcja  która przyjmie dwa argumenty:
# heading - tytuł artykułu w serwisie internetowym
# length - liczba znaków pozostałych po skróceniu tytułu artykułu, domyślnie 30 znaków
# I zwróci skróconą formę tytułu artykułu do 30 znaków, łącznie z trzema kropkami na końcu ...

def truncate(heading , length=30):
    if len(heading) > length:
        newText = "'" + heading[:27] + '...' + "'"
        return newText
    else:
        return "'" + heading + "'"

print(truncate('Python is a programming language that lets you work quickly.'))
print(truncate('Python programming.'))

print("---")

"""
Załóżmy, że implementujesz pewien proces ETL. 
Jako dane wejściowe otrzymujesz pliki CSV o następującej strukturze:
open,high,low,close
45.3,46.1,45.3,45.4
45.4,46.5,45.0,45.4
Funkcja która będzie przyjmować jeden argument:
row - jeden wiersz danych z pliku CSV o powyższej postaci (pomijając wiersz z nazwami kolumn)
"""
def transform(row):
    listETL = row.split(",")
    nameETL = ['open', 'high', 'low', 'close']
    allETL = dict(zip(nameETL, listETL))
    sorted_ETL = dict(sorted(allETL.items()))
    return sorted_ETL

print(transform('45.3,46.1,45.3,45.4'))

print("---")

# funkcja która zwróci maksimum z dwóch liczb. Użyj instrukcji warunkowej.
def maximum (a, b):
    if a > b:
        return a
    else:
        return b
    
print(maximum(4, 2))
print((maximum(-4, 2)))

print("---")
# funkcja która zwróci maksimum z trzech liczb. Użyj instrukcji warunkowej.
def maksimumThree (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c
    
print(maksimumThree(4, 2, 1))
print(maksimumThree(-3, 2, 5))

print("---")

# funkcja która jako parametr przyjmie obiekt iterowalny (lista, tupla) oraz zwróci iloczyn wszystkich elementów listy.
def multi(multiList):
    num = 1
    for ml in multiList:
        num *= ml
    return num

print(multi((-4, 6, 2)))
print(multi([4, 2, -5]))

print("---")
# funkcja która przyjmie listę słów i zwróci długość najdłuższego słowa.
def map_longest(listLongest):
    theLongest = []
    for txt in listLongest:
        theLongest.append(len(txt))
    return sorted(theLongest, reverse=True)[0]


print(map_longest(['python', 'sql']))
print(map_longest(['java', 'sql', 'r']))

print("---")