def weight_on_planets():
    e_weight = float(input("What do you weigh on earth? "))
    print("" + "\n" +
          "On Mars you would weigh %1.2f pounds." % (e_weight * 0.38) + "\n" +
          "On Jupiter you would weigh %1.2f pounds." % (e_weight * 2.34))


if __name__ == '__main__':
    weight_on_planets()
