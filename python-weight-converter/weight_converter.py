user_weight = input("Enter your weight:")
unit = input("l(bs) or K(g):")


if "l" == unit:
    converted_weight = int(user_weight) * 0.45
    print(f"{converted_weight} k(g)")
elif "k" == unit:
    converted_weight = int(user_weight) / 0.45
    print(f"{converted_weight} l(bs)")