# return few values from function
# 1. Solution 1

class Test:
  def __init__(self):
    self.value_1 = "This is test"
    self.value_2 = 32
    self.value_3 = 3434.422
    
def get_values():
  return Test()

results = get_values()

print(f"output: {results.value_1}, {results.value_2}, {results.value_3}")