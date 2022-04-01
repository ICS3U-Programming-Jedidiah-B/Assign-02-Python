#!/usr/bin/env python3
# Created by: Jedidiah
# Created on: Mar. 31, 2022
# This program asks the user for the length
# width and height to calculate surface area
# and volume of a rectanglar prism a rating
# system


def main():
    # input
    print("This program will calculate the surface area")
    print("and volume of a rectanglar prisim")
    print("")
    print("please enter the length below")
    length = float(input("Enter the length (cm): "))
    print("")
    print("please enter the width  below")
    width = float(input("Enter the width (cm): "))
    print("")
    print("please enter the height below")
    height = float(input("Enter the height (cm): "))
    print("")

    # process
    volume = width * height * length
    surface_area = (width * length + height * length + height * width) * 2
    # output
    print("")
    print("Volume = {:.2f} cm".format(volume))
    print("Surface Area = {:.2f} cm".format(surface_area))
    print("")

    # rating system
    rating = int(input("Rate this program from 1 to 10 :"))
    if rating > 7:
        print("")
        print("thank you for the high rating!")
    else:
        print("")
        print("thank you using the program anyway!")


if __name__ == "__main__":
    main()
