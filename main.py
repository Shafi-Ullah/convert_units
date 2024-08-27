import operator

SI_unit_to_int = {}
SI_unit_prefix = {
    "exa": {"int": 18, "power": 10**18},
    "peta": {"int": 17, "power": 10**15},
    "tera": {"int": 16, "power": 10**12},
    "giga": {"int": 15, "power": 10**9},
    "mega": {"int": 14, "power": 10**6},
    "kilo": {"int": 13, "power": 10**3},
    "hecto": {"int": 12, "power": 10**2},
    "deca": {"int": 11, "power": 10**1},
    "meter": {"int": 10, "power": 10**0},
    "deci": {"int": 9, "power": 10**-1},
    "centi": {"int": 8, "power": 10**-2},
    "milli": {"int": 7, "power": 10**-3},
    "micro": {"int": 6, "power": 10**-6},
    "nano": {"int": 5, "power": 10**-9},
    "angstrom": {"int": 4, "power": 10**-10},
    "pico": {"int": 3, "power": 10**-12},
    "femto": {"int": 2, "power": 10**-15},
    "atto": {"int": 1, "power": 10**-18},
}
time_to_int = {
    "eon": 16,
    "galactic year": 15,
    "millennium": 14,
    "century": 13,
    "decade": 12,
    "year": 11,
    "lunar year": 10,
    "month": 9,
    "lunar month": 8,
    "fortnight": 7,
    "week": 6,
    "day": 5,
    "hour": 4,
    "minute": 3,
    "shake": 2,
    "planck time": 1,
}
FPS_distance_int = {
    "nautical mile": 7,
    "mile": 6,
    "furlong": 5,
    "rod": 4,
    "pole": 4,
    "yard": 3,
    "foot": 2,
    "inch": 1,
}

weight_to_int = {
    # "metric ton": 12,
    "tonne": 12,
    "ton": 12,
    "quintal": 11,
    "Hundredweight(uk)": 10,
    "Hundredweight(us)": 9,
    "quarter": 8,
    "stone(uk)": 7,
    "stone(us)": 6,
    "pound": 5,
    "troy ounce": 4,
    "ounce": 3,
    "dram": 2,
    "grain": 1,
}
area_to_int = {
    "square nautical mile": 27,
    "square mile": 26,
    "square furlong": 25,
    "Hectare": 24,
    "Feddan": 23,
    "acre": 22,
    "acore": 22,
    "Cuerda": 21,
    "Jerib": 20,
    "kani": 19,
    "rai": 18,
    "Paki": 17,
    "Bigha": 17,
    "Rood": 16,
    "Stremma": 15,
    "Dunam": 15,
    "Mu": 14,
    "Kanal": 13,
    "Guntha": 12,
    "Are": 11,
    "Gonda": 10,
    "Katah": 9,
    "Cotah": 9,
    "Shotangsho": 8,
    "Shotok": 8,
    "square rod": 7,
    "square pole": 7,
    "Marla": 7,
    "Kora": 6,
    "square yard": 5,
    "Ojutangsho": 4,
    "square foot": 3,
    "square inch": 2,
    "Barn": 1,
}

temperature_to_int = {"kelvin": 3, "celsius": 2, "fahrenheit": 1}

weight_conversion_value = {
    12: 10,
    11: 1.9684130552,
    10: 1.12,
    9: 4,
    8: 1.7857142857,
    7: 1.12,
    6: 12.5,
    5: 14.583333333333,
    4: 1.0971428571429,
    3: 8,
    2: 27.34375,
}
time_conversion_value = {
    16: 10**9 / (23 * 10**7),
    15: 23 * 10**4,
    14: 10,
    13: 10,
    12: 10,
    11: 365 / 354.37,
    10: 354.37 / 30,
    9: 30 / 29.53058796,
    8: 29.53058796 / 14,
    7: 2,
    6: 7,
    5: 24,
    4: 60,
    3: 6000000000,
    2: 1.855094832 * (10**35),
}
FPS_unit_values = {7: 1.150779448, 6: 8, 5: 40, 4: 5.5, 3: 3, 2: 12, 1: 12}
# 'converted_value' stored the conversion value. 'for_break ' for stop the unit conversion to another unit, when it is necessary. 'unit_to_another_unit' to excess another unit.
converted_value, unit_to_another_unit, for_break, loop = None, 0, 0, 100


