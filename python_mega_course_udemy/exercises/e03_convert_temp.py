def celsius_to_f(celsius):
    if celsius < -273.15:
        return "That temperature doesn't make sense!"
    else:
        return 9.0/5.0 * celsius + 32

print(celsius_to_f(27))
print(celsius_to_f(-273.4))