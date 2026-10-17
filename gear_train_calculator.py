print("\n⚙️ Gear Train & Power Transmission Calculator\n")

# User Inputs
driver_teeth = int(input("Driver Gear Teeth: "))
driven_teeth = int(input("Driven Gear Teeth: "))
input_rpm = float(input("Input RPM: "))
input_torque = float(input("Input Torque (Nm): "))

# Validation
if driver_teeth <= 0:
    print("\n❌ Driver gear teeth must be greater than zero.")
    exit()

if driven_teeth <= 0:
    print("\n❌ Driven gear teeth must be greater than zero.")
    exit()

# Calculations
gear_ratio = driven_teeth / driver_teeth

output_rpm = input_rpm / gear_ratio

output_torque = input_torque * gear_ratio

# Results
print("\n========== RESULTS ==========")

print(f"Driver Gear Teeth : {driver_teeth}")
print(f"Driven Gear Teeth : {driven_teeth}")

print(f"\nGear Ratio        : {gear_ratio:.2f}:1")

print(f"\nInput RPM         : {input_rpm:.2f}")
print(f"Output RPM        : {output_rpm:.2f}")

print(f"\nInput Torque      : {input_torque:.2f} Nm")
print(f"Output Torque     : {output_torque:.2f} Nm")

print("\n=============================")

# Engineering Interpretation
print("\nEngineering Insight:")

if gear_ratio > 1:
    print(
        "The gear train increases torque while reducing rotational speed, "
        "providing mechanical advantage."
    )
elif gear_ratio < 1:
    print(
        "The gear train increases rotational speed while reducing torque, "
        "favoring higher-speed operation."
    )
else:
    print(
        "The gear train maintains equal rotational speed and