def SI_unit_distance_convesion(value):
    global user_input, converted_value
    operator_function = operator.truediv if user_input < user_target else operator.mul
    condition = (
        [4, 7, 8, 9, 10, 11, 12]
        if user_input < user_target
        else [5, 8, 9, 10, 11, 12, 13]
    )
    converted_value = (
        operator_function(value, 10)
        # 4 : Angstrom / 10 = 0.1 Nano ... 12 : Hec x 10 = 0.1 kilo
        if user_input in condition
        else (
            operator_function(value, 100)
            if user_input == (3 if user_input < user_target else 4)
            # Pico / 100 = 0.0001 angstrom
            else operator_function(value, 1000)
        )
    )
    user_input += (
        1 if user_input < user_target else -1 if user_input > user_target else 0
    )


def length_weight_time_conversion(value):
    global user_input, converted_value
    dictionary_for_conversion_value = (
        FPS_unit_values
        if unit_name == "length"
        else weight_conversion_value if unit_name == "mass" else time_conversion_value
    )
    converted_value = (
        (value / dictionary_for_conversion_value.get(user_input + 1))
        if user_input < user_target
        else (
            (value * dictionary_for_conversion_value.get(user_input))
            if user_input > user_target
            else value
        )
    )

    user_input += (
        1 if user_input < user_target else -1 if user_input > user_target else 0
    )


def temperature_conversion(temperature):
    global user_input, converted_value
    converted_value = (
        ((temperature - 273.15) if user_input == 3 else ((temperature * 9 / 5) + 32))
        if user_input > user_target
        else (
            (
                (temperature + 273.15)
                if user_input == 2
                else ((temperature - 32) * 5 / 9)
            )
            if user_input < user_target
            else temperature
        )
    )
    print(converted_value)
    user_input += (
        1 if user_input < user_target else -1 if user_input > user_target else 0
    )


# Inputs from user
print("\nLength ---> 1\nMass ---> 2\nTemperature --> 3\nTime --> 4")
unit_int_str = input("Which one you choose:").strip(" ").lower()
unit_name = (
    "length"
    if unit_int_str in ["1", "length"]
    else (
        "mass"
        if unit_int_str in ["2", "mass"]
        else "temperature" if unit_int_str in ["3", "temperature"] else "time"
    )
)
# print(unit_name)
user_input_str = (input(f"Enter {unit_name} name:")).strip(" ").lower()
user_target_str = (input(f"Enter {unit_name} target name:")).strip(" ").lower()
distance = eval(input(f"Enter {user_input_str}:"))
user_input_str_copy = user_input_str
user_target_str_copy = user_target_str

# It uptade the 'SI_unit_prefix' dictionary like 'exa' --> 'exameter', 'giga' --> 'gigameter' etc
if unit_name == "length":
    SI_unit_to_int = {
        key + "meter" if value["int"] not in [4, 10] else key: value["int"]
        for key, value in SI_unit_prefix.items()
    }
    # print(SI_unit_to_int)

# It uptade the 'SI_unit_prefix' dictionary like 'exa' --> 'exagram', 'exa' --> 'exasecond' etc
elif unit_name in ["mass", "time"]:
    seclet_suffix = "gram" if unit_name == "mass" else "second"
    SI_unit_to_int = {
        key + seclet_suffix if value["int"] != 10 else seclet_suffix: value["int"]
        for key, value in SI_unit_prefix.items()
    }
    # print(SI_unit_to_int)


