def remove_patterns(strings): # Task 4.1
# strings is in the format:
# original_string,pattern_1,pattern_2,….
# Find ALL patterns within the original_string and remove them out. If
# the same pattern found more than once, remove all of them.
# All remaining fragmented substrings need to be concatenated together
# in order and return as a new string called edited_string (See
# Figure 4.1 to see how this function works)
# Write your code here
    s=strings.split(',')
    s1,s2=s[0],s[1:]
    edited_string=s1
    for i in s2:
        edited_string=''.join(edited_string.split(i))
    return edited_string
def check_coverage(strings): # Task 4.2
# strings is in the format:
# reference_string,pattern_1,pattern_2, ….
# Check if patterns when aligned to the reference string will cover all
# characters within the reference string.
# Return string “Covered” if they can cover, otherwise return the
# indices of all positions in the references that are not covered
# (See Figure 4.2 to see how this function works
# Hint: You can use find()
# Do not remove the following statement
    exec(input().strip())

print(remove_patterns("ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789ABCDEFG,ABC,PQRS"))
print('DEFGHIJKLMNOTUVWXYZ0123456789DEFG')
print(remove_patterns("AAABBCCDDDCCCAAAAAAAAA,AA,CC"))