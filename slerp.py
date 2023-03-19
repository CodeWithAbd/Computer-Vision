import math

def slerp(q0, q1, alpha):
    dot = sum([a * b for a, b in zip(q0, q1)])
    theta = math.acos(dot)
    if abs(theta) < 1e-10:
        return q0
    else:
        q1_scale = math.sin((1 - alpha) * theta) / math.sin(theta)
        q2_scale = math.sin(alpha * theta) / math.sin(theta)
        return [q1_scale * q0[i] + q2_scale * q1[i] for i in range(len(q0))]

# Returning q0
print("Returning from the if statement: ")
q0 = [1, 0, 1, 0]
q1 = [1, 1, 0, 1]
alpha = 0.25
interpolatedQuent = slerp(q0, q1, alpha)
print(interpolatedQuent)

print("\n")

print("Returning from the else statement: ")
q0 = [1, 0, 0, 0]
q1 = [0, 1, 0, 0]
alpha = 0.5
interpolatedQuent = slerp(q0, q1, alpha)
print(interpolatedQuent)