# 'user_input' means user input to dictionary value.
user_input = (
    SI_unit_to_int
    if user_input_str in SI_unit_to_int
    else (
        FPS_distance_int
        if user_input_str in FPS_distance_int
        else (
            weight_to_int
            if user_input_str in weight_to_int
            else (
                temperature_to_int
                if user_input_str in temperature_to_int
                else time_to_int
            )
        )
    )
).get(user_input_str)
#'user_target' means user input to dictionary value.
user_target = (
    SI_unit_to_int
    if user_target_str in SI_unit_to_int
    else (
        FPS_distance_int
        if user_target_str in FPS_distance_int
        else (
            weight_to_int
            if user_target_str in weight_to_int
            else (
                temperature_to_int
                if user_input_str in temperature_to_int
                else time_to_int
            )
        )
    )
).get(user_target_str)

# for handel 'exaton','gigaton',etc.
# It makes 'exaton' --> 'exa' for it's exponential.
ton_input_prefix = user_input_str.replace(
    "tonne" if "tonne" in user_input_str else "ton", ""
)
ton_target_prefix = user_target_str.replace(
    "tonne" if "tonne" in user_target_str else "ton", ""
)

if (
    unit_name == "mass"
    and ton_input_prefix in SI_unit_prefix
    and ton_target_prefix in SI_unit_prefix
):
    print("if condition")
    converted_value = distance * (
        SI_unit_prefix.get(ton_input_prefix).get("power")
        / SI_unit_prefix.get(ton_target_prefix).get("power")
    )
    # loop = 1 it's means the "for loop" are not executing.
    loop = 1

# It convert's like's  exaton, gigaton  unit values to ton unit value.
elif (unit_name == "mass") and (ton_input_prefix in SI_unit_prefix):
    converted_value = distance * (SI_unit_prefix.get(ton_input_prefix).get("power"))
    user_input = 12
    user_input_str = "ton"
# It convert's like's  exaton, gigaton unit values to ton unit value.
elif (unit_name == "mass") and (ton_target_prefix in SI_unit_prefix):
    converted_value = distance / (SI_unit_prefix.get(ton_target_prefix).get("power"))
    user_target = 12
    user_target_str = "ton"

# It's choose the dictionary acccording their "unit_name".
change_unit_dictionary = (
    FPS_distance_int
    if unit_name == "length"
    else weight_to_int if unit_name == "mass" else time_to_int
)

if user_input_str in SI_unit_to_int and user_target_str in change_unit_dictionary:
    user_target = 10  # Meter, Gram, Second.
    unit_to_another_unit = 1  # For excess SI_unit_convesion.
    print(f"siiiiii{user_target} {unit_to_another_unit}")
elif user_input_str in change_unit_dictionary and user_target_str in SI_unit_to_int:
    # 2 --> Foot, 5 --> Pound, 3 --> minute.
    user_target = 2 if unit_name == "length" else 5 if unit_name == "mass" else 3
    unit_to_another_unit = 2  # For excess FPS_unit_conversion.
    print(f"changeeeeee{user_target} {unit_to_another_unit}")

# Main
for i in range(1, loop):
    parameter = converted_value if converted_value != None else distance
    # Length or Mass conversion
    if (user_input_str in SI_unit_to_int and user_target_str in SI_unit_to_int) or (
        unit_to_another_unit == 1
    ):
        if user_input != user_target:
            print("SI_unit_distance_convesion")
            SI_unit_distance_convesion(parameter)
        if (
            (unit_to_another_unit == 1)
            and (for_break != 1)
            and (user_input == user_target)
        ):
            print("for_break", for_break)
            print("Unit change, Length conversion")
            unit_change_value = (
                3.280839895
                if unit_name == "length"
                else 0.0022046226 if unit_name == "mass" else (1 / 60)
            )
            if converted_value == None:
                converted_value = 0

            if converted_value != 0:
                converted_value *= unit_change_value  # Meter --> Foot
            else:
                converted_value = distance * unit_change_value  # Meter --> Foot
                print("Unit change, Length conversion", converted_value)
            if (unit_to_another_unit == 1) and (for_break != 1):
                # (user_input --> Foot --> 2, Pound --> 5) (unit_to_another_unit == 2 --> for excess other conversion)
                for_break += 1
                unit_to_another_unit = 2
                user_input = (
                    2 if unit_name == "length" else 5 if unit_name == "mass" else 3
                )
                user_target = (
                    FPS_distance_int
                    if unit_name == "length"
                    else weight_to_int if unit_name == "mass" else time_to_int
                ).get(user_target_str)
                print(user_input, unit_to_another_unit, user_target)

    elif (
        (user_input_str in FPS_distance_int and user_target_str in FPS_distance_int)
        or (user_input_str in weight_to_int and user_target_str in weight_to_int)
        or (user_input_str in time_to_int and user_target_str in time_to_int)
        or (unit_to_another_unit == 2)
    ):
        if user_input != user_target:
            length_weight_time_conversion(parameter)
        if unit_to_another_unit == 2 and for_break != 1 and user_input == user_target:
            unit_change_value_to_si_unit = (
                0.3048
                if unit_name == "length"
                else 453.59237 if unit_name == "mass" else 60
            )
            if converted_value == None:
                converted_value = 0
            if converted_value != 0:
                converted_value *= unit_change_value_to_si_unit
            else:
                converted_value = distance * unit_change_value_to_si_unit
            if (unit_to_another_unit == 2) and (for_break != 1):
                for_break += 1
                user_input, unit_to_another_unit = 10, 1
                user_target = SI_unit_to_int.get(user_target_str)

    elif (unit_name == "temperature") and (user_input != user_target):
        temperature_conversion(parameter)
    # print(user_input, user_target, user_target_str, user_input_str)
    if user_input == user_target:
        break

