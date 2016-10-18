The null is properly formulates in wording and in formulae.

Good data wrangling, the data supports the question. Good simple coding style.


Now that you have the mean age you can simply proceed to a test of means between 2 samples (t-test)


Generally you do not want to print that many decimal digits, as they are not significant. For age, likely 1 or 2 decimal digit is appropriate. with a stdev of 11, 1 is enough.
print("Age_m:", age_m, "  std:", std_age_m)
print("Age_f:", age_f, "  std:", std_age_f)

use instead something like

print("Age_m: %.1f  std: %.1f"%(age_m, std_age_m))

or more elegantly (and sort of more modern pythonic style)

print("Age_m: {0:.1f} std: {1:.1f}".format(age_m, std_age_m))
