
s = "hello"

def main():
    print mix_up("hello", "world")

def fix_start(s):
  store = []
  result = []
  for index in range(len(s)):
    if s[index] in store:
      result.append("*")
    else:
      result.append(s[index])
      store.append(s[index])

  return result

def mix_up(a, b):
  pre_a = a[0] + a[1]
  pre_b = b[0] + b[1]

  after_a = a[2:len(a)]
  after_b = b[2:len(b)]

  return pre_b + after_a + " " + pre_a + after_b

if __name__ == "__main__":
    s = ["a", "b"]
    print "".join(s)

