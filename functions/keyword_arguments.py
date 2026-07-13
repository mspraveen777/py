def default_arg(maths,sci,hindi,kannada =0):
    print(f"maths= {maths}")
    print(f"science= {sci}")
    print(f"hindi= {hindi}")
    print(f"kannada= {kannada}")
    total_marks = maths + sci + hindi + kannada
    print(f"Total Marks= {total_marks}")
default_arg(hindi = 99, kannada = 100, maths= 30,sci=34)
default_arg(35,40,hindi = 99, kannada = 100)
