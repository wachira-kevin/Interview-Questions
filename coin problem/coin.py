

def solution(N, K):
    numbers = [int(i) for i in str(N)]

    for index in range(len(numbers)):
        if numbers[index] < 9 and K != 0:
            if (K + numbers[index]) > 9:
                K -= (9 - numbers[index])
                numbers[index] = 9
            else:
                numbers[index] += K
                K = 0
        print(K)
    return numbers


def jp(people):
    counter = 0
    for person in people:
        counter += 1
        if counter <= 2:
            if person["pet"] == "Dog":
                print("{} has a dog! Had to check {} of records to find a dog owner".format(person["name"], counter))
                break
        else:
            break




if __name__ == "__main__":
    jp([
    {'name': "Daniel", 'age': 29, 'job': "Engineer", 'pet': "Cat", 'pet_name': "Gato"},
    {'name': "Katie", 'age': 30, 'job': "Teacher", 'pet': "Dog", 'pet_name': "Frank"},
    {'name': "Owen", 'age': 26, 'job': "Sales person", 'pet': "Cat", 'pet_name': "Cosmo"},
    {'name': "Josh", 'age': 22, 'job': "Student", 'pet': "Cat", 'pet_name': "Chat"},
    {'name': "Estelle", 'age': 35, 'job': "French Diplomat", 'pet': "Dog", 'pet_name': "Gabby"},
    {'name': "Gustav", 'age': 24, 'job': "Brewer", 'pet': "Dog", 'pet_name': "Helen"}
])