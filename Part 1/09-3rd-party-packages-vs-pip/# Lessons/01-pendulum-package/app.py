'''
  Pip vs Pypi
  - pip --version
  - https://pypi.org/project/pendulum/


************************

  Install Pendulum Package
  - rust: https://www.rust-lang.org/tools/install
    -> since this package requires rust
    -> cargo --version
  - pip install pendulum
    -> install globally
    -> version conflicts
    -> bloats global namespace


************************

  - https://pypi.org/project/pendulum/
  - format date & time


'''

import pendulum


def main():
    pdt = pendulum.now() # pdt = pendulum datetime
    print(pdt)

    # formatting with pendulum
    print(pdt.format('DD/MM/YYYY'))
    print(pdt.format('H:m A'))
    print(pdt.to_day_datetime_string())

    # other pendulum methods
    pdt2 = pdt.add(days=1, months=2, years=3)
    print("add: ",pdt2.to_day_datetime_string())

    pdt3 = pdt.subtract(years=4, weeks=1)
    print("subtract: ", pdt3.to_day_datetime_string())

    pdt4 = pdt.set(year=1986, month=4)
    print(pdt4.to_day_datetime_string())

if __name__ == "__main__":
    main()
