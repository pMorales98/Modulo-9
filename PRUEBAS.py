

# Define a function named score
def score():
    global score 
    score = 0
    print(score)

# Call the function score

score()

def promedio(numeros):
    total = sum(numeros)
    promedio = total / len(numeros)
    print(promedio)


promedio(numeros=[1,2,3])