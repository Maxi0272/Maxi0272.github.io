def solutionA(lines):
  cal= 0
  new_cal = 0
  for line in lines:
    if not line:
      cal = 0
    else:
      cal += int(line)

      if cal > new_cal:
        new_cal = cal
  return new_cal


def solutionB(lines):
  cal= 0
  totalcal= 0
  new_cal = 0
  new_cal1 = 0
  new_cal2= 0
  for line in lines:
    if not line:
      cal = 0
    else:
      cal += int(line)

    if cal > new_cal:
      new_cal2 = new_cal1
      new_cal1= new_cal
      new_cal = cal
    elif cal > new_cal1:
      new_cal2 = new_cal1
      new_cal1 = cal
    elif cal > new_cal2:
      new_cal2 = cal
  totalcal = new_cal2 + new_cal1 + new_cal
  return totalcal

  return -2 # Dummy result, deliberately wrong


# Helper function for loading the problem data
def load_data(fileName):
  with open(fileName, "r") as input_data:
    lines = input_data.readlines()
  for i in range(len(lines)):
    lines[i] = lines[i].strip()
  return lines


if __name__ == "__main__":
  input_file_name = "dummy-input.txt"
  # TODO: Uncomment line below to use real input
  input_file_name = "input.txt" 
  
  print("Loading data")
  lines = load_data(input_file_name)
  
  resultA = solutionA(lines)
  print(f"Solution for part A: {resultA}")

  resultB = solutionB(lines)
  print(f"Solution for part B: {resultB}")