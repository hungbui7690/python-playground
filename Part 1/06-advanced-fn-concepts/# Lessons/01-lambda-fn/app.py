# lambda functions: single line functions
'''
Normal
  def add(x, y):
    return 10 + x + y

Lambda
  add_stuff = lambda x, y: 10 + x + y


////////////////////////////
Normal
  def is_high_score(score):
    return score >= 90
  high_scores = filter(is_high_score, scores)

Lambda
  high_scores = filter(lambda score: score >= 90, scores)
'''


def main():
    # example 1: function with 2 parameters x and y -> return "10 + x + y"

    # def add(x, y):
    #     return 10 + x + y

    add_stuff = lambda x, y: 10 + x + y
    result = add_stuff(5, 7)
    print(result)

    # example 2: with built in HO function -> filter

    scores = [20, 95, 45, 85, 90, 15, 55, 100, 10]

    # def is_high_score(score):
    #     return score >= 90
    # high_scores = filter(is_high_score, scores) # filter(cb, list)

    high_scores = filter(lambda score: score >= 90, scores)
    print(high_scores)
    print(list(high_scores))


if __name__ == "__main__":
    main()