converted_value = converted_value if converted_value != None else (distance)
print(
    f"\n{distance} {user_input_str_copy} is equivalent {converted_value} {user_target_str_copy}\n"
)


area_to_int = {""}
"""
Paki, Bigha 1337.8050706528304
Shotangsho,Shotok, 40.46860338724812
Katah,Cotah 66.89025353264152
Ojutangsho 0.40468603387248114
Kora 20.067076059792456
Gonda 80.26830423916982
Kani 1605.3660847833964
acre,Acore 4046.8603387248118
til 0.337238361560401"""
"""area_to_int = {
    "square nautical mile": 27,
    "square mile": 26,
    "square furlong": 25,
    "Hectare": 24,
    "Feddan": 23,
    "acre": 22,
    "acore": 22,
    "Cuerda": 21,
    "Jerib": 20,
    "kani": 19,
    "rai": 19,
    "Paki": 18,
    "Bigha": 18,
    "Rood": 17,
    "Stremma": 16,
    "Dunam": 16,
    "Mu": 15,
    "Kanal": 14,
    "Guntha": 13,
    "Are": 12,
    "Gonda": 11,
    "Katah": 10,
    "Cotah": 10,
    "Shotangsho": 9,
    "Shotok": 9,
    "square rod": 8,
    "square pole": 8,
    "Marla": 8,
    "Kora": 7,
    "square yard": 6,
    "Ojutangsho": 5,
    "til": 4,
    "square foot": 3,
    "square inch": 2,
    "Barn": 1,

}"""
"""square "nautical mile": 34299043 
square mile":  2589988.110336
square furlong": 40468.726
square rod",'pole: 25.29285264 
square yard": 0.83612736
square foot": 0.09290304
square inch": 0.00064516

Hectare (ha) 10000
Are (a) 100
Barn (b) 1.E-28
Dunam 1000
Feddan 4200
Rood 1011.7141056
Mu 666.6666666666666
Guntha 101.17141049999999324882
Rai 1600
Kanal 505.85705259999997451814
Marla 25.29285262999999872591
Stremma 1000
Jerib 2000
Cuerda 3930.395625

1 Shotangsho = 40.46860338724812 Square meter.
"""
1000
34299043
2589988.110336
40468.726
10000
4200
4046.8603387248118
3930.395625
2000
1605.3660847833964
600
1337.8050706528304
1011.7141056
1000
1000
666.6666666666666
505.8570526
101.1714105
100
80.26830423916982
66.89025353264152
40.46860338724812
25.29285264
25.29285263
20.067076059792456
0.83612736
0.40468603387248114
0.337238361560401
0.09290304
0.00064516


a = 435601.74134237 / 107639.10417
b = 40468.726 / 10000
print(b)
