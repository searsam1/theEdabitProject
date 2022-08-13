class StackCalc:

  def __init__(self):
    self.stack = [0]
    self.d = {
      
    } 
  def run(self, instructions):
      
    instruction_set = instructions.split()
    
    for i in instruction_set:
      
      if i.isnumeric():
        self.stack.append(int(i))
      
      elif i == "POP":
        self.stack.pop()
      
      elif i == "DUP":
        self.stack.append(self.stack[-1])
      
      elif i == "+":
        x1, x2 = self.stack.pop(), self.stack.pop()
        self.stack.append(x1 + x2)
      
      elif i == "-":
        x1, x2 = self.stack.pop(), self.stack.pop()
        self.stack.append(abs(x1 - x2))
      
      elif i == "*":
        x1, x2 = self.stack.pop(), self.stack.pop()
        self.stack.append(x1 * x2)  
      
      elif i == "/":
        x1, x2 = self.stack.pop(), self.stack.pop()
        mx, mn = max([x1,x2]), min([x1,x2])
        self.stack.append(int(mx / mn))
      else:
        self.stack.append("Invalid instruction: {}".format(i))
        break
        
        
  def getValue(self):
    answer = self.stack[-1]
    self.stack.clear()
    return answer
    
    