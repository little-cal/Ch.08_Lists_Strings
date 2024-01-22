import random
import math


def volume_sphere(radius):
    pie = math.pi
    volume = 4/3*pie*radius**3
    return volume


# user_radius = int(input("Give me a radius: "))
# vol = volume_sphere(user_radius)
# print(f"The volume is {vol:.2f}")


def main():
    print(volume_sphere(6))


if __name__ == "__main__":
    main()
