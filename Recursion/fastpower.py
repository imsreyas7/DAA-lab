
    def fast_power(base, power):
        result = 1
        while power > 0:
            # If power is even
            if power % 2 == 0:
                # Divide the power by 2
                power = power // 2
                # Multiply base to itself
                base = base * base
            else:
                # Decrement the power by 1 and make it even
                power = power - 1
                # Take care of the extra value that we took out
                # We will store it directly in result
                result = result * base

                # Now power is even, so we can follow our previous procedure
                power = power // 2
                base = base * base

        return result

x=int(input("Enter the number for which the power has to be found "))
n=int(input("Enter the power "))
print("The result is ",fast_power(x,n))